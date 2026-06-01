from agents.base_agent import SpecialistAgent
from config.prompts import (
    SOFTWARE_ARCHITECT_PROMPT,
    CLEAN_CODE_EVANGELIST_PROMPT,
    ALGORITHM_MATHEMATICIAN_PROMPT,
    ACADEMIC_SCOPING_POLICEMAN_PROMPT,
    SCIENTIFIC_RHETORIC_TUTOR_PROMPT,
    OBJECTIVITY_AND_BIAS_AUDITOR_PROMPT,
    EDGE_CASE_ANALYST_PROMPT
)

software_architect = SpecialistAgent("software_architect", SOFTWARE_ARCHITECT_PROMPT)
clean_code_evangelist = SpecialistAgent("clean_code_evangelist", CLEAN_CODE_EVANGELIST_PROMPT)
algorithm_mathematician = SpecialistAgent("algorithm_mathematician", ALGORITHM_MATHEMATICIAN_PROMPT)
academic_scoping_policeman = SpecialistAgent("academic_scoping_policeman", ACADEMIC_SCOPING_POLICEMAN_PROMPT)
scientific_rhetoric_tutor = SpecialistAgent("scientific_rhetoric_tutor", SCIENTIFIC_RHETORIC_TUTOR_PROMPT)
objectivity_and_bias_auditor = SpecialistAgent("objectivity_and_bias_auditor", OBJECTIVITY_AND_BIAS_AUDITOR_PROMPT)
edge_case_analyst = SpecialistAgent("edge_case_analyst", EDGE_CASE_ANALYST_PROMPT)

software_architect_node = software_architect.invoke_agent
clean_code_evangelist_node = clean_code_evangelist.invoke_agent
algorithm_mathematician_node = algorithm_mathematician.invoke_agent
academic_scoping_policeman_node = academic_scoping_policeman.invoke_agent
scientific_rhetoric_tutor_node = scientific_rhetoric_tutor.invoke_agent
objectivity_and_bias_auditor_node = objectivity_and_bias_auditor.invoke_agent
edge_case_analyst_node = edge_case_analyst.invoke_agent
