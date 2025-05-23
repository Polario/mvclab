import os
from git import Repo

def create_tag(repo_path, tag_name, message):
    """Create a new tag in the repository."""
    repo = Repo(repo_path)
    tag = repo.create_tag(tag_name, message=message)
    return tag

def delete_tag(repo_path, tag_name):
    """Delete a tag from the repository."""
    repo = Repo(repo_path)
    repo.delete_tag(tag_name)

def list_tags(repo_path):
    """List all tags in the repository."""
    repo = Repo(repo_path)
    return [tag.name for tag in repo.tags]

def push_tag(repo_path, tag_name):
    """Push a tag to the remote repository."""
    repo = Repo(repo_path)
    repo.git.push('origin', tag_name) 