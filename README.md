# Agentic-Research-Assistant

### Auditable research workflow

![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white) ![Tests](https://github.com/rohanst14/Agentic-Research-Assistant/actions/workflows/tests.yml/badge.svg) ![Stage](https://img.shields.io/badge/stage-research%20prototype-64748b)

Retrieve passages from a supplied corpus, verify source membership and return structured evidence with an execution trace.

## Design

Token overlap retrieval → rank sources → audit passage against original text → assemble findings and trace.

## Quick start

```bash
git clone https://github.com/rohanst14/Agentic-Research-Assistant.git
cd Agentic-Research-Assistant
python -m venv .venv
# Activate .venv for your operating system.
python -m pip install -e .
python examples/demo.py
python -m unittest discover -s tests -v
```

## Usage

```python
from agentic_research_assistant import run
result = run('reactor pressure', {'paper': 'reactor pressure changes with temperature'})
print(result)
```

## API contract

| Field | Description |
|---|---|
| Entry point | `run(question, corpus, limit=3)` |
| Inputs | A question, mapping of source IDs to passages, positive retrieval limit. |
| Outputs | Question, source-tagged findings, stage trace and evidence-found/insufficient-evidence status. |

## Repository map

| Path | Role |
|---|---|
| [src/agentic_research_assistant/](src/agentic_research_assistant/) | Python implementation |
| [examples/demo.py](examples/demo.py) | Reproducible synthetic demo |
| [tests/test_core.py](tests/test_core.py) | Regression checks |
| [docs/methodology.md](docs/methodology.md) | Evaluation design and limitations |
| [ROADMAP.md](ROADMAP.md) | Milestones and planned work |
| [CI workflow](.github/workflows/tests.yml) | Automated tests and demo |

## Evaluation and limitations

Evaluate retrieval recall, source consistency and abstention against human-labeled research queries.

This is a deterministic orchestration baseline, not a live literature search or autonomous LLM-agent system. Source consistency does not establish truth. The current demonstration is synthetic; no real-world performance claims are made.

## Project status

AI-assisted research prototype. See [roadmap](ROADMAP.md) for planned extensions.
