# Golden Exemplar: Narrow Git Rebase Request

## Request

“Teach me Git rebase.”

## Expected response shape

### Assumptions

The request is narrow and does not ask for a full Git curriculum or a study schedule. The target is a safe, practical introduction.

### Outcome summary

Perform an interactive rebase on a local branch, explain what changes, resolve a simple conflict, and know when not to rewrite shared history. Target: **Advanced Beginner — Lower Intermediate** for this bounded workflow.

### Starting point

Use a disposable repository with two local commits and a branch that needs to be rebased. Skip Git basics if the learner can already create branches, inspect history, and recover from a mistaken local commit.

### Learning map

1. Rebase concept and safety boundary [Core]
   1.1 Explain how rebase rewrites commit ancestry
   1.2 Distinguish local history from already-shared history
2. Basic workflow [Core]
   2.1 Create a disposable branch and inspect the commit graph
   2.2 Run `git rebase <base>` and inspect the result
   2.3 Use interactive rebase to reorder or squash local commits
3. Conflict recovery [Required]
   3.1 Recognize a rebase conflict state
   3.2 Resolve one conflict and continue the rebase
   3.3 Abort safely and return to the pre-rebase state
4. Evidence
   4.1 Rebase a bounded local branch, resolve or abort a conflict, and explain why rewriting shared history requires a different workflow

### Stop condition

Do not add remote workflows, advanced reflog recovery, CI integration, or a full Git syllabus unless requested. The learner is ready for this bounded outcome when they can complete it in a disposable repository without copying commands blindly.
