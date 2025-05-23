import os
from git import Repo

def push_changes(repo_path):
    """Push changes to the remote repository."""
    repo = Repo(repo_path)
    repo.git.push()

def pull_changes(repo_path):
    """Pull changes from the remote repository."""
    repo = Repo(repo_path)
    repo.git.pull()

def fetch_all(repo_path):
    """Fetch all changes from the remote repository."""
    repo = Repo(repo_path)
    repo.git.fetch('--all') 