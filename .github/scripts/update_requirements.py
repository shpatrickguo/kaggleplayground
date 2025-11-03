#!/usr/bin/env python3
"""
Script to automatically update requirements.txt based on imports in Jupyter notebooks.
Scans all subdirectories for .ipynb files and extracts Python imports.
"""

import json
import os
import re
import sys
from pathlib import Path
from typing import Set


# Mapping of import names to PyPI package names
PACKAGE_MAPPING = {
    'sklearn': 'scikit-learn',
    'cv2': 'opencv-python',
    'PIL': 'Pillow',
    'yaml': 'PyYAML',
    'dateutil': 'python-dateutil',
    'bs4': 'beautifulsoup4',
    'imblearn': 'imbalanced-learn',
    'pandas_profiling': 'ydata-profiling',
}

# Standard library modules that should not be in requirements.txt
STDLIB_MODULES = {
    'abc', 'argparse', 'array', 'ast', 'asyncio', 'atexit', 'base64', 'bisect',
    'builtins', 'bz2', 'calendar', 'cmath', 'cmd', 'code', 'codecs', 'collections',
    'colorsys', 'configparser', 'contextlib', 'copy', 'copyreg', 'csv', 'ctypes',
    'dataclasses', 'datetime', 'decimal', 'difflib', 'dis', 'distutils', 'email',
    'encodings', 'enum', 'errno', 'fcntl', 'filecmp', 'fileinput', 'fnmatch',
    'fractions', 'functools', 'gc', 'getopt', 'getpass', 'gettext', 'glob', 'grp',
    'gzip', 'hashlib', 'heapq', 'hmac', 'html', 'http', 'importlib', 'inspect',
    'io', 'ipaddress', 'itertools', 'json', 'keyword', 'linecache', 'locale',
    'logging', 'lzma', 'mailbox', 'marshal', 'math', 'mimetypes', 'mmap', 'modulefinder',
    'multiprocessing', 'numbers', 'operator', 'os', 'pathlib', 'pdb', 'pickle',
    'pickletools', 'pipes', 'pkgutil', 'platform', 'plistlib', 'posix', 'pprint',
    'profile', 'pstats', 'pty', 'pwd', 'py_compile', 'pyclbr', 'pydoc', 'queue',
    'quopri', 'random', 're', 'readline', 'reprlib', 'resource', 'rlcompleter',
    'runpy', 'sched', 'secrets', 'select', 'selectors', 'shelve', 'shlex', 'shutil',
    'signal', 'site', 'smtpd', 'smtplib', 'socket', 'socketserver', 'sqlite3',
    'ssl', 'stat', 'statistics', 'string', 'struct', 'subprocess', 'sys', 'sysconfig',
    'syslog', 'tabnanny', 'tarfile', 'tempfile', 'termios', 'test', 'textwrap',
    'threading', 'time', 'timeit', 'token', 'tokenize', 'trace', 'traceback',
    'tracemalloc', 'tty', 'turtle', 'types', 'typing', 'unicodedata', 'unittest',
    'urllib', 'uu', 'uuid', 'venv', 'warnings', 'wave', 'weakref', 'webbrowser',
    'wsgiref', 'xml', 'xmlrpc', 'zipapp', 'zipfile', 'zipimport', 'zlib',
}


def extract_imports_from_notebook(notebook_path: Path) -> Set[str]:
    """Extract all import statements from a Jupyter notebook."""
    imports = set()
    
    try:
        with open(notebook_path, 'r', encoding='utf-8') as f:
            notebook = json.load(f)
        
        for cell in notebook.get('cells', []):
            if cell.get('cell_type') == 'code':
                source = ''.join(cell.get('source', []))
                
                # Extract import statements
                for line in source.split('\n'):
                    line = line.strip()
                    
                    # Match "import package" or "import package as alias"
                    match = re.match(r'^import\s+([a-zA-Z0-9_]+)', line)
                    if match:
                        imports.add(match.group(1))
                    
                    # Match "from package import ..." or "from package.submodule import ..."
                    match = re.match(r'^from\s+([a-zA-Z0-9_]+)', line)
                    if match:
                        imports.add(match.group(1))
    
    except Exception as e:
        print(f"Warning: Could not process {notebook_path}: {e}", file=sys.stderr)
    
    return imports


def get_package_name(import_name: str) -> str:
    """Convert import name to PyPI package name."""
    # Check if there's a known mapping
    if import_name in PACKAGE_MAPPING:
        return PACKAGE_MAPPING[import_name]
    
    # Filter out standard library modules
    if import_name in STDLIB_MODULES:
        return None
    
    # Return the import name as-is for most packages
    return import_name


def find_all_notebooks(root_dir: Path) -> list:
    """Find all Jupyter notebooks in subdirectories."""
    notebooks = []
    
    for path in root_dir.rglob('*.ipynb'):
        # Skip notebooks in hidden directories or checkpoints
        if any(part.startswith('.') for part in path.parts):
            continue
        notebooks.append(path)
    
    return notebooks


def main():
    """Main function to update requirements.txt."""
    repo_root = Path(__file__).parent.parent.parent
    
    print(f"Scanning for notebooks in {repo_root}...")
    
    # Find all notebooks
    notebooks = find_all_notebooks(repo_root)
    print(f"Found {len(notebooks)} notebook(s)")
    
    # Extract all imports
    all_imports = set()
    for notebook in notebooks:
        print(f"Processing {notebook.relative_to(repo_root)}...")
        imports = extract_imports_from_notebook(notebook)
        all_imports.update(imports)
    
    # Convert to package names
    packages = set()
    for import_name in all_imports:
        package_name = get_package_name(import_name)
        if package_name:
            packages.add(package_name)
    
    # Sort packages alphabetically
    sorted_packages = sorted(packages)
    
    print(f"\nFound {len(sorted_packages)} unique package(s):")
    for pkg in sorted_packages:
        print(f"  - {pkg}")
    
    # Write to requirements.txt
    requirements_path = repo_root / 'requirements.txt'
    with open(requirements_path, 'w') as f:
        for package in sorted_packages:
            f.write(f"{package}\n")
    
    print(f"\nUpdated {requirements_path}")
    
    # Check if there were any changes
    if os.system('git diff --quiet requirements.txt') != 0:
        print("\nChanges detected in requirements.txt")
        return 0
    else:
        print("\nNo changes to requirements.txt")
        return 0


if __name__ == '__main__':
    sys.exit(main())
