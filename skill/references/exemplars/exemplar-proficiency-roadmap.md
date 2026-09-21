# Golden Exemplar: Branch-Specific Proficiency Roadmap

## Request

“I know Python at Competent level. Build me a roadmap to become Proficient in databases, using Python for data work.”

## Expected response shape

### Assumptions

Python is an established branch and should not be rebuilt from Novice. Database experience is unknown and requires an entry diagnostic. The roadmap targets **Proficient — Upper Intermediate** database performance, not professional certification or universal expertise.

### Outcome summary

Build, analyze, optimize, and review database-backed systems in ambiguous but bounded situations, using Python where it supports the outcome. Route strategy: **competency**, with project-first evidence at major milestones.

### Starting point

1. Run a short database diagnostic: write a join, explain a transaction boundary, inspect an execution plan, and identify an indexing trade-off.
2. Start at the first unmet database prerequisite; retain Python as a supporting branch and skip demonstrated Python foundations.
3. Use a bounded unfamiliar schema as the first challenge rather than a tutorial-only exercise.

### Proficiency gap and evidence

| Branch or outcome | Current level | Target level | Performance context | Evidence |
|---|---|---|---|---|
| Python for data work | Competent | Competent or supporting | Bounded unfamiliar | Integrate a parameterized query and inspect failures without rebuilding Python basics |
| Relational database fundamentals | Unknown | Proficient | Familiar to ambiguous transition | Explain normalization, constraints, transactions, and query behavior in a new schema |
| Database engineering | Unknown | Proficient | Ambiguous and review-oriented | Design and defend schema, indexing, migration, backup, and performance trade-offs |

### Learning map excerpt

1. Entry diagnostic and database foundations [Required]
   1.1 Write and explain joins, constraints, and transaction boundaries
   1.2 Inspect a query plan and identify one plausible bottleneck
2. Relational modeling and correctness [Core]
   2.1 Design normalized schemas and explain denormalization trade-offs
   2.2 Model constraints, isolation, and failure behavior
3. Query performance and operations [Core]
   3.1 Compare indexing strategies on a bounded unfamiliar workload
   3.2 Plan a safe migration with rollback and compatibility considerations
   3.3 Design backup, restore, and observability checks appropriate to the context
4. Proficient capstone [Milestone]
   4.1 Review an unfamiliar database-backed design, identify risks, propose alternatives, and defend the chosen trade-offs

### Feedback loop

Advance when the learner can transfer the reasoning to a new schema. If the learner can execute commands but cannot explain trade-offs, remediate the smallest conceptual gap rather than adding more tools.
