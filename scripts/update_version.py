import re
import sys
from pathlib import Path

def get_current_version():
    setup_file = Path("setup.py")
    with open(setup_file) as f:
        content = f.read()
        match = re.search(r'version="(\d+\.\d+\.\d+)"', content)
        if match:
            return match.group(1)
    return None

def update_version(major=None, minor=None):
    current_version = get_current_version()
    if not current_version:
        print("Could not find version in setup.py")
        sys.exit(1)
    
    major_ver, minor_ver, patch_ver = map(int, current_version.split('.'))
    
    # Update only if explicitly provided, otherwise keep current
    if major is not None:
        major_ver = major
    if minor is not None:
        minor_ver = minor
    
    # Always increment patch version
    patch_ver += 1
    
    new_version = f"{major_ver}.{minor_ver}.{patch_ver}"
    
    # Update setup.py
    setup_file = Path("setup.py")
    with open(setup_file) as f:
        content = f.read()
    
    new_content = re.sub(
        r'version="\d+\.\d+\.\d+"',
        f'version="{new_version}"',
        content
    )
    
    with open(setup_file, 'w') as f:
        f.write(new_content)
    
    print(f"Updated version to {new_version}")
    return new_version

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Update package version")
    parser.add_argument("--major", type=int, help="Set major version")
    parser.add_argument("--minor", type=int, help="Set minor version")
    args = parser.parse_args()
    
    update_version(args.major, args.minor) 