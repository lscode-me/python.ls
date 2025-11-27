# Final Project: Build a Complete ETL Pipeline

## Project Overview
Build a production-ready ETL pipeline that processes a 5GB dataset using Unix command-line tools and Python.

## Requirements

### 1. Data Source
Choose one:
- Public API (e.g., GitHub API, OpenWeather, JSONPlaceholder)
- Large CSV dataset (e.g., Kaggle datasets)
- Web scraping (with permission)
- Simulated data generation

### 2. Pipeline Components

#### Extract
- Fetch data from API or file
- Handle pagination if applicable
- Store raw data in JSONL or CSV format
- Include error handling and retries

#### Transform
- Clean data (remove nulls, duplicates)
- Filter relevant records
- Enrich data (join with lookup tables)
- Convert formats (JSON → CSV, etc.)
- Aggregate statistics

#### Load
- Generate markdown report
- Create CSV summary files
- Optionally: Load to database (SQLite)

### 3. Technical Requirements

Must include:
- [ ] At least 3 distinct processing stages
- [ ] Parallel processing (GNU parallel or xargs -P)
- [ ] Error handling (set -euo pipefail, trap)
- [ ] Progress monitoring (pv)
- [ ] Temporary file management (mktemp)
- [ ] Checkpoints for resumability
- [ ] Makefile for orchestration
- [ ] Logging to file
- [ ] Configuration via .env
- [ ] Performance profiling (time command)

Must use at least 5 of these tools:
- grep, sed, awk
- jq, mlr, csvkit
- sort, uniq, cut, paste
- curl, wget
- gzip, zcat
- Python (for complex logic)

### 4. Performance Goals
- Process 5GB of data
- Complete in under 30 minutes
- Use < 2GB RAM
- Utilize multiple CPU cores

### 5. Documentation

Create README.md with:
- Project overview
- Data source description
- Pipeline architecture diagram
- Installation instructions
- Usage examples
- Performance benchmarks
- Known limitations

## Example Project Ideas

### Idea 1: GitHub Repository Analytics
- Fetch commits from popular repos
- Analyze commit patterns
- Generate contributor statistics
- Create markdown report with top contributors, commit trends

### Idea 2: Weather Data Analysis
- Fetch historical weather data
- Process temperature trends
- Aggregate by location/month
- Generate climate report

### Idea 3: Log Analytics Dashboard
- Process application logs (5GB)
- Extract error patterns
- Calculate response time percentiles
- Generate performance report

### Idea 4: E-commerce Sales Pipeline
- Load order data (CSV)
- Calculate revenue by product/category
- Find top customers
- Generate sales report with visualizations (ASCII charts)

## Evaluation Criteria

### Functionality (40%)
- Pipeline executes successfully
- Produces correct output
- Handles edge cases

### Performance (20%)
- Efficient use of parallelism
- Streaming vs loading
- Memory usage

### Code Quality (20%)
- Error handling
- Logging
- Code organization
- Comments

### Documentation (20%)
- Clear README
- Usage examples
- Performance analysis

## Deliverables

1. **Source Code**
   - All scripts (.sh, .py, etc.)
   - Makefile
   - .env.example

2. **Documentation**
   - README.md
   - ARCHITECTURE.md (pipeline design)

3. **Sample Output**
   - Generated reports
   - Log files
   - Performance metrics

4. **Presentation** (optional)
   - 5-minute demo video
   - OR
   - Written walkthrough

## Example Pipeline Structure

```
project/
├── Makefile
├── README.md
├── .env.example
├── bin/
│   ├── extract.sh
│   ├── transform.sh
│   └── load.sh
├── lib/
│   ├── python_filter.py
│   └── enrichment.py
├── data/
│   └── .gitkeep
├── output/
│   └── .gitkeep
└── logs/
    └── .gitkeep
```

## Getting Started

1. **Choose a dataset**: Find 5GB+ data source
2. **Design pipeline**: Sketch 3-5 stages
3. **Build incrementally**: Start with 100MB sample
4. **Add features**: Parallelism, checkpoints, etc.
5. **Optimize**: Profile and improve performance
6. **Document**: Write README and comments

## Tips

- **Start small**: Test on 100MB before 5GB
- **Checkpoint frequently**: Don't lose progress
- **Profile early**: Identify bottlenecks
- **Use existing data**: Kaggle, data.gov
- **Ask for help**: Use course resources

## Submission

Submit via:
- GitHub repository (public or private)
- ZIP file with all code and docs

Include:
- Link to data source (if public)
- Instructions to run pipeline
- Expected runtime and resource usage

## Timeline

- **Week 1**: Choose project, design pipeline
- **Week 2**: Implement core functionality
- **Week 3**: Add parallelism and optimization
- **Week 4**: Documentation and testing

Good luck! 🚀
