import os
from git import Repo

def get_commit_stats(repo_path, since=None):
    """Get statistics for the commit history."""
    repo = Repo(repo_path)
    commits = list(repo.iter_commits(since=since))
    return {
        'total_commits': len(commits),
        'authors': set(commit.author.name for commit in commits)
    }

def get_commit_history(repo_path):
    """Get the commit history of the repository."""
    repo = Repo(repo_path)
    return list(repo.iter_commits())

def get_contributor_stats(repo_path, since=None):
    """Get statistics for contributors."""
    repo = Repo(repo_path)
    commits = list(repo.iter_commits(since=since))
    contributors = {}
    for commit in commits:
        author = commit.author.name
        if author in contributors:
            contributors[author] += 1
        else:
            contributors[author] = 1
    return contributors 