from setuptools import setup, find_packages

def read_requirements(filename):
    with open(filename) as f:
        return [line.strip() for line in f if line.strip() and not line.startswith('#')]

setup(
    name="demo-csv-linter",
    version="0.0.1",
    description="demo python CLI tool to lint csv files",
    packages=find_packages(),
    install_requires=read_requirements('requirements.txt'),
    entry_points={
        "console_scripts": [
            "csv-linter=csv_linter.main:main"
        ]
    },
    python_requires=">=3.8",
)
