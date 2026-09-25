# Experimental Matrix

## Developer

Richard Sikaonga

## Model

gemma-4-31b-it-qat-w4a16-ct

## Variants

| Variant | Structured Workflow | Semantic Search | Code Neighbors | Code Subgraph |
|---|---:|---:|---:|---:|
| Baseline | No | No | No | No |
| Evidence First | Yes | No | No | No |
| Graph Guided | Yes | Yes | Yes | Yes |

## Primary Metric

Repository issue resolution:

PASS / FAIL

## Secondary Measurements

For each run record:

- execution time
- PASS or FAIL
- tool calls
- files inspected
- files modified
- lines added
- lines removed
- tests executed
- graph queries
- patch notes

## Reporting Rule

Only actual measured results are recorded.

No estimated or synthetic benchmark scores are reported.
