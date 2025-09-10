"""
Pytest configuration and shared fixtures for wayne tests.
"""

import pytest
import polars as pl
import numpy as np


@pytest.fixture
def sample_data():
    """Create sample data for testing."""
    np.random.seed(42)
    n = 100
    return pl.DataFrame({
        'y': np.random.normal(0, 1, n),
        'x1': np.random.normal(0, 1, n),
        'x2': np.random.normal(0, 1, n),
        'x3': np.random.normal(0, 1, n),
        'categorical': np.random.choice(['A', 'B', 'C'], n)
    })


@pytest.fixture
def mtcars_data():
    """Load mtcars data for testing."""
    return pl.read_csv('data/mtcars.csv')


@pytest.fixture
def simple_data():
    """Create simple data for basic tests."""
    return pl.DataFrame({
        'y': [1, 2, 3, 4, 5],
        'x1': [1, 2, 3, 4, 5],
        'x2': [2, 4, 6, 8, 10]
    })

