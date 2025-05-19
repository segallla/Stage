# Stage

This repository contains a simple Battery Energy Storage System (BESS) analysis
pipeline. The pipeline evaluates California sites using a series of steps
(`STEP1` through `STEP8`) and returns structured results.

## Usage

```python
from bess.pipeline import analyze_address, analyze_addresses

result = analyze_address("44933 Fern Ave, Lancaster, CA 93534")
```

## Running Tests

Run the unit tests with Python's built-in `unittest` module:

```bash
python -m unittest -v
```


## Web Front End

A minimal web interface is provided in `webapp/app.py`. Run it with Python to start a local server (default port `8000`):

```bash
python webapp/app.py
```

Open your browser at `http://localhost:8000` to enter an address and view the analysis results in JSON format.
