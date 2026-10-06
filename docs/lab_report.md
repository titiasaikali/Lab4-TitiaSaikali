# Lab 4 report

Name: **Titia Saikali**  
Course: EECE 435L  
Date: October 6, 2026  
Mode: Solo, confirmed by student

## Implementation
A task manager demonstrates one project with Tkinter and PyQt6 frontends.
Both provide add, completion toggle, delete, and refresh operations through
one SQLite backend. Commits to SQLite preserve tasks between runs.
Parameterized SQL handles task titles, and blank titles are rejected.
Separate GUI processes avoid event-loop conflicts while sharing the database.

## Git workflow
Initialize main, stage related files, commit the backend, commit both interfaces,
then commit testing/documentation and tag v1.0. Inspect status and history.
The solo instructions remove partner setup, feature branches, pull requests,
merging, and contribution tracking; these are not simulated or claimed.

## Validation
Actual automated output is recorded in test_results.txt. Tests instantiate both
GUI classes and verify Tkinter add -> PyQt refresh/toggle -> Tkinter refresh/delete,
PyQt add, persistence, blank validation, and parameterized input.
Manual review: launch both GUIs, add in Tkinter, refresh PyQt, toggle there,
refresh Tkinter, close/reopen to verify persistence, then delete.

## Remaining account-dependent work
Publish to GitHub, invite instructor/TAs if private, and submit the actual URL
and README on Moodle. See github_submission.md. External steps are not claimed.
The tutorial reading is for the student: review the linked tutorial and study
notes before presenting this work.

Automated result: all 3 integration tests passed on October 6, 2026.
Python source compilation also passed. GUI tests required access to the installed
Tcl/Tk libraries outside the sandbox; no project code workaround was needed.
