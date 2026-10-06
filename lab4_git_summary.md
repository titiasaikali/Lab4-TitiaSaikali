# Git study notes ? Titia Saikali

Git stores local version history; GitHub hosts repositories for remote access.
The working tree holds edits, the index holds staged changes, and a commit
records a staged snapshot. A remote is a named repository URL.

## Commands
```powershell
git init -b main
git status
git add src/backend.py
git commit -m "Add shared backend"
git diff
git diff --staged
git log --oneline --graph --all
git show HEAD
git tag -a v1.0 -m "Final release"
git remote -v
git push -u origin main
git pull origin main
```
Push sends local history to a remote; fetch downloads remote history without
integrating it, while pull fetches and integrates changes. A tag identifies a
release commit. A clone copies a repository and its history.

## Collaboration concepts (not required for this solo submission)
Create an isolated branch with `git switch -c feature-tkinter`, commit changes,
then merge with `git merge feature-tkinter` from main. Conflicting edits require
reviewing conflict markers, choosing the final content, staging, and committing.
A GitHub pull request allows review before merging branches.

## Undo and temporary work
`git restore file` discards unstaged edits; use carefully.
`git restore --staged file` unstages without discarding edits.
`git revert COMMIT` records a new commit undoing an earlier one.
`git stash` saves temporary edits; `git stash pop` restores them.
Avoid rewriting already shared history unnecessarily.

## Good practice
Use descriptive commits, inspect diffs before committing, ignore generated data
and environments, avoid secrets, and test before tagging a release.

Review the assignment tutorial: https://www.w3schools.com/git/
VS Code source control: https://code.visualstudio.com/docs/sourcecontrol/overview
