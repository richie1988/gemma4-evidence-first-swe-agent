# Richard Sikaonga — Gemma 4 Developer Agent Competition Entry

Developer: Richard Sikaonga

This directory contains a conservative baseline submission for the Google - The Gemma 4 Developer Agent Competition.

## Submission contents

- `agent.yaml` — root Agent Config
- `prompts/system.md` — autonomous software-engineering workflow prompt

The submission intentionally uses the required Gemma 4 base model without LoRA adapters for the first baseline. This keeps the package small and minimizes configuration risk while testing the prompt-and-tool strategy first.

## Strategy

The agent follows an evidence-first SWE workflow:

1. translate the issue into acceptance criteria;
2. inspect repository structure;
3. use semantic/code-graph tools to localize likely symbols;
4. reproduce the bug or establish a focused baseline;
5. make the smallest compatible fix;
6. run focused and broader relevant tests;
7. inspect the Git diff and submit the patch.

## Before uploading

1. Accept the competition rules in Kaggle.
2. Upload `submission.zip` directly as the competition submission.
3. Do not nest `submission.zip` inside another directory: `agent.yaml` is already at the archive root.
4. Run the provided validation script locally if you modify the package.

## Notes

This baseline does not include a LoRA adapter. A later experimental branch can add a trained PEFT adapter after establishing the baseline score and validating the competition's exact adapter loading behavior.
