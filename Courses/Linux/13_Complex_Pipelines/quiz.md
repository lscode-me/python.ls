# Complex Pipelines: Map/Reduce, Staging, Checkpoints, Orchestration - Quiz

Test your knowledge of complex pipeline orchestration with Make, checkpoints, and staging.

---

## Question 1: Split-Map-Reduce Order

What is the correct order of phases in a split-map-reduce pipeline?

A) Map → Split → Reduce
B) Split → Map → Reduce
C) Reduce → Map → Split
D) Split → Reduce → Map

---

## Question 2: Makefile Dependencies

In a Makefile, what does the syntax `target: dependency` mean?

A) `target` must be created before `dependency`
B) `target` depends on `dependency`; if `dependency` is newer, rebuild `target`
C) `target` and `dependency` are aliases
D) `dependency` is optional for building `target`

---

## Question 3: Parallel Make

How do you run 4 Make targets in parallel?

A) `make -p 4`
B) `make -j 4`
C) `make --parallel 4`
D) Both B and `make --jobs=4`

---

## Question 4: Checkpoint Purpose

What is the purpose of checkpoint files in a pipeline?

A) To track performance metrics
B) To enable resuming after failure without redoing completed work
C) To log errors
D) To create backups

---

## Question 5: Temporary Directory

Which command creates a temporary directory that is automatically cleaned up?

A) `tmpdir=$(mktemp -d)`
B) `mkdir /tmp/mydir`
C) `TMPDIR=/tmp/work`
D) `mktemp --directory --cleanup`

---

## Question 6: PHONY Targets

In a Makefile, what does `.PHONY: clean` declare?

A) `clean` is a temporary target
B) `clean` is not a real file target, always run its commands
C) `clean` should be run in parallel
D) `clean` depends on all other targets

---

## Question 7: Checkpoint Implementation

How do you implement a checkpoint in bash?

A) `if [ ! -f .checkpoint ]; then do_work; touch .checkpoint; fi`
B) `checkpoint do_work`
C) `save_state && do_work`
D) `do_work | tee .checkpoint`

---

## Question 8: Staging Definition

What is staging in a data pipeline?

A) Running pipeline in production
B) Using intermediate storage areas between processing stages
C) Deploying code changes
D) Testing the pipeline

---

## Question 9: Make Timestamp Checking

Which Make syntax checks if target is older than any dependency?

A) Make automatically compares timestamps of target vs dependencies
B) `$(if $(older))`
C) `[[ target -ot dependency ]]`
D) `make --check-timestamps`

---

## Question 10: Make Variables

How do you pass the first dependency to a Make recipe?

A) `$<`
B) `$@`
C) `$^`
D) `$*`

---

## Question 11: mktemp Benefits

What is the benefit of using `mktemp -d` over `mkdir /tmp/mydir`?

A) Faster execution
B) Creates unique directory name, avoiding conflicts
C) Automatically sets permissions
D) Works on more operating systems

---

## Question 12: Idempotency

In a pipeline, what does "idempotent" mean?

A) Pipeline runs in parallel
B) Running pipeline multiple times produces same result
C) Pipeline has checkpoints
D) Pipeline handles errors gracefully

---

## Question 13: Make Target Rebuild

How do you make a Make target run only if output doesn't exist?

A) Use `.PHONY`
B) Define target with no dependencies: `target:`
C) Targets automatically work this way (run if target missing or dependencies newer)
D) Add `[ -f target ] && exit 0` to recipe

---

## Question 14: Output Versioning

What is the purpose of versioning pipeline outputs?

A) To track code versions
B) To enable reproducing results from specific pipeline runs
C) To compress files
D) To improve performance

---

## Question 15: Exponential Backoff

Which pattern implements exponential backoff retry?

A) `sleep 2` in a loop
B) `delay=$((delay * 2))` after each failed attempt
C) `retry_count=$((retry_count + 1))`
D) `sleep $RANDOM`

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | Split divides data into chunks, Map processes each chunk in parallel, Reduce aggregates results |
| 2 | B | Make compares timestamps: if dependency is newer than target (or target doesn't exist), rebuild target |
| 3 | D | Both `make -j 4` and `make --jobs=4` work for parallel execution |
| 4 | B | Checkpoints mark stages as complete. On restart, skip completed stages |
| 5 | A | Creates unique temporary directory. Combine with trap for automatic cleanup |
| 6 | B | `.PHONY` tells Make that target is not a file, so always execute its recipe |
| 7 | A | Check if checkpoint file exists. If not, do work and create checkpoint |
| 8 | B | Staging stores intermediate results, allowing inspection and debugging between stages |
| 9 | A | Make's built-in behavior: if any dependency is newer than target, rebuild target |
| 10 | A | `$<` is first prerequisite, `$@` is target, `$^` is all prerequisites |
| 11 | B | `mktemp -d` generates unique name, preventing conflicts from concurrent runs |
| 12 | B | Idempotent pipelines can be safely rerun. Important for reliability and checkpointing |
| 13 | C | Make rebuilds if target doesn't exist OR any dependency is newer |
| 14 | B | Versioning outputs creates historical record, enabling comparison and reproducibility |
| 15 | B | Exponential backoff: wait 1s, 2s, 4s, 8s, etc. Prevents overwhelming failed services |

