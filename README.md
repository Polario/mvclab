# MVC Lab

A framework for initializing web projects with MVC structure and configuration files for various tools.

## Features

- CLI tool for initializing web projects with a predefined MVC structure
- Configuration files for various development tools
- Git agent framework for automating version control tasks
- Support for both front-end and back-end development
- Integration with popular development tools

## Installation

```bash
pip install .
```

## Usage

Initialize a new project:

```bash
mvclab init my_project
```

This will create a new directory `my_project` with the following structure:

```
my_project/
├── front-end/
│   ├── designs/
│   ├── src/
│   └── public/
├── back-end/
│   ├── models/
│   ├── controllers/
│   └── routes/
└── shared/
```

## Configuration Files

The framework includes configuration files for various tools:

- `.gitignore`: Git ignore patterns
- `.cursorrules`: Cursor IDE rules
- `.copilotignore`: GitHub Copilot ignore patterns
- `v0.config.json`: v0 configuration
- `devin.config.json`: Devin configuration
- `jules.config.json`: Jules configuration
- `claude.config.json`: Claude configuration
- `codex.config.json`: Codex configuration

## Git Agent Framework

The framework includes a Git agent system for automating version control tasks:

- `init_repo.py`: Initialize Git repositories
- `branch_manager.py`: Manage Git branches
- `commit_agent.py`: Handle Git commits
- `merge_agent.py`: Manage Git merges
- `review_agent.py`: Code review automation

## Tool Integration

### Figma Integration

For tools like Figma that don't use local configuration files, integration is handled through:

1. API keys stored in environment variables
2. Plugin configurations
3. Design token exports

See the documentation for specific integration instructions.

## Development

1. Clone the repository:
```bash
git clone https://github.com/Polario/mvclab.git
cd mvclab
```

2. Install development dependencies:
```bash
pip install -e ".[dev]"
```

3. Run tests:
```bash
pytest
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 