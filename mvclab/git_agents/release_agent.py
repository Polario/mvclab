import os
from git import Repo

def create_release_branch(repo_path, version):
    """Create a new release branch."""
    repo = Repo(repo_path)
    branch_name = f'release-{version}'
    branch = repo.create_head(branch_name)
    return branch

def prepare_release(repo_path, version):
    """Prepare a release by updating version files."""
    # Example: Update version in a file
    version_file = os.path.join(repo_path, 'version.txt')
    with open(version_file, 'w') as f:
        f.write(version)

def finalize_release(repo_path, version, message):
    """Finalize a release by creating a tag."""
    repo = Repo(repo_path)
    tag_name = f'v{version}'
    tag = repo.create_tag(tag_name, message=message)
    return tag_name

def cleanup_release(repo_path, version):
    """Clean up a release branch."""
    repo = Repo(repo_path)
    branch_name = f'release-{version}'
    repo.delete_head(branch_name) 