"""
Code review module for Git operations.
"""
from git import Repo
from git.exc import GitCommandError
from datetime import datetime, timedelta

def get_changed_files(repo_path, branch='HEAD', since=None):
    """
    Get list of files changed in the specified branch.
    
    Args:
        repo_path (str): Path to the Git repository
        branch (str): Branch name or reference
        since (datetime, optional): Only show changes since this date
        
    Returns:
        list: List of changed files
    """
    try:
        repo = Repo(repo_path)
        commit = repo.commit(branch)
        
        if since:
            commits = list(repo.iter_commits(branch, since=since))
        else:
            commits = [commit]
            
        changed_files = set()
        for commit in commits:
            changed_files.update(commit.stats.files.keys())
            
        return list(changed_files)
    except GitCommandError as e:
        raise Exception(f"Failed to get changed files: {str(e)}")

def get_file_diff(repo_path, file_path, branch='HEAD'):
    """
    Get the diff for a specific file.
    
    Args:
        repo_path (str): Path to the Git repository
        file_path (str): Path to the file
        branch (str): Branch name or reference
        
    Returns:
        str: The diff output
    """
    try:
        repo = Repo(repo_path)
        return repo.git.diff(branch, '--', file_path)
    except GitCommandError as e:
        raise Exception(f"Failed to get file diff: {str(e)}")

def get_commit_stats(repo_path, branch='HEAD', since=None):
    """
    Get statistics about commits in the specified branch.
    
    Args:
        repo_path (str): Path to the Git repository
        branch (str): Branch name or reference
        since (datetime, optional): Only show stats since this date
        
    Returns:
        dict: Statistics about the commits
    """
    try:
        repo = Repo(repo_path)
        commits = list(repo.iter_commits(branch, since=since))
        
        stats = {
            'total_commits': len(commits),
            'total_changes': sum(len(commit.stats.files) for commit in commits),
            'authors': {},
            'files_changed': set()
        }
        
        for commit in commits:
            author = commit.author.name
            stats['authors'][author] = stats['authors'].get(author, 0) + 1
            stats['files_changed'].update(commit.stats.files.keys())
            
        stats['files_changed'] = len(stats['files_changed'])
        return stats
    except GitCommandError as e:
        raise Exception(f"Failed to get commit stats: {str(e)}") 