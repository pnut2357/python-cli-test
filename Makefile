.PHONY: version-patch version-minor version-major

version-patch:
	python scripts/update_version.py

version-minor:
	python scripts/update_version.py --minor $$(python -c "import re; print(re.search(r'version=\"(\d+)\.(\d+)\.\d+\"', open('setup.py').read()).group(2))")

version-major:
	python scripts/update_version.py --major $$(python -c "import re; print(re.search(r'version=\"(\d+)\.\d+\.\d+\"', open('setup.py').read()).group(1))") 