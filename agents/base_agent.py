from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage
from config.settings import SystemSettings
from graph.state import DebateState

class SpecialistAgent:
    def __init__(self, agent_name: str, system_prompt: str):
        self.name = agent_name
        self.system_prompt = system_prompt

        self.llm = ChatGoogleGenerativeAI(
            model=SystemSettings.MODEL_NAME,
            google_api_key=SystemSettings.GEMINI_API_KEY,
            temperature=SystemSettings.TEMPERATURE
        )

    async def invoke_agent(self, state: DebateState) -> dict:
        system_message = SystemMessage(content=self.system_prompt)
        full_messages = [system_message] + state['messages']
        response = await self.llm.ainvoke(full_messages)
        
        return {
            "agent_analyses": {
                self.name: response.content
            }
        }