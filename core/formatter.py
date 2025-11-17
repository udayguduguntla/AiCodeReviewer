import subprocess

def format_code_with_black(file_path):
    subprocess.run(["black", file_path])
    return "Code formatted with Black (PEP8 compliance)."
