import subprocess
import json
from radon.complexity import cc_visit
from radon.metrics import mi_visit

def run_flake8(file_path):
    result = subprocess.run(
        ["flake8", file_path, "--format=json"],
        capture_output=True,
        text=True
    )
    try:
        return json.loads(result.stdout) if result.stdout else {}
    except json.JSONDecodeError:
        return {"error": "flake8 output could not be parsed"}

def calculate_complexity(code):
    complexity = cc_visit(code)
    return [{"function": c.name, "complexity": c.complexity, "line": c.lineno} for c in complexity]

def calculate_maintainability_index(code):
    return {"maintainability_index": mi_visit(code, multi=True)}

def run_static_analysis(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        code = f.read()

    return {
        "flake8_issues": run_flake8(file_path),
        "complexity": calculate_complexity(code),
        "maintainability": calculate_maintainability_index(code)
    }
