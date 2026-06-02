from datetime import datetime
from pathlib import Path
from graph.state import DebateState
from utils.logger import logger

def save_debate_to_markdown(state: DebateState, base_dir: str = "outputs") -> str:
    try:
        output_path = Path(base_dir)
        output_path.mkdir(parents=True, exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_target = output_path / f"debate_report_{timestamp}.md"

        final_socratic_response = state["messages"][-1].content

        agent_analyses = state.get("agent_analyses") or {}

        md_content = f"""# Multi-Agent Debate Ecosystem - Session Report
Generated on: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
---

## Master Socratic Synthesis
{final_socratic_response.strip()}

---

## Detailed Specialist Audits
"""

        if not agent_analyses:
            md_content += "\n*No individual specialist analyses were recorded for this session.*\n"
        else:
            for agent_name, analysis in agent_analyses.items():
                md_content += f"\n### Specialist: {agent_name.upper()}\n"
                md_content += f"```text\n{analysis.strip()}\n```\n"
                md_content += "---\n"

        file_target.write_text(md_content, encoding="utf-8")

        logger.info(f"Session successfully persisted to: {file_target.resolve()}")
        return str(file_target.resolve())
    
    except Exception as e:
        logger.error(f"Failed to persist debate report to filesystem: {str(e)}")
        raise e