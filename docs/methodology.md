# Methodology

## Objective
Retrieve passages from a supplied corpus, verify source membership and return structured evidence with an execution trace.

## Algorithm
Token overlap retrieval → rank sources → audit passage against original text → assemble findings and trace.

## Interface
run(question, corpus, limit=3)

Inputs: A question, mapping of source IDs to passages, positive retrieval limit.

Outputs: Question, source-tagged findings, stage trace and evidence-found/insufficient-evidence status.

## Evaluation protocol
Evaluate retrieval recall, source consistency and abstention against human-labeled research queries.

Report test corpus provenance, exact revision, configuration, failures and uncertainty. The included regression tests are not a benchmark.

## Threats to validity
This is a deterministic orchestration baseline, not a live literature search or autonomous LLM-agent system. Source consistency does not establish truth.
