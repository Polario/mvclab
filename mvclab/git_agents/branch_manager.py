import os
from git import Repo

def create_branch(repo_path, branch_name):
    """Create a new branch in the repository."""
    repo = Repo(repo_path)
    new_branch = repo.create_head(branch_name)
    return new_branch

def list_branches(repo_path):
    """List all branches in the repository."""
    repo = Repo(repo_path)
    return [branch.name for branch in repo.branches]

def delete_branch(repo_path, branch_name):
    """Delete a branch from the repository."""
    repo = Repo(repo_path)
    repo.delete_head(branch_name) 