# Python in Pipelines: Hybrid Shell-Python Workflows - Resources

## Core Python Documentation

### Standard Library - Essential Modules
- [sys module](https://docs.python.org/3/library/sys.html) - System-specific parameters and functions
- [subprocess module](https://docs.python.org/3/library/subprocess.html) - Subprocess management and shell interaction
- [fileinput module](https://docs.python.org/3/library/fileinput.html) - Iterate over lines from multiple input streams
- [argparse module](https://docs.python.org/3/library/argparse.html) - Command-line argument parsing
- [logging module](https://docs.python.org/3/library/logging.html) - Flexible event logging system
- [pathlib module](https://docs.python.org/3/library/pathlib.html) - Object-oriented filesystem paths
- [shutil module](https://docs.python.org/3/library/shutil.html) - High-level file operations
- [tempfile module](https://docs.python.org/3/library/tempfile.html) - Temporary file and directory creation
- [concurrent.futures](https://docs.python.org/3/library/concurrent.futures.html) - High-level asynchronous execution
- [multiprocessing](https://docs.python.org/3/library/multiprocessing.html) - Process-based parallelism

### File and Data Processing
- [csv module](https://docs.python.org/3/library/csv.html) - CSV file reading and writing
- [json module](https://docs.python.org/3/library/json.html) - JSON encoder and decoder
- [pickle module](https://docs.python.org/3/library/pickle.html) - Python object serialization
- [gzip module](https://docs.python.org/3/library/gzip.html) - Support for gzip compression
- [zipfile module](https://docs.python.org/3/library/zipfile.html) - Work with ZIP archives
- [tarfile module](https://docs.python.org/3/library/tarfile.html) - Read and write tar archive files

## Essential Third-Party Libraries

### Data Processing Powerhouses
- [pandas](https://pandas.pydata.org/docs/) - Data manipulation and analysis library
- [NumPy](https://numpy.org/doc/) - Numerical computing with Python
- [Dask](https://docs.dask.org/) - Parallel computing library
- [Polars](https://pola-rs.github.io/polars-book/) - Fast DataFrame library
- [Vaex](https://vaex.io/) - Out-of-core DataFrames for big data

### JSON and Streaming Data
- [ijson](https://github.com/ijson/ijson) - Streaming JSON parser
- [jsonlines](https://jsonlines.readthedocs.io/) - Handle JSON Lines format
- [orjson](https://github.com/ijl/orjson) - Fast JSON library
- [ujson](https://github.com/ultrajson/ultrajson) - Ultra fast JSON encoder/decoder

### Command Line and Shell Integration
- [click](https://click.palletsprojects.com/) - Python package for creating command line interfaces
- [typer](https://typer.tiangolo.com/) - Modern CLI framework based on Python type hints
- [sh](https://sh.readthedocs.io/) - Python subprocess replacement
- [plumbum](https://plumbum.readthedocs.io/) - Shell combinators library
- [fabric](https://www.fabfile.org/) - High level SSH command execution

### Workflow and Pipeline Frameworks
- [Luigi](https://luigi.readthedocs.io/) - Build complex pipelines of batch jobs
- [Airflow](https://airflow.apache.org/docs/) - Workflow management platform
- [Prefect](https://docs.prefect.io/) - Modern workflow management system
- [Snakemake](https://snakemake.readthedocs.io/) - Workflow management system
- [Nextflow](https://www.nextflow.io/docs/) - Data-driven computational pipelines

## Performance and Optimization

### Profiling and Benchmarking
- [cProfile](https://docs.python.org/3/library/profile.html) - Built-in Python profiler
- [line_profiler](https://github.com/pyutils/line_profiler) - Line-by-line profiling
- [memory_profiler](https://github.com/pythonprofilers/memory_profiler) - Memory usage monitoring
- [py-spy](https://github.com/benfred/py-spy) - Sampling profiler for Python
- [scalene](https://github.com/plasma-umass/scalene) - High-performance CPU, GPU and memory profiler

### Parallel and Async Processing
- [asyncio](https://docs.python.org/3/library/asyncio.html) - Asynchronous I/O, event loop, coroutines
- [aiofiles](https://github.com/Tinche/aiofiles) - Asynchronous file operations
- [joblib](https://joblib.readthedocs.io/) - Lightweight pipelining in Python
- [ray](https://docs.ray.io/) - Distributed computing framework
- [celery](https://docs.celeryproject.org/) - Distributed task queue

## Data Formats and Serialization

### Binary and Efficient Formats
- [Apache Arrow](https://arrow.apache.org/docs/python/) - In-memory columnar format
- [Apache Parquet](https://parquet.apache.org/docs/) - Columnar storage format
- [Apache Avro](https://avro.apache.org/docs/current/gettingstartedpython.html) - Data serialization system
- [Protocol Buffers](https://developers.google.com/protocol-buffers/docs/pythontutorial) - Google's data interchange format
- [MessagePack](https://msgpack.org/) - Efficient binary serialization format

### Configuration and Markup
- [PyYAML](https://pyyaml.org/wiki/PyYAMLDocumentation) - YAML parser and emitter
- [toml](https://github.com/uiri/toml) - TOML parser
- [configparser](https://docs.python.org/3/library/configparser.html) - Configuration file parser
- [lxml](https://lxml.de/) - XML and HTML processing
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - HTML/XML parsing

## System Integration and Monitoring

### System Monitoring
- [psutil](https://psutil.readthedocs.io/) - System and process monitoring
- [resource](https://docs.python.org/3/library/resource.html) - Resource usage information
- [time](https://docs.python.org/3/library/time.html) - Time-related functions
- [datetime](https://docs.python.org/3/library/datetime.html) - Date and time handling

### Logging and Debugging
- [structlog](https://www.structlog.org/) - Structured logging
- [loguru](https://github.com/Delgan/loguru) - Modern logging library
- [rich](https://rich.readthedocs.io/) - Rich text and beautiful formatting
- [tqdm](https://tqdm.github.io/) - Fast, extensible progress bar

## Tutorials and Learning Resources

### Python Command Line Tools
- [RealPython: Python subprocess](https://realpython.com/python-subprocess/) - Complete guide to subprocess
- [RealPython: Command Line Interfaces](https://realpython.com/command-line-interfaces-python-argparse/) - Building CLI apps
- [Python Module of the Week: subprocess](https://pymotw.com/3/subprocess/) - Detailed subprocess examples
- [Automate the Boring Stuff](https://automateboringstuff.com/) - Practical Python automation

### Data Pipeline Design
- [Data Engineering Cookbook](https://github.com/andkret/Cookbook) - Open-source data engineering guide
- [Effective Python](https://effectivepython.com/) - Best practices for Python
- [Architecture Patterns with Python](https://www.cosmicpython.com/) - Software design patterns

### Unix/Linux Integration
- [The Art of Command Line](https://github.com/jlevy/the-art-of-command-line) - Command line mastery
- [Advanced Bash-Scripting Guide](https://tldp.org/LDP/abs/html/) - Comprehensive bash reference
- [Unix Power Tools](http://shop.oreilly.com/product/9780596003302.do) - Classic Unix reference

## Testing and Quality Assurance

### Testing Frameworks
- [pytest](https://docs.pytest.org/) - Testing framework
- [unittest](https://docs.python.org/3/library/unittest.html) - Built-in testing framework
- [hypothesis](https://hypothesis.readthedocs.io/) - Property-based testing
- [pytest-benchmark](https://pytest-benchmark.readthedocs.io/) - Performance testing

### Code Quality Tools
- [black](https://black.readthedocs.io/) - Code formatter
- [flake8](https://flake8.pycqa.org/) - Style guide enforcement
- [mypy](https://mypy.readthedocs.io/) - Static type checker
- [bandit](https://bandit.readthedocs.io/) - Security linter
- [pylint](https://pylint.pycqa.org/) - Code analysis tool

## Cloud and Container Integration

### Cloud Platforms
- [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) - AWS SDK for Python
- [google-cloud](https://googleapis.dev/python/google-cloud-core/latest/) - Google Cloud Client Libraries
- [azure-sdk-for-python](https://github.com/Azure/azure-sdk-for-python) - Azure SDK for Python

### Container Technologies
- [Docker SDK for Python](https://docker-py.readthedocs.io/) - Docker API client
- [Kubernetes Python Client](https://github.com/kubernetes-client/python) - Kubernetes API client

## Books and Deep Learning

### Essential Reading
- "Fluent Python" by Luciano Ramalho - Advanced Python techniques
- "Python Tricks" by Dan Bader - Python best practices
- "High Performance Python" by Micha Gorelick - Optimization techniques
- "Architecture Patterns with Python" by Harry Percival - Design patterns
- "Data Pipelines with Apache Airflow" by Bas Harenslak - Workflow orchestration

### Online Courses
- [Python for Data Engineering (Coursera)](https://www.coursera.org/specializations/python-data-engineering)
- [Command Line Tools for Genomic Data Science](https://www.coursera.org/learn/genomic-tools)
- [Python Automation and Testing (edX)](https://www.edx.org/learn/python/python-automation-testing)

## Community and Support

### Forums and Communities
- [Python.org Community](https://www.python.org/community/) - Official Python community
- [r/Python](https://www.reddit.com/r/Python/) - Python subreddit
- [Python Discord](https://discord.gg/python) - Real-time Python community
- [Stack Overflow Python](https://stackoverflow.com/questions/tagged/python) - Q&A platform

### Package Management
- [PyPI](https://pypi.org/) - Python Package Index
- [conda-forge](https://conda-forge.org/) - Community-driven conda packages
- [Poetry](https://python-poetry.org/) - Dependency management
- [pipx](https://pypa.github.io/pipx/) - Install and run Python applications
