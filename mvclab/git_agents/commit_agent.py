"""
Commit management module for Git operations.
"""
from git import Repo
from git.exc import GitCommandError
from datetime import datetime

def create_commit(repo_path, message, files=None):
    """
    Create a commit with the specified files and message.
    
    Args:
        repo_path (str): Path to the Git repository
        message (str): Commit message
        files (list, optional): List of files to commit. If None, all changes are committed.
        
    Returns:
        git.Commit: The created commit object
    """
    try:
        repo = Repo(repo_path)
        index = repo.index
        
        if files:
            index.add(files)
        else:
            index.add('*')
            
        return index.commit(message)
    except GitCommandError as e:
        raise Exception(f"Failed to create commit: {str(e)}")

def amend_commit(repo_path, message=None):
    """
    Amend the last commit with new changes or message.
    
    Args:
        repo_path (str): Path to the Git repository
        message (str, optional): New commit message. If None, keeps the old message.
    """
    try:
        repo = Repo(repo_path)
        repo.git.commit('--amend', '-m', message if message else '--no-edit')
    except GitCommandError as e:
        raise Exception(f"Failed to amend commit: {str(e)}")

def get_commit_history(repo_path, branch='HEAD', limit=10):
    """
    Get the commit history for a branch.
    
    Args:
        repo_path (str): Path to the Git repository
        branch (str): Branch name or reference
        limit (int): Maximum number of commits to return
        
    Returns:
        list: List of commit objects
    """
    try:
        repo = Repo(repo_path)
        commits = list(repo.iter_commits(branch, max_count=limit))
        return commits
    except GitCommandError as e:
        raise Exception(f"Failed to get commit history: {str(e)}") 