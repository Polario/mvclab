"""
MVC Lab - A framework for initializing web projects with MVC structure.
"""

__version__ = "0.1.0"
__author__ = "Martin Akerman"

from .cli import cli
from .git_agents import init_repo, branch_manager, commit_agent, merge_agent, review_agent

__all__ = [
    'cli',
    'init_repo',
    'branch_manager',
    'commit_agent',
    'merge_agent',
    'review_agent'
] 