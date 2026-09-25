from pathlib import Path
import zipfile, sys, re

zip_path = Path(sys.argv[1] if len(sys.argv) > 1 else "submission.zip")
required_model = "gemma-4-31b-it-qat-w4a16-ct"

if not zip_path.exists():
    raise SystemExit(f"Missing: {zip_path}")

with zipfile.ZipFile(zip_path) as zf:
    names = set(zf.namelist())
    assert "agent.yaml" in names, "agent.yaml must be at ZIP root"
    assert "prompts/system.md" in names, "Missing prompts/system.md"
    assert not any(name.startswith("/") or ".." in Path(name).parts for name in names), "Unsafe path in ZIP"
    agent = zf.read("agent.yaml").decode("utf-8")
    system = zf.read("prompts/system.md").decode("utf-8")

assert required_model in agent, "Required Gemma 4 model missing"
assert "instruction: !include prompts/system.md" in agent, "Prompt include missing"
assert "name: submit_patch" in agent, "submit_patch tool missing"

combined = (agent + "\n" + system).lower()
for banned in ("chatgpt", "openai"):
    assert banned not in combined, f"Unexpected branding string found: {banned}"

print("Submission structure validation passed.")
