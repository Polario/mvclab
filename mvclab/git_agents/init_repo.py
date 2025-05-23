"""
Git repository initialization module.
"""
import os
from git import Repo

def init_repository(project_path):
    """
    Initialize a new Git repository at the specified project path.
    
    Args:
        project_path (str): Path where the repository should be initialized
        
    Returns:
        git.Repo: The initialized Git repository object
    """
    try:
        repo = Repo.init(project_path)
        
        # Create initial commit
        repo.index.add('*')
        repo.index.commit("Initial commit")
        
        return repo
    except Exception as e:
        raise Exception(f"Failed to initialize Git repository: {str(e)}") 