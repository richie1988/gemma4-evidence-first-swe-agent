# Graph-Guided Evidence-First Software Repair with Gemma 4

**Developer:** Richard Sikaonga  
**Competition:** Google - The Gemma 4 Developer Agent Competition

This repository contains an autonomous software-engineering agent built around Gemma 4 for repository-level issue diagnosis, code repair, validation, and patch submission.

The project investigates whether a structured **evidence-first workflow** combined with **semantic code retrieval and repository graph reasoning** can improve the reliability of autonomous software repair under a constrained execution budget.

## Project Objective

Autonomous coding agents must do more than generate code. To resolve real repository issues reliably, an agent must:

- understand the reported problem;
- identify the correct implementation area;
- trace dependencies and affected symbols;
- establish a likely root cause;
- make a compatible change;
- validate the change against relevant tests;
- review the resulting patch;
- and avoid unrelated modifications.

This project approaches software repair as an evidence-gathering and localization problem before treating it as a code-generation problem.

## Core Approach

The main agent follows an eight-stage workflow:

1. **Understand** — translate the issue into concrete acceptance criteria.
2. **Inspect** — determine repository structure, language, build system, and likely implementation areas.
3. **Localize** — use semantic search, exact repository search, and code-graph relationships to identify relevant symbols.
4. **Reproduce** — establish a focused failure signal where practical.
5. **Hypothesize** — identify a probable root cause before editing.
6. **Modify** — apply the smallest behaviorally complete change.
7. **Validate** — run focused tests first, followed by broader relevant checks.
8. **Review and Submit** — inspect the final Git diff and submit only a coherent patch.

The central design principle is:

> **Localize first. Understand dependencies. Edit minimally. Validate incrementally.**

## Gemma 4 Model

The project uses the competition-supported base model:

```text
gemma-4-31b-it-qat-w4a16-ct
```

The current implementation does not depend on a LoRA adapter. This provides a clean baseline for measuring the contribution of prompting, tool use, repository reasoning, and agent workflow before introducing model adaptation.

## Three-Agent Experimental Framework

The repository contains three configurations for controlled comparison.

### 1. Baseline Agent

A lightweight software-engineering agent with standard repository inspection, editing, testing, and patch-submission capabilities.

```text
agents/baseline/
```

### 2. Evidence-First Agent

Adds a structured workflow requiring issue analysis, repository inspection, root-cause hypothesis formation, minimal editing, incremental testing, and final diff review.

```text
agents/evidence_first/
```

### 3. Graph-Guided Evidence-First Agent

Extends the evidence-first workflow with:

- semantic code retrieval;
- code-neighbor exploration;
- repository dependency analysis;
- induced code-subgraph inspection.

```text
agents/graph_guided/
```

The objective of this ablation study is to distinguish improvements caused by workflow discipline from improvements associated specifically with graph-guided localization.

## Repository Structure

```text
gemma4-evidence-first-swe-agent/
│
├── agent.yaml
├── submission.zip
├── validate_submission.py
│
├── prompts/
│   └── system.md
│
├── agents/
│   ├── baseline/
│   │   ├── agent.yaml
│   │   └── system.md
│   │
│   ├── evidence_first/
│   │   ├── agent.yaml
│   │   └── system.md
│   │
│   └── graph_guided/
│       ├── agent.yaml
│       └── system.md
│
├── docs/
│   ├── architecture.md
│   ├── methodology.md
│   └── evaluation.md
│
├── experiments/
│   ├── experiment_matrix.md
│   ├── README.md
│   └── results/
│       └── results.csv
│
├── paper/
│   └── README.md
│
└── images/
```

## Competition Submission

The competition-ready archive is:

```text
submission.zip
```

Its root contains:

```text
submission.zip
├── agent.yaml
└── prompts/
    └── system.md
```

The root agent is the graph-guided evidence-first implementation.

## Agent Tools

The main agent can use the competition harness tools for:

### Repository Interaction

- `read_file`
- `edit_file`
- `write_file`
- `run_command`

### Graph and Semantic Analysis

- `search_similar_code`
- `get_code_neighbors`
- `get_code_subgraph`

### Execution and Submission

- `get_status`
- `submit_patch`

The graph tools are used selectively rather than as a replacement for conventional repository search.

Semantic retrieval helps answer:

> **Where might the relevant implementation be?**

Graph analysis helps answer:

> **What depends on this implementation?**

## Minimal-Patch Strategy

The agent is instructed to avoid:

- unrelated refactoring;
- unnecessary dependencies;
- formatting churn;
- speculative features;
- disabled tests;
- weakened validation;
- hidden exceptions;
- unconditional success paths;
- modifications unrelated to the issue.

The objective is the **smallest repository-consistent patch that completely resolves the required behavior**.

## Validation Strategy

Validation proceeds incrementally:

```text
Issue
  ↓
Repository Investigation
  ↓
Failure Reproduction
  ↓
Root-Cause Hypothesis
  ↓
Minimal Patch
  ↓
Focused Test
  ↓
Relevant Regression Tests
  ↓
Git Diff Review
  ↓
Patch Submission
```

Before submission, the agent is instructed to inspect commands such as:

```bash
git status --short
git diff --check
git diff --stat
git diff HEAD
```

## Experimental Evaluation

The planned comparison is:

| Variant | Structured Workflow | Semantic Search | Code Neighbors | Code Subgraph |
|---|---:|---:|---:|---:|
| Baseline | No | No | No | No |
| Evidence First | Yes | No | No | No |
| Graph Guided | Yes | Yes | Yes | Yes |

The primary metric is repository issue resolution:

```text
PASS / FAIL
```

Additional measurements may include:

- execution time;
- tool calls;
- files inspected;
- files modified;
- patch size;
- tests executed;
- graph queries;
- edit iterations.

Only results obtained from actual evaluation runs are reported. No synthetic benchmark scores are included.

## Validate the Submission

Run:

```bash
python3 validate_submission.py submission.zip
```

A valid package should report:

```text
Submission structure validation passed.
```

## Research Direction

The project focuses on four questions:

1. Does explicit evidence gathering improve software repair reliability?
2. Does graph-guided localization improve fault identification?
3. Can minimal-patch discipline reduce regressions?
4. Can budget-aware repository exploration preserve enough execution time for meaningful validation?

Future experiments may evaluate PEFT/LoRA adaptation separately from the prompt-and-tool baseline.

## Developer

**Richard Sikaonga**

GitHub: [richie1988](https://github.com/richie1988)

Project Repository:  
[github.com/richie1988/gemma4-evidence-first-swe-agent](https://github.com/richie1988/gemma4-evidence-first-swe-agent)

## Status

- Competition agent configured
- Submission archive generated
- Submission structure validated
- Three-agent ablation framework implemented
- Research documentation structure created
- Experiment result tracking prepared
- Benchmark evaluation ongoing

## License

Add the appropriate open-source license before distributing or reusing the project outside the competition.
