# Contributing to Protein Structure-Function ML Project

Thank you for your interest in contributing to this project! This document provides guidelines and instructions for contributing.

## Getting Started

1. Fork the repository on GitHub
2. Clone your fork locally:
   ```bash
   git clone https://github.com/yourusername/protein-structure-function-ml-project.git
   cd protein-structure-function-ml-project
   ```
3. Create a new branch for your feature or bug fix:
   ```bash
   git checkout -b feature/your-feature-name
   ```

## Development Environment

1. Set up the conda environment:
   ```bash
   conda env create -f environment.yml
   conda activate protein-ml
   ```

2. Install pre-commit hooks:
   ```bash
   pre-commit install
   ```

## Code Style

- Follow PEP 8 guidelines for Python code
- Use Black for code formatting
- Write meaningful variable and function names
- Add type hints where appropriate
- Document all functions with Google-style docstrings

## Testing

- Write unit tests for new functionality
- Ensure all tests pass before submitting PR:
  ```bash
  pytest tests/
  ```
- Aim for at least 80% code coverage

## Submitting Changes

1. Commit your changes with descriptive commit messages
2. Push your branch to your fork
3. Create a Pull Request (PR) with:
   - Clear title and description
   - Reference to any related issues
   - Summary of changes made
   - Test results

## Documentation

- Update docstrings for modified functions
- Update README.md if needed
- Add examples to docstrings
- Document any new dependencies

## Adding New Features

When adding new features, please:

1. Follow the existing architecture patterns
2. Create appropriate abstract base classes
3. Implement proper interfaces
4. Add comprehensive error handling
5. Include unit tests
6. Update relevant documentation

## Project Structure Guidelines

- Place new data sources in `src/data/`
- Add feature extractors to `src/features/`
- Implement models in `src/models/`
- Create visualizations in `src/visualization/`
- Keep notebooks focused and well-documented

## Questions?

Feel free to open an issue for:
- Bug reports
- Feature requests
- General questions
- Documentation improvements

Thank you for contributing!