import os
from datetime import datetime, timedelta
import traceback

print("[LOG] test_git_agents.py script started.")

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

results = {}

def log(msg):
    print(f"[LOG] {msg}")

def test_basic_operations():
    name = "Basic Operations"
    try:
        repo_path = os.getcwd()
        log(f"Testing {name} in {repo_path}")
        log(f"Current branches: {list_branches(repo_path)}")
        new_branch = create_branch(repo_path, 'feature-branch')
        log(f"Created branch: {getattr(new_branch, 'name', str(new_branch))}")
        log(f"Branches after creation: {list_branches(repo_path)}")
        with open('test.txt', 'w') as f:
            f.write('Test content')
        commit = create_commit(repo_path, 'Add test file')
        log(f"Commit created: {getattr(commit, 'hexsha', str(commit))}")
        history = get_commit_history(repo_path)
        log(f"Commit history: {[getattr(c, 'hexsha', str(c)) for c in history]}")
        results[name] = 'PASS'
    except Exception as e:
        log(f"{name} failed: {e}\n{traceback.format_exc()}")
        results[name] = 'FAIL'

def test_merge_operations():
    name = "Merge Operations"
    try:
        repo_path = os.getcwd()
        log(f"Testing {name}")
        merge_branch_name = 'merge-test'
        create_branch(repo_path, merge_branch_name)
        with open('merge_test.txt', 'w') as f:
            f.write('Merge test content')
        create_commit(repo_path, 'Add merge test file')
        merge_result = merge_branch(repo_path, merge_branch_name, 'main')
        log(f"Merge successful: {getattr(merge_result, 'hexsha', str(merge_result))}")
        delete_branch(repo_path, merge_branch_name)
        results[name] = 'PASS'
    except Exception as e:
        log(f"{name} failed: {e}\n{traceback.format_exc()}")
        results[name] = 'FAIL'

def test_rebase_operations():
    name = "Rebase Operations"
    try:
        repo_path = os.getcwd()
        log(f"Testing {name}")
        rebase_branch_name = 'rebase-test'
        create_branch(repo_path, rebase_branch_name)
        with open('rebase_test.txt', 'w') as f:
            f.write('Rebase test content')
        create_commit(repo_path, 'Add rebase test file')
        rebase_branch(repo_path, 'main', rebase_branch_name)
        log("Rebase successful")
        delete_branch(repo_path, rebase_branch_name)
        results[name] = 'PASS'
    except Exception as e:
        log(f"{name} failed: {e}\n{traceback.format_exc()}")
        results[name] = 'FAIL'

def test_tag_operations():
    name = "Tag Operations"
    try:
        repo_path = os.getcwd()
        log(f"Testing {name}")
        tag_name = 'test-tag'
        create_tag(repo_path, tag_name, 'Test tag')
        log(f"Created tag: {tag_name}")
        tags = list_tags(repo_path)
        log(f"Current tags: {tags}")
        delete_tag(repo_path, tag_name)
        log(f"Deleted tag: {tag_name}")
        results[name] = 'PASS'
    except Exception as e:
        log(f"{name} failed: {e}\n{traceback.format_exc()}")
        results[name] = 'FAIL'

def test_release_operations():
    name = "Release Operations"
    try:
        repo_path = os.getcwd()
        log(f"Testing {name}")
        version = '1.0.0'
        release_branch = create_release_branch(repo_path, version)
        log(f"Created release branch: {release_branch}")
        prepare_release(repo_path, version)
        log(f"Prepared release: {version}")
        tag_name = finalize_release(repo_path, version, 'Release 1.0.0')
        log(f"Finalized release with tag: {tag_name}")
        cleanup_release(repo_path, version)
        log("Cleaned up release")
        results[name] = 'PASS'
    except Exception as e:
        log(f"{name} failed: {e}\n{traceback.format_exc()}")
        results[name] = 'FAIL'

def test_history_analysis():
    name = "History Analysis"
    try:
        repo_path = os.getcwd()
        log(f"Testing {name}")
        since = datetime.now() - timedelta(days=7)
        stats = get_commit_stats(repo_path, since=since)
        log(f"Commit stats: {stats}")
        contributor_stats = get_contributor_stats(repo_path, since=since)
        log(f"Contributor stats: {contributor_stats}")
        results[name] = 'PASS'
    except Exception as e:
        log(f"{name} failed: {e}\n{traceback.format_exc()}")
        results[name] = 'FAIL'

def test_clone_and_pull_push():
    name = "Clone/Pull/Push Operations"
    try:
        repo_path = os.getcwd()
        log(f"Testing {name}")
        fetch_all(repo_path)
        log("Fetch all remotes successful")
        try:
            push_changes(repo_path)
            log("Push changes successful")
        except Exception as e:
            log(f"Push changes failed (expected if no remote): {e}")
        try:
            pull_changes(repo_path)
            log("Pull changes successful")
        except Exception as e:
            log(f"Pull changes failed (expected if no remote): {e}")
        results[name] = 'PASS'
    except Exception as e:
        log(f"{name} failed: {e}\n{traceback.format_exc()}")
        results[name] = 'FAIL'

def test_conflict_resolution():
    name = "Conflict Resolution"
    try:
        repo_path = os.getcwd()
        log(f"Testing {name}")
        conflict_files = get_conflict_files(repo_path)
        log(f"Conflict files: {conflict_files}")
        results[name] = 'PASS'
    except Exception as e:
        log(f"{name} failed: {e}\n{traceback.format_exc()}")
        results[name] = 'FAIL'

def main():
    log("Starting robust Git agent tests...")
    test_functions = [
        test_basic_operations,
        test_merge_operations,
        test_rebase_operations,
        test_tag_operations,
        test_release_operations,
        test_history_analysis,
        test_clone_and_pull_push,
        test_conflict_resolution
    ]
    for func in test_functions:
        try:
            func()
        except Exception as e:
            log(f"Test function {func.__name__} crashed: {e}\n{traceback.format_exc()}")
    log("\nTest Summary:")
    for k, v in results.items():
        print(f"  {k}: {v}")
    log("All tests attempted.")

if __name__ == '__main__':
    main() 