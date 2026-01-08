# Bash as Glue: Combining Tools & Error Handling - Quiz

## Questions

1. What does `set -e` do?
   - A) Exit on any error
   - B) Enable echo
   - C) Set environment variable
   - D) Exit when empty

2. What does `set -u` do?
   - A) Set uppercase
   - B) Exit on undefined variable usage
   - C) Use UTF-8
   - D) Unbuffered output

3. What does `set -o pipefail` do?
   - A) Pipe fails immediately
   - B) Pipeline returns failure if any command fails
   - C) Fails all pipes
   - D) Outputs pipe errors

4. Which trap signal runs cleanup on normal exit?
   - A) `TERM`
   - B) `INT`
   - C) `EXIT`
   - D) `ERR`

5. What does `mktemp` return?
   - A) Current temp directory
   - B) Path to new temporary file
   - C) Temp file contents
   - D) Process ID

6. How do you auto-export all variables when sourcing a file?
   - A) `export -a`
   - B) `set -a; source .env; set +a`
   - C) `source -e .env`
   - D) `export $(cat .env)`

7. What does `trap 'cleanup' EXIT INT TERM` do?
   - A) Runs cleanup on exit or interrupt signals
   - B) Traps only exit codes
   - C) Exits on interrupt
   - D) Terminates cleanup

8. Which variable contains the line number where an error occurred?
   - A) `$LINE`
   - B) `$LINENO`
   - C) `$ERRNO`
   - D) `$ERROR_LINE`

9. What does `mktemp -d` create?
   - A) Temporary file with -d flag
   - B) Temporary directory
   - C) Temp file in /tmp/d/
   - D) Deletes temp file

10. How do you reference a variable with a default value if unset?
    - A) `$VAR || "default"`
    - B) `${VAR:-default}`
    - C) `$VAR ? default`
    - D) `default($VAR)`

11. What does `set -E` do?
    - A) Extended globbing
    - B) ERR trap inherited by shell functions
    - C) Export all variables
    - D) Echo commands

12. Which is the proper way to quote a variable?
    - A) `$VAR`
    - B) `"$VAR"`
    - C) `'$VAR'`
    - D) `` `$VAR` ``

13. How do you check if a file exists in bash?
    - A) `if [ -f file ]; then`
    - B) `if exists file; then`
    - C) `if file -e; then`
    - D) `if test file; then`

14. What does `trap - SIGNAL` do?
    - A) Ignores signal
    - B) Resets trap to default behavior
    - C) Negates signal
    - D) Subtracts signal

15. Which command gets the directory of the current script?
    - A) `$0`
    - B) `pwd`
    - C) `dirname $0`
    - D) `$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)`

---

## Answer Key

1. **A** - `set -e` exits immediately if any command returns non-zero status
2. **B** - `set -u` treats unset variables as error and exits
3. **B** - `pipefail` makes pipeline return failure if any command in pipe fails (not just last)
4. **C** - `EXIT` trap runs on any exit (normal or error)
5. **B** - `mktemp` creates unique temporary file and returns its path
6. **B** - `set -a` auto-exports all subsequent variable assignments
7. **A** - Trap runs cleanup function on EXIT (normal), INT (Ctrl+C), or TERM (kill)
8. **B** - `$LINENO` expands to current line number in script
9. **B** - `-d` flag creates temporary directory instead of file
10. **B** - `${VAR:-default}` uses default if VAR is unset or empty
11. **B** - `-E` makes ERR trap inherited by functions and subshells
12. **B** - Always quote variables to handle spaces and special characters
13. **A** - `[ -f file ]` tests if file exists and is a regular file
14. **B** - `trap - SIGNAL` removes custom trap, restores default behavior
15. **D** - Gets absolute path of script directory, handling symlinks correctly
