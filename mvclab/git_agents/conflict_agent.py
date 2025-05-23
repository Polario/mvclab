import os
from git import Repo

def get_conflict_files(repo_path):
    """Get a list of files with merge conflicts."""
    repo = Repo(repo_path)
    conflicts = repo.index.unmerged_blobs()
    return list(conflicts.keys())

def resolve_conflict(repo_path, file_path):
    """Resolve a conflict in a file."""
    # Example: Resolve by choosing the first version
    repo = Repo(repo_path)
    repo.git.checkout('--ours', file_path)
    repo.index.add([file_path])

def abort_merge(repo_path):
    """Abort an ongoing merge."""
    repo = Repo(repo_path)
    repo.git.merge('--abort')

def continue_merge(repo_path):
    """Continue an ongoing merge."""
    repo = Repo(repo_path)
    repo.git.merge('--continue') 