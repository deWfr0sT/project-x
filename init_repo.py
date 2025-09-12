import os

# Folder structure
folders = [
    "data/raw",
    "data/processed",
    "notebooks",
    "src/ingestion",
    "src/processing",
    "src/correlation",
    "src/models",
    "src/api/routes",
    "src/dashboard",
    "tests",
    "scripts"
]

files = {
    "README.md": "# Stock News Impact Quant\n\nProject to analyze impact of news on stock prices.",
    "requirements.txt": "pandas\nnumpy\nrequests\nsqlalchemy\npsycopg2-binary\ntransformers\ntorch\nscikit-learn\nfastapi\nuvicorn\nstreamlit\nbeautifulsoup4\nnsepython\nnsepy\n",
    ".gitignore": "venv/\n__pycache__/\n*.pyc\n*.pyo\n*.pyd\n*.db\n*.sqlite3\n.env\n*.csv\n*.json\n*.log\n",
    "config.yaml": "database:\n  type: postgres\n  host: localhost\n  port: 5432\n  user: user\n  password: pass\n  name: stocks\n\napi_keys:\n  dhan: YOUR_DHANHQ_KEY\n  openai: YOUR_OPENAI_KEY\n"
}

def create_structure():
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
    for filename, content in files.items():
        with open(filename, "w") as f:
            f.write(content)
    print("✅ Repo structure created!")

if __name__ == "__main__":
    create_structure()
