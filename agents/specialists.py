from agents.base_agent import SpecialistAgent
from config.prompts import (
    SOFTWARE_ENGINEER_PROMPT,
    SCIENTIFIC_REVIEWER_PROMPT,
    EDGE_CASE_ANALYST_PROMPT
)

software_engineer = SpecialistAgent("software_engineer", SOFTWARE_ENGINEER_PROMPT)
scientific_reviewer = SpecialistAgent("scientific_reviewer", SCIENTIFIC_REVIEWER_PROMPT)
edge_case_analyst = SpecialistAgent("edge_case_analyst", EDGE_CASE_ANALYST_PROMPT)

software_engineer_node = software_engineer.invoke_agent
scientific_reviewer_node = scientific_reviewer.invoke_agent
edge_case_analyst_node = edge_case_analyst.invoke_agent
