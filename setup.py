from setuptools import setup, find_packages

setup(
    name="demo-csv-linter",
    version="0.0.1",
    description="demo python CLI tool to lint csv files",
    packages=find_packages(),
    install_requires=[
        "click==7.1.2",
        "numpy==1.24.3",
        "pandas==1.5.3"
    ],
    entry_points={
        "console_scripts": [
            "csv-linter=csv_linter.main:main"
        ]
    },
    python_requires=">=3.8",
)
