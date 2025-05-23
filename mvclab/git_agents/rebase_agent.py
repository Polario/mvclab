import os
from git import Repo

def rebase_branch(repo_path, base_branch, target_branch):
    """Rebase a target branch onto a base branch."""
    repo = Repo(repo_path)
    repo.git.checkout(target_branch)
    repo.git.rebase(base_branch)

def abort_rebase(repo_path):
    """Abort an ongoing rebase."""
    repo = Repo(repo_path)
    repo.git.rebase('--abort')

def continue_rebase(repo_path):
    """Continue an ongoing rebase."""
    repo = Repo(repo_path)
    repo.git.rebase('--continue') 