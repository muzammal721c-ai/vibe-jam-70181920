#!/usr/bin/env python3
"""
Submission ZIP Generator for CodeQuest 2026 Vibe Jam
Packages project excluding .env, git history, cache, virtualenvs, etc.
"""

import os
import zipfile

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_ZIP = os.path.join(BASE_DIR, "vibejam-AskSE-submission.zip")

EXCLUDE_DIRS = {
    ".git",
    "__pycache__",
    "venv",
    "env",
    ".venv",
    "node_modules",
    "build",
    "dist",
    ".idea",
    ".vscode"
}

EXCLUDE_FILES = {
    ".env",
    "vibejam-AskSE-submission.zip",
    "askse.db"
}

def export():
    print(f"Packaging submission ZIP: {OUTPUT_ZIP}...")
    file_count = 0
    with zipfile.ZipFile(OUTPUT_ZIP, "w", zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(BASE_DIR):
            # Modify dirs in-place to avoid excluded folders
            dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]

            for file in files:
                if file in EXCLUDE_FILES or file.endswith(".pyc"):
                    continue

                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, BASE_DIR)
                zipf.write(full_path, rel_path)
                file_count += 1
                print(f"  + {rel_path}")

    print(f"\nSuccessfully generated {OUTPUT_ZIP} with {file_count} files!")
    print("Verification: .env is excluded. Compliant with Section 1 submission rules.")

if __name__ == "__main__":
    export()
