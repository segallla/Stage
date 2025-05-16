# Stage

This repository contains a simple Battery Energy Storage System (BESS) analysis
pipeline. The pipeline evaluates California sites using a series of steps
(`STEP1` through `STEP8`) and returns structured results.

## Usage

```python
from bess.pipeline import analyze_address

result = analyze_address("44933 Fern Ave, Lancaster, CA 93534")
result2 = analyze_address("5300 Sheila St, Commerce, CA 90040")
```

## Running Tests

Run the unit tests with Python's built-in `unittest` module:

```bash
python -m unittest -v
```

