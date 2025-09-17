# GitHub Copilot Instructions for Wayne

## Project Overview
Wayne is a Python package that converts statistical formulas into model matrices using Polars DataFrames. It provides a single main function `trade_formula_for_matrix()` that takes a formula and DataFrame, returning a model matrix.

## Coding Standards

### Function Naming
- **Use snake_case for all function names** (e.g., `trade_formula_for_matrix`, `parse_formula_data`)
- Keep function names descriptive but concise
- Avoid camelCase or PascalCase for functions

### Code Style
- Keep it simple and readable
- Use type hints for function parameters and return values
- Follow existing patterns in the codebase
- Use Polars DataFrames as the primary data structure

### Documentation
- Include docstrings for all public functions
- Use clear examples in docstrings
- Document function parameters and return values

### Dependencies
- Core dependencies: polars, numpy, fiasto-py
- Maintain compatibility with Python 3.8+
- Avoid adding unnecessary dependencies

### Testing
- Write tests for new functions
- Use pytest for testing framework
- Test edge cases and error conditions
- Maintain existing test patterns

## Key Principles
1. **Simplicity**: Wayne does one thing well - formula to matrix conversion
2. **Consistency**: Follow existing naming and code patterns
3. **Performance**: Leverage Polars for efficient data operations
4. **Compatibility**: Support R-style statistical formulas