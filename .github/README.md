# GitHub Workflows

## Update Requirements

This workflow automatically updates the `requirements.txt` file based on Python imports found in Jupyter notebooks across the repository.

### Triggers

The workflow runs on:
- **Push to main**: When notebooks (`.ipynb` files) are modified
- **Pull requests**: When notebooks are modified
- **Schedule**: Weekly on Mondays at 00:00 UTC
- **Manual**: Can be triggered manually via workflow dispatch

### How it works

1. Scans all subdirectories for Jupyter notebooks (`.ipynb` files)
2. Extracts Python import statements from code cells
3. Maps import names to PyPI package names (e.g., `sklearn` → `scikit-learn`)
4. Generates an updated `requirements.txt` file with all unique packages
5. Creates a pull request if changes are detected

### Script

The main logic is in `.github/scripts/update_requirements.py`, which:
- Recursively finds all notebooks
- Parses notebook JSON to extract imports
- Filters out standard library modules
- Handles common package name mappings
- Outputs a sorted list of dependencies
