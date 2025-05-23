"""
Branch management module for Git operations.
"""
from git import Repo
from git.exc import GitCommandError

def create_branch(repo_path, branch_name):
    """
    Create a new branch in the repository.
    
    Args:
        repo_path (str): Path to the Git repository
        branch_name (str): Name of the branch to create
        
    Returns:
        git.Head: The created branch object
    """
    try:
        repo = Repo(repo_path)
        current = repo.active_branch
        
        # Create and checkout new branch
        new_branch = repo.create_head(branch_name)
        new_branch.checkout()
        
        return new_branch
    except GitCommandError as e:
        raise Exception(f"Failed to create branch: {str(e)}")

def delete_branch(repo_path, branch_name):
    """
    Delete a branch from the repository.
    
    Args:
        repo_path (str): Path to the Git repository
        branch_name (str): Name of the branch to delete
    """
    try:
        repo = Repo(repo_path)
        repo.delete_head(branch_name)
    except GitCommandError as e:
        raise Exception(f"Failed to delete branch: {str(e)}")

def list_branches(repo_path):
    """
    List all branches in the repository.
    
    Args:
        repo_path (str): Path to the Git repository
        
    Returns:
        list: List of branch names
    """
    try:
        repo = Repo(repo_path)
        return [branch.name for branch in repo.heads]
    except GitCommandError as e:
        raise Exception(f"Failed to list branches: {str(e)}") 