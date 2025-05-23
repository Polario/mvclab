import os
from git import Repo

def get_changed_files(repo_path):
    """Get a list of files changed in the working directory."""
    repo = Repo(repo_path)
    return [item.a_path for item in repo.index.diff(None)]

def get_commit_stats(repo_path):
    """Get statistics for the commit history."""
    repo = Repo(repo_path)
    commits = list(repo.iter_commits())
    return {
        'total_commits': len(commits),
        'authors': set(commit.author.name for commit in commits)
    } 