# Pull Request – Multi-Agent Debate Ecosystem (LangGraph + Gemini)

Thank you for your contribution! Please fill out the information below to facilitate the analysis, architectural validation, and code review of this Pull Request.

---

## Proposal Description

Clearly describe which component of the graph or ecosystem is being implemented or modified:

> _Example: Implementation of the 'DebateState' data contract and isolation of Gemini API keys into a structured configuration class._

---

## Type of Change

Mark with an `x` the categories that apply to this PR:

- [ ] Bug fix (bugfix in the Graph or Nodes)
- [ ] New feature (agent, node, or router feature)
- [ ] Code Refactoring (Clean Code / SOLID Principles)
- [ ] Prompt Engineering adjustment (System Prompts)
- [ ] Performance improvement (Asynchronous calls / Token optimization)
- [ ] Documentation or Log updates (.md)

---

## Testing and Graph Validation

Describe how you tested the physical and logical execution of the nodes/state (e.g., type checking with Mypy, workflow execution in the terminal):

> _Example: Verified that the linter does not throw initialization errors with NotRequired fields. Tested the dictionary union (|) function, ensuring the immutability of the old state._

---

## Modified / Added Files

List the main files changed in this PR:

> _Example:_
> - `graph/state.py`
> - `config/settings.py`

---

## Required Environment Variables (If applicable)

State if this PR requires new keys or parameters in the `.env` file:

> _Example: Requires `GEMINI_API_KEY` configured in the local `.env` file._

---

## Developer Checklist

Before submitting, verify that you have met the project's quality guidelines:

- [ ] Code written with strict Type Hints;
- [ ] Functions respect the Single Responsibility Principle (SOLID);
- [ ] Variable and function names are readable and self-explanatory (Clean Code);
- [ ] No API keys are hardcoded directly into the code;
- [ ] The `requirements.txt` file was updated if new libraries were installed.

---