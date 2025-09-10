#!/bin/bash
# Development install script for wayne package with uv

# Clean previous build
rm -rf dist/

# Build the package
uv build

# Install in development mode
uv pip install -e .