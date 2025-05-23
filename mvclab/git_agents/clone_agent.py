import os
from git import Repo

def clone_repository(repo_url, target_path):
    """Clone a repository to the target path."""
    return Repo.clone_from(repo_url, target_path)

def clone_with_submodules(repo_url, target_path):
    """Clone a repository and initialize its submodules."""
    repo = Repo.clone_from(repo_url, target_path)
    repo.submodule_update(recursive=True)
    return repo 