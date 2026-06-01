from typing import Annotated, TypedDict, List, Dict, Optional, NotRequired
from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages

def merge_analyses(old_value: Optional[Dict[str, str]], new_value: Dict[str, str]) -> Dict[str, str]:
    if not old_value:
        return new_value
    return old_value | new_value

class DebateState(TypedDict):
    messages: Annotated[List[BaseMessage], add_messages]
    raw_input: str

    input_type: NotRequired[str]
    output_filepath: NotRequired[str]
    debate_concluded: NotRequired[bool]

    agent_analyses: Annotated[Dict[str, str], merge_analyses]    