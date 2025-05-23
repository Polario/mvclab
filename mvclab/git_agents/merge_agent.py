"""
Merge management module for Git operations.
"""
from git import Repo
from git.exc import GitCommandError

def merge_branch(repo_path, source_branch, target_branch='HEAD'):
    """
    Merge a source branch into the target branch.
    
    Args:
        repo_path (str): Path to the Git repository
        source_branch (str): Name of the branch to merge from
        target_branch (str): Name of the branch to merge into
        
    Returns:
        git.Commit: The merge commit object if successful
    """
    try:
        repo = Repo(repo_path)
        current = repo.active_branch
        
        # Checkout target branch
        repo.heads[target_branch].checkout()
        
        # Perform merge
        merge_result = repo.git.merge(source_branch)
        
        return repo.head.commit
    except GitCommandError as e:
        raise Exception(f"Failed to merge branch: {str(e)}")
    finally:
        # Restore original branch
        current.checkout()

def abort_merge(repo_path):
    """
    Abort a merge in progress.
    
    Args:
        repo_path (str): Path to the Git repository
    """
    try:
        repo = Repo(repo_path)
        repo.git.merge('--abort')
    except GitCommandError as e:
        raise Exception(f"Failed to abort merge: {str(e)}")

def get_merge_conflicts(repo_path):
    """
    Get list of files with merge conflicts.
    
    Args:
        repo_path (str): Path to the Git repository
        
    Returns:
        list: List of files with conflicts
    """
    try:
        repo = Repo(repo_path)
        return repo.index.unmerged_blobs.keys()
    except GitCommandError as e:
        raise Exception(f"Failed to get merge conflicts: {str(e)}") 