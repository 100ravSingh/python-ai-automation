# Python Automation – Reusable Prompt Library

Use these prompts with GitHub Copilot Chat or as comments above code.
They are aligned with `.github/copilot-instructions.md` and the `PythonAutomationAgent`.

---

## 1. Python Automation Script Template

> Prompt:
> Create a Python automation script with the following standards:
> - Use functions for every logical block.
> - Add `argparse` for CLI input arguments.
> - Include `logging` with debug, info, warning, error.
> - Wrap main logic inside `if __name__ == "__main__": main()`.
> - Add `try/except` for error handling with informative messages.
> - Use `pathlib` instead of `os.path` for file paths.
> - Ensure PEP 8 compliance and include type hints where helpful.
> Return complete code.

---

## 2. File Processing Automation

> Prompt:
> Write a Python script that:
> - Reads files from a given directory (recursive).
> - Filters files by extension.
> - Processes them in batches.
> - Includes error handling for unreadable files.
> - Writes output to a timestamped folder.
> - Logs all steps to a log file using the `logging` module.

---

## 3. Excel / CSV Automation (pandas)

> Prompt:
> Generate a Python automation script using `pandas` that:
> - Loads CSV/Excel files dynamically from a path or glob pattern.
> - Validates columns and data types.
> - Removes duplicates and empty rows.
> - Applies transformations using pure functions.
> - Saves output to a `processed/` folder with timestamped filenames.
> - Logs summary statistics (rows in/out, dropped, etc.).

---

## 4. API Automation

> Prompt:
> Create a Python API automation script that:
> - Uses `requests` for GET/POST with retry logic (e.g., via `urllib3.Retry`).
> - Accepts endpoint and payload via `argparse`.
> - Logs response status, headers, and truncated body.
> - Validates JSON response and handles non-JSON responses gracefully.
> - Saves failed requests to a retry queue file (e.g., JSONL).
> - Reads API key or token from environment variables only.

---

## 5. Scheduler-Friendly Jobs (Cron / Task Scheduler)

> Prompt:
> Write a Python script designed to run on a scheduler:
> - No interactive input.
> - Use `logging` instead of `print`.
> - Validate all external file paths and config upfront.
> - Handle network/unavailable resource errors with retries and backoff.
> - Optionally send an email or webhook notification if the job fails.
> - Log a final summary line with counts (e.g., processed, failed, duration).

---

## 6. Directory Sync / Backup Automation

> Prompt:
> Develop a Python automation tool that:
> - Syncs two folders (`source` → `destination`).
> - Compares file hashes or modification times to detect changes.
> - Copies only modified or new files.
> - Logs every action (copied, skipped, failed).
> - Generates a sync summary report with counts and elapsed time.

---

## 7. Web Scraping Automation

> Prompt:
> Produce a Python script that:
> - Uses `requests` + `BeautifulSoup`.
> - Supports URL input from CLI.
> - Extracts structured data into CSV or JSON.
> - Handles pagination (next links or page numbers).
> - Includes delay/random sleep to avoid aggressive scraping.
> - Logs scraping steps and all errors.

---

## 8. System Monitoring Automation

> Prompt:
> Create a system monitoring script that:
> - Uses `psutil` to read CPU, RAM, and disk usage.
> - Logs metrics with timestamps at a fixed interval.
> - Uses configurable thresholds for warnings.
> - Writes logs using a rotating file handler.
> - Optionally sends alerts via webhook when thresholds are breached.

---

## 9. Database Automation

> Prompt:
> Generate a Python script that:
> - Connects to a database (SQLite/MySQL/PostgreSQL).
> - Reads credentials from environment variables or config file.
> - Executes parameterized queries safely.
> - Fetches, transforms, and exports data to CSV/JSON.
> - Includes retry logic for transient failures.
> - Logs all DB operations and number of rows affected.

---

## 10. OOP-Based Automation Framework

> Prompt:
> Create a Python automation framework using OOP:
> - Implement a `BaseTask` class with `run()`, `validate()`, and `log()` methods.
> - Create derived classes for specific tasks (e.g., `FileTask`, `ApiTask`).
> - Use dependency injection for configuration and logger.
> - Implement a `TaskManager` to orchestrate multiple tasks.
> - Add example `pytest` tests for at least one task class.

---

## How to Use

- In **Copilot Chat**:
  - Copy a prompt block and paste it along with your request.
  - Optionally mention `@PythonAutomationAgent` to specialize behavior.
- In code, you can add a comment:
  ```python
  # Use: "File Processing Automation" from prompts/python-automation.md
