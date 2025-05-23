"""
CLI implementation for the MVC Lab framework.
"""
import os
import shutil
import click
from pathlib import Path
from .git_agents.init_repo import init_repository

@click.group()
def cli():
    """MVC Lab - A framework for initializing web projects with MVC structure."""
    pass

@cli.command()
@click.argument('project_name')
def init(project_name):
    """Initialize a new project with MVC structure."""
    try:
        # Get the package directory
        package_dir = Path(__file__).parent
        
        # Create project directory
        project_path = Path(project_name)
        if project_path.exists():
            click.echo(f"Error: Directory '{project_name}' already exists.")
            return
        
        # Create project structure
        project_path.mkdir(parents=True)
        
        # Copy templates
        templates_dir = package_dir / 'templates'
        for item in templates_dir.iterdir():
            if item.is_dir():
                shutil.copytree(item, project_path / item.name)
        
        # Copy config files
        config_dir = package_dir / 'config_files'
        for item in config_dir.iterdir():
            if item.is_file():
                shutil.copy2(item, project_path)
        
        # Initialize Git repository
        repo = init_repository(str(project_path))
        
        click.echo(f"Successfully created project '{project_name}' with MVC structure.")
        click.echo(f"Project directory: {project_path.absolute()}")
        
    except Exception as e:
        click.echo(f"Error: {str(e)}")
        if project_path.exists():
            shutil.rmtree(project_path) 