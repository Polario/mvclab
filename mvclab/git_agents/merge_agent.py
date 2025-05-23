import os
from git import Repo

def merge_branch(repo_path, source_branch, target_branch):
    """Merge a source branch into a target branch."""
    repo = Repo(repo_path)
    repo.git.checkout(target_branch)
    merge_result = repo.git.merge(source_branch)
    return merge_result

def get_merge_conflicts(repo_path):
    """Get a list of files with merge conflicts."""
    repo = Repo(repo_path)
    conflicts = repo.index.unmerged_blobs()
    return list(conflicts.keys()) 