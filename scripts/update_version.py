import re
import sys
import subprocess
from pathlib import Path

def get_current_version():
    setup_file = Path("setup.py")
    with open(setup_file) as f:
        content = f.read()
        match = re.search(r'version="(\d+\.\d+\.\d+)"', content)
        if match:
            return match.group(1)
    return None

def run_git_command(command, check=True):
    try:
        result = subprocess.run(command, shell=True, check=check, capture_output=True, text=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error executing git command: {e}")
        if check:
            sys.exit(1)
        return None

def has_changes():
    status = run_git_command("git status --porcelain", check=False)
    return bool(status.strip())

def create_git_tag(version):
    tag_name = f"{version}"
    
    # Check if tag already exists
    existing_tags = run_git_command("git tag", check=False)
    if existing_tags and tag_name in existing_tags.split('\n'):
        print(f"Tag {tag_name} already exists")
        return
    
    # Stage the setup.py file
    run_git_command("git add setup.py", check=False)
    
    # Check if there are changes to commit
    if not has_changes():
        print("No changes to commit")
        return
    
    # Create commit
    commit_result = run_git_command(f'git commit -m "Bump version to {version}"', check=False)
    if not commit_result:
        print("Failed to create commit")
        return
    
    # Create and push tag
    run_git_command(f"git tag -a {tag_name} -m 'Version {version}'", check=False)
    run_git_command(f"git push origin {tag_name}", check=False)
    run_git_command("git push origin HEAD", check=False)
    print(f"Created and pushed tag {tag_name}")

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
    
    # Create git tag
    create_git_tag(new_version)
    
    return new_version

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Update package version")
    parser.add_argument("--major", type=int, help="Set major version")
    parser.add_argument("--minor", type=int, help="Set minor version")
    args = parser.parse_args()
    
    update_version(args.major, args.minor) 