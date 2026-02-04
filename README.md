# ETL Lab 1: Introduction to ETL Processes

This repository contains the implementation of the first laboratory for the ETL course. The main objective is to understand the end-to-end data pipeline: Extract, Transform, and Load.

## Project Structure

```
ETL_Lab_1/
│
├── data/
│   ├── raw/                # Original input files (CSV, JSON, XML)
│   ├── transformed/        # Output CSV file
│   └── database/           # SQLite database file
│
├── src/
│   ├── extract.py          # Functions to extract data from multiple formats
│   ├── transform.py        # Logic to clean and standardize data
│   ├── load.py             # Functions to save to CSV and Database
│   ├── main.py             # Main script that orchestrates the workflow
│   ├── log.py              # Logging utility
│   └── db.py               # Helper to run SQL queries
│
├── logs/
│   └── log_file.txt        # Execution logs
│
└── reflection_questions.md # Answers to the lab's reflection questions
```

## How to Run (Using uv)

This project uses `uv` for modern, fast dependency management. This ensures that everyone running the project has the exact same environment and libraries.

### 1. Install uv
If you don't have `uv` installed, get it here: [https://docs.astral.sh/uv/getting-started/installation/](https://docs.astral.sh/uv/getting-started/installation/)

For example, on Windows (PowerShell):
```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 2. Run the Project
You don't need to manually create a virtual environment. `uv` handles it for you.
Simply run:

```bash
uv run src/main.py
```

This command will:
*   Automatically create a virtual environment.
*   Install all required libraries (like pandas) defined in `pyproject.toml`.
*   Run the script.

## Project Dependencies
*   Python 3 (Managed by uv)
*   Pandas
*   SQLite
