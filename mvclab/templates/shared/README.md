# Shared Template

This directory contains shared resources between front-end and back-end.

## Directory Structure

- `types/`: Shared TypeScript types and interfaces
- `constants/`: Shared constants and configuration
- `utils/`: Shared utility functions
- `schemas/`: Shared data schemas and validation

## Usage

1. Front-end:
```typescript
import { User } from '../shared/types';
import { API_URL } from '../shared/constants';
```

2. Back-end:
```python
from shared.types import User
from shared.constants import API_URL
```

## Development Guidelines

- Keep shared code minimal and focused
- Document all shared types and interfaces
- Maintain backward compatibility
- Version shared resources appropriately
- Include tests for shared utilities 