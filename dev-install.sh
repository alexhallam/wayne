#!/bin/bash
# Development install script for wayne package with uv

# Clean previous build
rm -rf target/wheels/wayne_trade-*

# Build the package
maturin build

# Publish with uv
uv publish target/wheels/wayne_trade-0.1.1-*.whl