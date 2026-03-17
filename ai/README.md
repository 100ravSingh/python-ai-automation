# AI Agent Toolkit (ai/)

This folder contains a small *agent toolkit* used to power Copilot-like automation workflows.
Each agent is represented by a `Tool` implementation that knows how to handle a prompt and return a result.

---

## Quick Start (interactive)

```bash
python -c "from ai.mcp import server; print(server.list_tools()); print(server.run_tool('PythonAutomationAgent', 'generate a small script'))"
```

### Example (Python REPL)

```py
from ai.mcp import server

# list available agents
print(server.list_tools())

# run an agent
result = server.run_tool('PythonAutomationAgent', 'create a small backup script')
print(result)
```

---

## Available Agents

At runtime the following agent tools are registered (see `ai/mcp/tools/__init__.py`):

- `PythonAutomationAgent` (generates basic Python automation scripts)
- `NodeApiAgent` (generates starter Node/Express API guidance)
- `ReactFrontendAgent` (generates starter React UI guidance)
- `DevOpsCICDAgent` (generates CI/CD workflow guidance)
- `DataSQLAgent` (generates SQL/data workflow guidance)
- `AIMLAgent` (generates AI/ML script guidance)
- `DebugAgent` (generates debugging/troubleshooting guidance)
- `TestAgent` (generates test plan/test code guidance)
- `DocAgent` (generates documentation snippets)
- `RefactorAgent` (generates refactoring suggestions)
- `ArchitectureAdvisor` (generates architecture/design guidance)
- `UTDocAgent` (generates unit test documentation guidance)

> If you add a new tool class under `ai/mcp/ai/`, add it to the `TOOLS` registry in `ai/mcp/tools/__init__.py`.

---

## Extending the Agents

Each agent is implemented as a small Python class under `ai/mcp/ai/` that derives from `ai.mcp.tools.base.BaseTool`.

To add logic:
1. Edit the `run(self, prompt: str) -> str` method in the corresponding module (for example `ai/mcp/ai/node_api.py`).
2. Make it do the work you want (e.g., call an LLM, generate files, etc.).
3. Keep the method signature the same so the registry still works.

---

## Copilot Agent Definitions

This repo also includes Copilot agent definitions in `.github/agents/*.agent.md`.
Those files define how each agent should behave when invoked within Copilot Chat.

---

## Notes

- This repo does not include a full “server” HTTP API by default — the entrypoint is the `ai.mcp.server` module.
- The current agent implementations mostly return placeholder strings; they're intended as a starting point for more advanced logic.
