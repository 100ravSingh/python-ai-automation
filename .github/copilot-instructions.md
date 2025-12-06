# GitHub Copilot – Repo Instructions

## Project Context

- Primary language: **Python**
- Focus: **automation scripts, tooling, backend/API work, DevOps, and frontend integrations**
- Tech stack:
  - Python (automation, ETL, ML helpers)
  - Node.js / Express (APIs, services)
  - React (frontend)
  - CI/CD (GitHub Actions, DevOps pipelines)
- Style: **clean, modular, production-oriented** code.

---

## Global Coding Standards

- Follow **PEP 8** for Python and idiomatic patterns for JS/TS/React.
- Prefer **small, focused functions and classes** over long scripts.
- Use **type hints** in Python for non-trivial functions.
- Use **`logging`** instead of `print()` in automation or production scripts.
- Use **`pathlib`** instead of `os.path` for file paths.
- Keep code **environment-agnostic** (no hard-coded absolute paths).

---

## Configuration & Secrets

- Read configuration from:
  - Environment variables, OR
  - Config files (YAML/JSON/INI) committed without secrets.
- Never hard-code **secrets, API keys, or passwords**.
- For examples, use placeholders like `YOUR_API_KEY_HERE` or environment variables like `API_KEY`.

---

## Error Handling & Reliability

- Wrap critical sections in `try/except`.
- Log errors with enough context (inputs, file paths, environment assumptions).
- Prefer failing fast with clear messages over silent failure.
- When unsure about behavior, add a brief comment or docstring.

---

## Python Automation Conventions

For Python automation scripts:

- Every script should:
  - Define a `main()` function.
  - Use `if __name__ == "__main__": main()`.
  - Optionally use `argparse` for CLI arguments.
  - Use the `logging` module with `DEBUG`, `INFO`, `WARNING`, `ERROR`.
- Prefer **modular design**:
  - Core logic in `src/` modules.
  - Simple entrypoints in `scripts/`.

For common automation scenarios (file processing, APIs, schedulers, backups, scraping, monitoring, DB, OOP frameworks), align with the patterns defined in:

- `prompts/python-automation.md`

---

## Testing

- Python:
  - Use **pytest** style tests.
  - Name tests descriptively: `test_<condition>_<expected_result>`.
- JavaScript/TypeScript:
  - Use **Jest** / Testing Library where relevant.
- For non-trivial logic:
  - Generate at least one example test file when asked.

---

## Copilot Custom Agents

This repo defines specialized **task-specific agents** in:

- `.github/copilot-agents.md`

When using Copilot Chat, prefer these agents:

- `@PythonAutomationAgent` for Python automation, ETL, system scripts.
- `@NodeApiAgent` for Node.js / Express APIs.
- `@ReactFrontendAgent` for React UI work.
- `@DevOpsCICDAgent` for pipelines and infra workflows.
- `@DataSQLAgent` for SQL and data tasks.
- `@AIMLAgent` for AI/ML related work.
- `@DebugAgent` for debugging.
- `@TestAgent` for tests.
- `@DocAgent` for docs, README, docstrings.
- `@RefactorAgent` for improving existing code.
- `@ArchitectureAdvisor` for system design.

You can call them by name, for example:

- `@PythonAutomationAgent create a script that processes CSV files on a schedule.`
- `@DevOpsCICDAgent set up a GitHub Actions workflow for tests + linting + deploy.`

---

## Output Expectations

When the user asks for:

- A **script** → Provide a complete, runnable script with a `main()` entrypoint where appropriate.
- A **module** → Provide cohesive, importable code, not just fragments.
- A **configuration** → Provide full file content (YAML, JSON, etc.), with brief comments.
- A **design or architecture** → Provide a structured explanation, optionally with a simple text diagram.

Where appropriate:

- Suggest a **folder structure**.
- Indicate any **dependencies** (e.g., `pip install ...`, `npm install ...`).
- Add **short docstrings** for important functions and classes.

---

## Don’ts

- Don’t use deprecated or obscure APIs without a good reason.
- Don’t mix **business logic** and **I/O or CLI parsing** in a messy way.
- Don’t generate huge unstructured files when a modular layout makes more sense.
- Don’t expose secrets in examples.
