# CSV Linter CLI

A Python command-line tool for linting CSV files. This tool helps identify common issues in CSV files such as empty columns, unnamed columns, and carriage returns.

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Installation

```bash
# Create and activate a virtual environment (recommended)
python3.10 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install the package
pip install -e .
```

## Usage

The CSV linter can be used to check CSV files for common issues:

```bash
# Basic usage
csv-linter path/to/your/file.csv

# Show the data while checking
csv-linter --show-data path/to/your/file.csv
```

### Checks Performed

1. **Empty Columns**: Identifies columns that have no items
2. **Unnamed Columns**: Detects columns with "Unnamed" in their headers
3. **Carriage Returns**: Finds fields containing carriage returns (`\r\n`)

## Development

### Project Structure
```
csv-linter/
├── csv_linter/
│   ├── __init__.py
│   └── main.py
├── scripts/
│   └── update_version.py
├── tests/
│   └── test_main.py
├── setup.py
├── requirements.txt
└── Makefile
```

### Version Management

The project includes a version management system that automatically handles version updates and git tagging.

#### Available Commands

```bash
# Increment patch version (0.0.1 -> 0.0.2)
make version-patch

# Update minor version (0.0.1 -> 0.1.0)
make version-minor

# Update major version (0.0.1 -> 1.0.0)
make version-major
```

Each command will:
1. Update the version in setup.py
2. Create a git commit
3. Create and push a git tag
4. Push changes to the remote repository

### GitHub Actions

The project uses two GitHub Actions workflows:

#### 1. Python Package (python-package.yml)
- **Trigger**: Pull requests to main branch
- **Purpose**: Runs tests and linting
- **How to trigger**: Create a pull request against the main branch

#### 2. Python Publish (python-publish.yml)
- **Trigger**: When a new release is published
- **Purpose**: Builds and publishes the package to PyPI
- **How to trigger**:
  1. Update version using version management commands
  2. Go to GitHub repository
  3. Click "Releases" in the right sidebar
  4. Click "Create a new release"
  5. Set the tag version (e.g., v0.0.1)
  6. Add release notes
  7. Click "Publish release"

### Required Secrets

For the publish workflow to work, you need to set up:
1. `PYPI_API_TOKEN`: Your PyPI API token (starts with `pypi-`)
   - Get it from: https://pypi.org/manage/account/token/
   - Add it to: Repository Settings → Secrets and variables → Actions

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests: `pytest`
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

