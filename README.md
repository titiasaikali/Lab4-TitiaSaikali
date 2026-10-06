# EECE 435L Lab 4 ? Git and GitHub

Student: **Titia Saikali** | October 6, 2026 | Solo

## Project: Task Manager
Both Tkinter and PyQt6 interfaces support adding, completing/reopening, deleting,
and refreshing tasks. They use one SQLite backend at `data/tasks.sqlite3`.
Data persists after closing. Click Refresh to see changes from the other GUI.
Run each interface in its own process so their event loops remain independent.

## Setup and run (PowerShell)
Open Lab4 in VS Code. Python 3.10+ with Tkinter is required.
The local `.venv` is prepared; after cloning, recreate it:
```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe src\tkinter_ui.py
```
Run PyQt in a second terminal:
```powershell
.\.venv\Scripts\python.exe src\pyqt_ui.py
```
Select a task to toggle or delete it. Blank titles are rejected.
The database and environment are excluded from Git.

## Testing
```powershell
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
```
Tests use a temporary database and actual GUI callbacks for cross-interface
add/toggle/delete, persistence, validation, and parameterized SQL input.
See `docs/test_results.txt` for recorded results.

## Structure
- `src/backend.py`: shared SQLite storage.
- `src/tkinter_ui.py` and `src/pyqt_ui.py`: interfaces.
- `tests/test_integration.py`: integration tests.
- `docs/Lab 4-Git.docx`: original assignment.
- `docs/lab_report.md`: report and completion status.
- `docs/github_submission.md`: remaining GitHub/Moodle steps.
- `lab4_git_summary.md`: Git study notes.

## Git and submission
The local repository uses main and commits attributed to Titia Saikali with the
Git email already configured on this computer. The solo workflow does not need
partner setup, branches, pull requests, merging, or contribution tracking.
GitHub repository: https://github.com/titiasaikali/Lab4-TitiaSaikali (private).
See `docs/github_submission.md` for submission and reviewer access.
Moodle upload and instructor/TA invitations are still pending.

## References
- Assignment tutorial: https://www.w3schools.com/git/
- VS Code: https://code.visualstudio.com/docs/sourcecontrol/overview
- SQLite: https://docs.python.org/3/library/sqlite3.html
- PyQt: https://www.riverbankcomputing.com/software/pyqt/
