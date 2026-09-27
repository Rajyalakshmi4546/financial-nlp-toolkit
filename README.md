# Financial NLP Toolkit

Financial NLP Toolkit is a Python library that simplifies working with financial text data. It offers utilities for tokenization, entity extraction, sentiment analysis, and building end‑to‑end pipelines that can be integrated into larger applications.

## Repository

[https://github.com/Rajyalakshmi4546/financial-nlp-toolkit](https://github.com/Rajyalakshmi4546/financial-nlp-toolkit)

## Key Components

- **src/** – Core source code implementing the NLP utilities.
- **build.py** – Helper script for building the distribution package.
- **examples/** – Ready‑to‑run examples demonstrating typical workflows.
- **docs/** – Documentation source files.
- **playground/** – Interactive notebooks and scripts for experimentation.
- **tests/** – Test suite powered by `pytest`.
- **setup.cfg**, **setup.py**, **pyproject.toml** – Packaging configuration.
- **Pipfile**, **Pipfile.lock** – Development environment specifications.

## Installation

The package can be installed from PyPI or directly from the source repository.

```bash
# From PyPI
pip install financial-nlp-toolkit

# From source
git clone https://github.com/Rajyalakshmi4546/financial-nlp-toolkit.git
cd financial-nlp-toolkit
pip install -e .
```

> Python 3.6 or newer is required.

## Quick Start

```python
from financial_nlp_toolkit import pipeline

# Create a pipeline for financial text
fin_pipe = pipeline()

text = "Apple reported a 10% increase in revenue for Q4 2023."
result = fin_pipe.process(text)

print(result)
```

The example above shows how to instantiate a default pipeline and process a piece of financial news. Refer to the `examples/` directory for more detailed use‑cases.

## Development & Testing

```bash
# Run the test suite
pytest

# Build the package
python build.py
```

## Contributing

Contributions are welcome. Please see `CONTRIBUTING.md` for guidelines on how to propose changes, report bugs, or suggest enhancements.

## License

The project is released under the MIT License. The original `LICENSE` file is included unchanged.

---

Developed by Rajyalakshmi Nelakurthi.
