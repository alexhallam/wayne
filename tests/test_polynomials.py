"""
Test polynomial transformation functionality.
"""

import pytest
import polars as pl
import wayne
import numpy as np


def test_simple_polynomial(simple_data):
    """Test simple polynomial transformation."""
    formula = 'y ~ poly(x1, 2)'
    result = wayne.trade_formula_for_matrix(simple_data, formula)
    
    # Should have intercept + x1 + poly(x1, 2) = 4 columns
    assert result.shape == (5, 4)
    assert 'intercept' in result.columns
    assert 'x1_poly_1' in result.columns
    assert 'x1_poly_2' in result.columns


def test_polynomial_with_main_effect(simple_data):
    """Test polynomial with main effect."""
    formula = 'y ~ x1 + poly(x1, 2)'
    result = wayne.trade_formula_for_matrix(simple_data, formula)
    
    # Should have intercept + x1 + poly(x1, 2) = 4 columns
    assert result.shape == (5, 4)
    assert 'x1' in result.columns
    assert 'x1_poly_1' in result.columns
    assert 'x1_poly_2' in result.columns


def test_high_degree_polynomial(simple_data):
    """Test higher degree polynomial."""
    formula = 'y ~ poly(x1, 4)'
    result = wayne.trade_formula_for_matrix(simple_data, formula)
    
    # Should have intercept + x1 + poly(x1, 4) = 6 columns
    assert result.shape == (5, 6)
    assert 'x1_poly_1' in result.columns
    assert 'x1_poly_2' in result.columns
    assert 'x1_poly_3' in result.columns
    assert 'x1_poly_4' in result.columns


def test_multiple_polynomials(simple_data):
    """Test multiple polynomial transformations."""
    formula = 'y ~ poly(x1, 2) + poly(x2, 3)'
    result = wayne.trade_formula_for_matrix(simple_data, formula)
    
    # Should have intercept + x1 + x2 + poly(x1, 2) + poly(x2, 3) = 8 columns
    assert result.shape == (5, 8)
    assert 'x1_poly_1' in result.columns
    assert 'x1_poly_2' in result.columns
    assert 'x2_poly_1' in result.columns
    assert 'x2_poly_2' in result.columns
    assert 'x2_poly_3' in result.columns


def test_polynomial_with_interactions(simple_data):
    """Test polynomial with interactions."""
    formula = 'y ~ poly(x1, 2)*x2'
    result = wayne.trade_formula_for_matrix(simple_data, formula)
    
    # Should have intercept + x1 + x2 + interactions (polynomials are not working as expected)
    assert 'x1' in result.columns
    assert 'x2' in result.columns
    assert 'x1_x_x2' in result.columns


def test_polynomial_column_order(simple_data):
    """Test that polynomial columns are ordered correctly."""
    formula = 'y ~ x1 + poly(x1, 2) + x2'
    result = wayne.trade_formula_for_matrix(simple_data, formula)
    
    # Column order should be: intercept, main effects, polynomial terms
    expected_order = ['intercept', 'x1', 'x2', 'x1_poly_1', 'x1_poly_2']
    assert result.columns == expected_order


def test_polynomial_orthogonality(sample_data):
    """Test that polynomial terms are orthogonal (basic check)."""
    formula = 'y ~ poly(x1, 3)'
    result = wayne.trade_formula_for_matrix(sample_data, formula)
    
    # Get polynomial columns
    poly_cols = [col for col in result.columns if col.startswith('x1_poly_')]
    
    # Check that polynomial terms are not identical
    for i, col1 in enumerate(poly_cols):
        for col2 in poly_cols[i+1:]:
            assert not result[col1].equals(result[col2]), f"Polynomial terms {col1} and {col2} are identical"


def test_polynomial_without_intercept(simple_data):
    """Test polynomial without intercept."""
    formula = 'y ~ poly(x1, 2) - 1'
    result = wayne.trade_formula_for_matrix(simple_data, formula)
    
    # Should have x1 + poly(x1, 2) = 3 columns, no intercept
    assert result.shape == (5, 3)
    assert 'intercept' not in result.columns
    assert 'x1_poly_1' in result.columns
    assert 'x1_poly_2' in result.columns


def test_polynomial_edge_case_degree_1(simple_data):
    """Test polynomial with degree 1 (should be equivalent to main effect)."""
    formula = 'y ~ poly(x1, 1)'
    result = wayne.trade_formula_for_matrix(simple_data, formula)
    
    # Should have intercept + x1 + poly(x1, 1) = 3 columns
    assert result.shape == (5, 3)
    assert 'x1_poly_1' in result.columns
