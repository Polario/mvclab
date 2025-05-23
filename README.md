# mvclab Framework

mvclab is a modular, agent-based framework for managing Git-based projects. It automates and streamlines repository management, Git workflows, and project scaffolding for teams and individuals.

## Features
- **Repository Initialization Agent:** Initializes new repositories locally and on hosting platforms.
- **Cloning Agent:** Clones existing repositories to local machines.
- **Branch Management Agent:** Creates, switches, and deletes branches as needed.
- **Commit Agent:** Stages changes and commits them with appropriate messages.
- **Push/Pull Agent:** Pushes changes to remote repositories and pulls updates.
- **Merge Agent:** Merges branches and handles conflicts.
- **Rebase Agent:** Performs rebases to maintain a clean commit history.
- **Tag Agent:** Creates and manages tags for releases.
- **Code Review Agent:** Analyzes code changes and provides feedback or approvals.
- **Release Management Agent:** Manages the release process, including creating release branches and tags.
- **Conflict Resolution Agent:** Assists in resolving merge conflicts by suggesting resolutions.
- **History Analysis Agent:** Analyzes commit history for reporting and insights.
- **Issue Tracking Integration Agent:** Links commits to issue trackers and updates statuses.
- **CI/CD Integration Agent:** Triggers builds and deployments based on Git events.
- **Access Control Agent:** Manages permissions and access to repositories.
- **Configurable Agents:** Use JSON config files to customize agent behavior.
- **Project Templates:** Quickly scaffold front-end, back-end, and shared codebases.
- **CLI Tool:** All features accessible via a robust command-line interface.
- **Web Home Page:** A local web UI is available after install, with a Home tab and a Test tab to run all framework tests interactively.

## Why mvclab?
- **Productivity:** Automate repetitive Git tasks and reduce human error.
- **Consistency:** Enforce best practices and workflows across teams.
- **Extensibility:** Easily add new agents for custom workflows.
- **Transparency:** Detailed logging and reporting for all operations.

## Quick Start
```bash
pip install -e .
# or
pip install mvclab
```

To create a new project:
```bash
mvclab init my_project
cd my_project
```

## Testing the Framework
You can test all features using the provided test script:

```bash
python test_git_agents.py
```

Or, after installing, visit the local home page (see below) and use the **Test** tab to run all tests interactively in your browser.

## Home Page (Web UI)
After installing mvclab, you can launch the local web UI:

```bash
mvclab web
```

- **Home Tab:** Overview of your project, agents, and recent activity.
- **Test Tab:** Run all framework tests and view results in real time.

## CLI Usage
```bash
mvclab --help
```

## Development
- See `requirements.txt` and `pyproject.toml` for dependencies.
- Agents are in `mvclab/git_agents/`.
- Config templates are in `mvclab/config_files/`.
- Project templates are in `mvclab/templates/`.

## License
MIT 