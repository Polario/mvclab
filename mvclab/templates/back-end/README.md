# Back-end Template

This directory contains the back-end structure for your project.

## Directory Structure

- `models/`: Data models and database schemas
- `controllers/`: Business logic and request handlers
- `routes/`: API route definitions

## Getting Started

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the development server:
```bash
python app.py
```

## Development Guidelines

- Follow PEP 8 style guide
- Write docstrings for all functions and classes
- Include type hints
- Write tests for all functionality
- Keep controllers thin and models fat
- Use dependency injection where appropriate 