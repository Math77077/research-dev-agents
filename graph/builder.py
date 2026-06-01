from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import StateGraph, START, END
from config.settings import SystemSettings
from graph.state import DebateState
from agents.specialists import (
    software_architect_node,
    clean_code_evangelist_node,
    algorithm_mathematician_node,
    academic_scoping_policeman_node,
    scientific_rhetoric_tutor_node,
    objectivity_and_bias_auditor_node,
    edge_case_analyst_node
)

async def supervisor_router_node(state: DebateState) -> dict:
    llm = ChatGoogleGenerativeAI(
        model=SystemSettings.MODEL_NAME,
        google_api_key=SystemSettings.GEMINI_API_KEY,
        temperature=0.0
    )

    system_prompt = SystemMessage(
        content=(
            "Analyze the user's input. If it contains source code, programming logic, or software engineering questions, reply with exactly one word: 'CODE'. If it contains scientific text, thesis topics, methodology, or academic drafts, reply with exactly one word: 'ACADEMIC'."
        )
    )

    user_input = state['messages'][-1]
    response = await llm.ainvoke([system_prompt, user_input])
    return {
        "messages": [AIMessage(content=response.content.strip())]
    }

async def synthesizer_node(state: DebateState) -> dict:
    llm = ChatGoogleGenerativeAI(
        model=SystemSettings.MODEL_NAME,
        google_api_key=SystemSettings.GEMINI_API_KEY,
        temperature=0.7
    )

    current_analyses = state.get("agent_analyses") or {}

    formatted_analyses = ""
    for agent_name, analysis_content in current_analyses.items():
        formatted_analyses += f"\n=== ANALYSIS FROM: {agent_name.upper()} ===\n"
        formatted_analyses += f"{analysis_content}\n"
        formatted_analyses += "=========================================\n"

    system_prompt = SystemMessage(
        content=(
            "You are the Master Debate Synthesizer and Academic Committee Chair. Your job is to read all specialist insights provided by the panel, detect core contradictions, and compile a beautiful, single unified review. CRITICAL: You must NEVER give code chunks or direct copy-paste solutions. Adopt a strict Socratic and Active Learning approach: guide the student by highlighting where they succeeded, where the committee found fatal flaws, and wrap up with clear, guiding questions to steer their next autonomous step."
        )
    )

    user_payload = HumanMessage(
        content=(
            f"Here is the specialized committee debate feedback regarding my submission:\n"
            f"{formatted_analyses}\n"
            f"Please synthesize their findings and guide me through the next steps socratically."
        )
    )

    response = await llm.ainvoke([system_prompt, user_payload])
    return {
        "messages": [AIMessage(content=response.content)]
    }

def where_to_go(state: DebateState) -> str:
    last_message = state['messages'][-1]
    decision_track = last_message.content.strip()

    if decision_track == 'CODE':
        return "technical_track"
    elif decision_track == 'ACADEMIC':
        return "academic_track"
    return "end_track"

workflow = StateGraph(DebateState)
workflow.add_node("supervisor", supervisor_router_node)

workflow.add_node("architect", software_architect_node)
workflow.add_node("clean_code", clean_code_evangelist_node)
workflow.add_node("mathematician", algorithm_mathematician_node)
workflow.add_node("edge_case", edge_case_analyst_node)

workflow.add_node("scoping", academic_scoping_policeman_node)
workflow.add_node("rhetoric", scientific_rhetoric_tutor_node)
workflow.add_node("bias", objectivity_and_bias_auditor_node)

workflow.add_node("synthesizer", synthesizer_node)

workflow.add_edge(START, "supervisor")

workflow.add_conditional_edges(
    "supervisor",
    where_to_go,
    {
        "technical_track": ["architect", "clean_code", "mathematician", "edge_case"],
        "academic_track": ["scoping", "rhetoric", "bias"],
        "end_track": END
    }
)

all_specialists = ["architect", "clean_code", "mathematician", "edge_case", "scoping", "rhetoric", "bias"]

for specialist in all_specialists:
    workflow.add_edge(specialist, "synthesizer")

workflow.add_edge("synthesizer", END)
debate_graph = workflow.compile()