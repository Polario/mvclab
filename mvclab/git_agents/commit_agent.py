import os
from git import Repo

def create_commit(repo_path, message):
    """Create a commit with the current changes."""
    repo = Repo(repo_path)
    repo.index.add('*')
    commit = repo.index.commit(message)
    return commit

def get_commit_history(repo_path):
    """Get the commit history of the repository."""
    repo = Repo(repo_path)
    return list(repo.iter_commits())

def amend_commit(repo_path, message):
    """Amend the last commit with a new message."""
    repo = Repo(repo_path)
    repo.index.add('*')
    repo.index.commit(message, amend=True) 