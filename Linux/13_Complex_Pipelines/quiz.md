# Quiz: Complex Pipelines

## Questions

1. **What is the correct order of phases in a split-map-reduce pipeline?**
   - A) Map → Split → Reduce
   - B) Split → Map → Reduce
   - C) Reduce → Map → Split
   - D) Split → Reduce → Map

2. **In a Makefile, what does the syntax `target: dependency` mean?**
   - A) `target` must be created before `dependency`
   - B) `target` depends on `dependency`; if `dependency` is newer, rebuild `target`
   - C) `target` and `dependency` are aliases
   - D) `dependency` is optional for building `target`

3. **How do you run 4 Make targets in parallel?**
   - A) `make -p 4`
   - B) `make -j 4`
   - C) `make --parallel 4`
   - D) `make --jobs=4` (both B and D are equivalent)

4. **What is the purpose of checkpoint files in a pipeline?**
   - A) To track performance metrics
   - B) To enable resuming after failure without redoing completed work
   - C) To log errors
   - D) To create backups

5. **Which command creates a temporary directory that is automatically cleaned up?**
   - A) `tmpdir=$(mktemp -d)`
   - B) `mkdir /tmp/mydir`
   - C) `TMPDIR=/tmp/work`
   - D) `mktemp --directory --cleanup`

6. **In a Makefile, what does `.PHONY: clean` declare?**
   - A) `clean` is a temporary target
   - B) `clean` is not a real file target, always run its commands
   - C) `clean` should be run in parallel
   - D) `clean` depends on all other targets

7. **How do you implement a checkpoint in bash?**
   - A) `if [ ! -f .checkpoint ]; then do_work; touch .checkpoint; fi`
   - B) `checkpoint do_work`
   - C) `save_state && do_work`
   - D) `do_work | tee .checkpoint`

8. **What is staging in a data pipeline?**
   - A) Running pipeline in production
   - B) Using intermediate storage areas between processing stages
   - C) Deploying code changes
   - D) Testing the pipeline

9. **Which Make syntax checks if target is older than any dependency?**
   - A) Make automatically compares timestamps of target vs dependencies
   - B) `$(if $(older))`
   - C) `[[ target -ot dependency ]]`
   - D) `make --check-timestamps`

10. **How do you pass the first dependency to a Make recipe?**
    - A) `$<`
    - B) `$@`
    - C) `$^`
    - D) `$*`

11. **What is the benefit of using `mktemp -d` over `mkdir /tmp/mydir`?**
    - A) Faster execution
    - B) Creates unique directory name, avoiding conflicts
    - C) Automatically sets permissions
    - D) Works on more operating systems

12. **In a pipeline, what does "idempotent" mean?**
    - A) Pipeline runs in parallel
    - B) Running pipeline multiple times produces same result
    - C) Pipeline has checkpoints
    - D) Pipeline handles errors gracefully

13. **How do you make a Make target run only if output doesn't exist?**
    - A) Use `.PHONY`
    - B) Define target with no dependencies: `target:`
    - C) Targets automatically work this way (run if target missing or dependencies newer)
    - D) Add `[ -f target ] && exit 0` to recipe

14. **What is the purpose of versioning pipeline outputs?**
    - A) To track code versions
    - B) To enable reproducing results from specific pipeline runs
    - C) To compress files
    - D) To improve performance

15. **Which pattern implements exponential backoff retry?**
    - A) `sleep 2` in a loop
    - B) `delay=$((delay * 2))` after each failed attempt
    - C) `retry_count=$((retry_count + 1))`
    - D) `sleep $RANDOM`

---

## Answer Key

1. **B** - Split → Map → Reduce  
   *Split divides data into chunks, Map processes each chunk in parallel, Reduce aggregates results.*

2. **B** - `target` depends on `dependency`; if `dependency` is newer, rebuild `target`  
   *Make compares timestamps: if dependency is newer than target (or target doesn't exist), Make rebuilds target.*

3. **D** - Both `make -j 4` and `make --jobs=4` work  
   *`-j N` enables parallel execution with N concurrent jobs.*

4. **B** - To enable resuming after failure without redoing completed work  
   *Checkpoints mark stages as complete (e.g., `touch .checkpoint`). On restart, skip completed stages.*

5. **A** - `tmpdir=$(mktemp -d)`  
   *Creates unique temporary directory. Combine with `trap 'rm -rf "$tmpdir"' EXIT` for automatic cleanup.*

6. **B** - `clean` is not a real file target, always run its commands  
   *`.PHONY` tells Make that `clean` is not a file, so always execute its recipe even if a file named "clean" exists.*

7. **A** - `if [ ! -f .checkpoint ]; then do_work; touch .checkpoint; fi`  
   *Check if checkpoint file exists. If not, do work and create checkpoint. On rerun, work is skipped.*

8. **B** - Using intermediate storage areas between processing stages  
   *Staging stores intermediate results (e.g., in `stage1/`, `stage2/`), allowing inspection and debugging between stages.*

9. **A** - Make automatically compares timestamps of target vs dependencies  
   *Make's built-in behavior: if any dependency is newer than target, or target doesn't exist, rebuild target.*

10. **A** - `$<`  
    *`$<` is first prerequisite, `$@` is target, `$^` is all prerequisites, `$*` is stem in pattern rules.*

11. **B** - Creates unique directory name, avoiding conflicts  
    *`mktemp -d` generates unique name (e.g., `/tmp/tmp.XyZ123`), preventing conflicts from concurrent runs.*

12. **B** - Running pipeline multiple times produces same result  
    *Idempotent pipelines can be safely rerun. Important for reliability and checkpointing.*

13. **C** - Targets automatically work this way  
    *Make rebuilds target if: (1) target doesn't exist, OR (2) any dependency is newer than target.*

14. **B** - To enable reproducing results from specific pipeline runs  
    *Versioning outputs (e.g., `output_20240315_143022/`) creates historical record, enabling comparison and reproducibility.*

15. **B** - `delay=$((delay * 2))` after each failed attempt  
    *Exponential backoff: wait 1s, 2s, 4s, 8s, etc. Prevents overwhelming failed services. Linear: `delay=$((delay + 1))`.*

