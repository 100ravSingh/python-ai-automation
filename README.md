# ✅ **1. `.github/copilot-instructions.md` — GLOBAL BEHAVIOR BRAIN**

### **What it does**

This file defines the **overall rules, standards, preferences, and coding style** for the entire repository.

It tells Copilot:

* How you want code to be written
* Which libraries to use
* What conventions to follow
* How to handle errors
* How scripts should be structured
* How APIs, React components, or pipelines should look
* What not to do (e.g., no prints, no secrets, always use pathlib)

### **How it works**

Copilot automatically reads this file **every time it generates code inside this repo**.

It becomes the *default mindset* of Copilot.

Even without prompting, Copilot will:

* Use logging instead of print
* Use pathlib
* Add main() in Python scripts
* Follow your folder structure
* Suggest cleaner patterns

🧠 Think of this file as:
**“Your coding style + rules that Copilot must obey.”**

---

# ✅ **2. `.github/agents/*.agent.md` - GitHub Copilot Custom Agents**

This repository defines a set of Copilot Chat agents, each with a focused role and a set of behavior rules.

## Available agents

- [PythonAutomationAgent](./agents/PythonAutomationAgent.agent.md)
- [NodeApiAgent](./agents/NodeApiAgent.agent.md)
- [ReactFrontendAgent](./agents/ReactFrontendAgent.agent.md)
- [DevOpsCICDAgent](./agents/DevOpsCICDAgent.agent.md)
- [DataSQLAgent](./agents/DataSQLAgent.agent.md)
- [AIMLAgent](./agents/AIMLAgent.agent.md)
- [DebugAgent](./agents/DebugAgent.agent.md)
- [TestAgent](./agents/TestAgent.agent.md)
- [DocAgent](./agents/DocAgent.agent.md)
- [RefactorAgent](./agents/RefactorAgent.agent.md)
- [ArchitectureAdvisor](./agents/ArchitectureAdvisor.agent.md)
- [UTDocAgent](./agents/UTDocAgent.agent.md)

> Each agent file contains the role, responsibilities, behavior rules, and output format.
```
@PythonAutomationAgent create a script that processes CSV files daily
```

Copilot instantly switches personality and responds *as that expert*.

🧠 Think of this file as:
**“Your private team of AI specialists, each with a job.”**

---

# ✅ **3. `.github/prompts/python-automation.md` — REUSABLE TASK-LEVEL PROMPTS**

### **What it does**

This is a collection of **reusable instruction blocks** for common tasks you automate.

Examples:

* File processing automation
* CSV/Excel cleaning
* API automation
* Cron/scheduler-friendly scripts
* Folder sync/backup scripts
* Web scraping
* System monitoring
* Database automation
* OOP automation frameworks

These are *templates* that Copilot follows to generate predictable, clean code.

### **How it works**

You can:

* Paste a block into Copilot Chat
* Or reference it above your code:

```python
# Use: "File Processing Automation" from .github/prompts/python-automation.md
```

Copilot will then generate the code following the exact pattern from that prompt.

🧠 Think of this file as:
**“Your library of ready-made instructions for repeat automation tasks.”**

---

# 🚀 **How all 3 work together**

| Component                        | Purpose              | How it helps                                                                     |
| -------------------------------- | -------------------- | -------------------------------------------------------------------------------- |
| **copilot-instructions.md**      | Global rules         | Defines coding style, structure, patterns — the default way Copilot behaves      |
| **copilot-agents.md**            | Specialized personas | Gives you AI experts you can activate on demand                                  |
| **prompts/python-automation.md** | Task templates       | Provides structured patterns Copilot should follow for specific automation tasks |

Together they create a **full Copilot programming environment**:

### ✔ Consistent code

### ✔ Cleaner automation scripts

### ✔ Specialized AI help on demand

### ✔ Faster workflow, fewer mistakes

### ✔ No repeating instructions manually

---

# 🧠 In simple words:

**1. Copilot Instructions → How Copilot should behave always**
**2. Copilot Agents → What expert Copilot should become**
**3. Prompts → What exact pattern Copilot should follow for each type of task**

---

# AI Agent Toolkit (optional)

This repo also includes a small **agent toolkit** under `ai/mcp/` that lets you run the same agent personalities programmatically.

- `ai/mcp/tools/__init__.py` registers a set of tools (one per agent).
- Each tool lives in `ai/mcp/ai/<AgentName>.py` and implements `BaseTool.run(prompt: str) -> str`.
- You can list/run tools via `ai/mcp/server.py`.

### Quick start (Python)

```py
from ai.mcp import server

print(server.list_tools())
print(server.run_tool('PythonAutomationAgent', 'create a small backup script'))
```

> See `ai/README.md` for more details.
