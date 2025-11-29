# Useful Links: Input/Output Streams in Python

## Official Documentation

### Python Standard Library
- [sys — System-specific parameters and functions](https://docs.python.org/3/library/sys.html)
  - `sys.stdin`, `sys.stdout`, `sys.stderr`
  - `sys.argv`, `sys.exit()`
- [argparse — Parser for command-line options](https://docs.python.org/3/library/argparse.html)
  - Creating CLI utilities with arguments
- [subprocess — Subprocess management](https://docs.python.org/3/library/subprocess.html)
  - Creating pipelines in Python
- [io — Core tools for working with streams](https://docs.python.org/3/library/io.html)
  - Working with buffering
- [signal — Set handlers for asynchronous events](https://docs.python.org/3/library/signal.html)
  - Handling SIGINT, SIGTERM

### Working with Data
- [csv — CSV File Reading and Writing](https://docs.python.org/3/library/csv.html)
- [json — JSON encoder and decoder](https://docs.python.org/3/library/json.html)
- [re — Regular expression operations](https://docs.python.org/3/library/re.html)

## Articles and Tutorials

### Unix Philosophy & Python
- [The Art of Unix Programming](http://www.catb.org/~esr/writings/taoup/html/)
  - Classic book on Unix philosophy
- [Command Line Tools in Python](https://realpython.com/command-line-interfaces-python-argparse/)
  - Creating CLI tools with argparse
- [Writing Command Line Tools in Python](https://dbader.org/blog/how-to-make-command-line-commands-with-python)
  - Best practices for CLI utilities

### Streams and I/O
- [Understanding stdin, stdout, and stderr](https://www.howtogeek.com/435903/what-are-stdin-stdout-and-stderr-on-linux/)
  - Standard streams basics
- [Python I/O Performance](https://realpython.com/python-buffering/)
  - Buffering and performance
- [Working with Binary Data in Python](https://realpython.com/python-binary-data/)
  - Binary streams

### Advanced Topics
- [Building Streaming Data Pipelines](https://realpython.com/python-iterators-iterables/)
  - Iterators and generators for streams
- [BrokenPipeError in Python](https://docs.python.org/3/library/signal.html#note-on-sigpipe)
  - Why it occurs and how to handle
- [Python subprocess pipelines](https://stackoverflow.com/questions/13332268/how-to-use-subprocess-command-with-pipes)
  - Creating complex pipelines

## Tools and Libraries

### CLI Frameworks
- [Click](https://click.palletsprojects.com/)
  - Modern framework for CLI applications
  ```bash
  pip install click
  ```
- [Typer](https://typer.tiangolo.com/)
  - CLI with type hints
  ```bash
  pip install typer
  ```
- [Fire](https://github.com/google/python-fire)
  - Automatic CLI generation from Google
  ```bash
  pip install fire
  ```

### Data Processing
- [pandas](https://pandas.pydata.org/)
  - Powerful library for tabular data
  ```bash
  pip install pandas
  ```
- [jq.py](https://github.com/mwilliamson/jq.py)
  - jq for Python
  ```bash
  pip install jq
  ```

### Progress Bars
- [tqdm](https://github.com/tqdm/tqdm)
  - Beautiful progress bars
  ```bash
  pip install tqdm
  ```
  ```python
  from tqdm import tqdm
  import sys
  
  for line in tqdm(sys.stdin):
      process(line)
  ```

### Colorized Output
- [colorama](https://github.com/tartley/colorama)
  - Colored terminal output
  ```bash
  pip install colorama
  ```
- [rich](https://github.com/Textualize/rich)
  - Rich terminal formatting
  ```bash
  pip install rich
  ```

## Example Projects

### Ready-made Python Utilities
- [csvkit](https://csvkit.readthedocs.io/)
  - Suite of utilities for working with CSV
  ```bash
  pip install csvkit
  csvcut -c 1,3 file.csv | csvlook
  ```
- [jq](https://stedolan.github.io/jq/)
  - JSON processor (written in C, but has Python bindings)
- [httpie](https://httpie.io/)
  - HTTP client in Unix style
  ```bash
  pip install httpie
  http GET api.example.com/users | jq .
  ```

### Open Source Examples
- [glances](https://github.com/nicolargo/glances)
  - System monitoring
- [youtube-dl](https://github.com/ytdl-org/youtube-dl)
  - Video downloader
- [pgcli](https://github.com/dbcli/pgcli)
  - PostgreSQL CLI with autocompletion

## Books

### Python
- **"Fluent Python" by Luciano Ramalho**
  - Chapter on iterators and generators
- **"Effective Python" by Brett Slatkin**
  - Best practices for I/O operations
- **"Python Cookbook" by David Beazley**
  - Recipes for working with streams

### Unix/Linux
- **"The Linux Command Line" by William Shotts**
  - Command line basics
- **"Unix Power Tools" by Jerry Peek**
  - Advanced techniques
- **"Classic Shell Scripting" by Arnold Robbins**
  - Shell integration

## Videos and Courses

### Free Courses
- [Python Command Line Tools (YouTube)](https://www.youtube.com/results?search_query=python+command+line+tools)
- [Real Python — CLI Applications](https://realpython.com/courses/python-cli-tools/)

### Conferences
- PyCon talks:
  - "Building Command Line Tools with Python"
  - "Data Pipelines with Python"
  - "Unix Philosophy in Python"

## Practical Resources

### Datasets for Practice
- [Awesome Public Datasets](https://github.com/awesomedata/awesome-public-datasets)
  - CSV, JSON, logs for experiments
- [Sample Web Server Logs](https://github.com/elastic/examples/tree/master/Common%20Data%20Formats/apache_logs)
  - Logs for parsing

### Coding Challenges
- [Command Line Challenge](https://cmdchallenge.com/)
  - Command line puzzles
- [Advent of Code](https://adventofcode.com/)
  - Solve puzzles with Python CLI utilities

### Cheat Sheets
- [Python argparse cheatsheet](https://gist.github.com/nloadholtes/c3a09ce76a63a7e4d2d3)
- [Python subprocess cheatsheet](https://gist.github.com/kirpit/1306188)

## Communities and Forums

- [r/Python](https://www.reddit.com/r/Python/)
  - Python project discussions
- [r/commandline](https://www.reddit.com/r/commandline/)
  - CLI tools and techniques
- [Stack Overflow — Python CLI tag](https://stackoverflow.com/questions/tagged/python+command-line)
  - Questions and answers
- [Python Discord](https://pythondiscord.com/)
  - Active community

## Debugging and Profiling

### Debugging
- [pdb — Python Debugger](https://docs.python.org/3/library/pdb.html)
  ```python
  import pdb; pdb.set_trace()
  ```
- [ipdb](https://github.com/gotcha/ipdb)
  - IPython debugger
  ```bash
  pip install ipdb
  ```

### Profiling
- [cProfile](https://docs.python.org/3/library/profile.html)
  ```bash
  python -m cProfile -s tottime script.py
  ```
- [line_profiler](https://github.com/pyutils/line_profiler)
  - Line-by-line profiling
  ```bash
  pip install line_profiler
  ```

## Testing CLI Applications

- [pytest](https://docs.pytest.org/)
  - Testing framework
  ```bash
  pip install pytest
  ```
- [Click Testing](https://click.palletsprojects.com/en/8.1.x/testing/)
  - Testing Click applications
- [subprocess testing patterns](https://docs.python.org/3/library/subprocess.html#subprocess.run)

## Useful UNIX Commands for Combining

Learn these commands to create powerful pipelines:

- `grep`, `egrep`, `fgrep` — pattern search
- `sed` — stream editor
- `awk` — text processing
- `cut`, `paste` — working with columns
- `sort`, `uniq` — sorting and unique values
- `head`, `tail` — beginning/end of file
- `wc` — count lines/words/characters
- `tr` — character replacement
- `tee` — split stream
- `xargs` — build commands

## Alternatives to Python for CLI

For comparison and inspiration:

- **Bash/Shell** — for simple tasks
- **Perl** — classic choice for text processing
- **Ruby** — elegant syntax
- **Go** — fast compiled utilities
- **Rust** — performance and safety
- **Node.js** — if you know JavaScript

## Conclusion

The best way to learn is to **practice**:

1. Read source code of existing CLI utilities
2. Solve problems on [HackerRank](https://www.hackerrank.com/domains/python) and [LeetCode](https://leetcode.com/)
3. Create your own utilities for everyday tasks
4. Participate in open source projects

**Remember:** Every expert was once a beginner. Write code, experiment, make mistakes, and learn! 🚀
