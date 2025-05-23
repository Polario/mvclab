"""
Git agent modules for MVC Lab.
"""

from mvclab.git_agents.branch_manager import create_branch, list_branches, delete_branch
from mvclab.git_agents.commit_agent import create_commit, get_commit_history, amend_commit
from mvclab.git_agents.merge_agent import merge_branch, get_merge_conflicts
from mvclab.git_agents.review_agent import get_changed_files, get_commit_stats as review_commit_stats
from mvclab.git_agents.clone_agent import clone_repository, clone_with_submodules
from mvclab.git_agents.push_pull_agent import push_changes, pull_changes, fetch_all
from mvclab.git_agents.rebase_agent import rebase_branch, abort_rebase, continue_rebase
from mvclab.git_agents.tag_agent import create_tag, delete_tag, list_tags, push_tag
from mvclab.git_agents.release_agent import (
    create_release_branch, prepare_release, finalize_release, cleanup_release
)
from mvclab.git_agents.conflict_agent import (
    get_conflict_files, resolve_conflict, abort_merge, continue_merge
)
from mvclab.git_agents.history_agent import (
    get_commit_stats, get_commit_history as hist_commit_history, get_contributor_stats
)

__all__ = [
    'create_branch', 'list_branches', 'delete_branch',
    'create_commit', 'get_commit_history', 'amend_commit',
    'merge_branch', 'get_merge_conflicts',
    'get_changed_files', 'review_commit_stats',
    'clone_repository', 'clone_with_submodules',
    'push_changes', 'pull_changes', 'fetch_all',
    'rebase_branch', 'abort_rebase', 'continue_rebase',
    'create_tag', 'delete_tag', 'list_tags', 'push_tag',
    'create_release_branch', 'prepare_release', 'finalize_release', 'cleanup_release',
    'get_conflict_files', 'resolve_conflict', 'abort_merge', 'continue_merge',
    'get_commit_stats', 'hist_commit_history', 'get_contributor_stats'
]
