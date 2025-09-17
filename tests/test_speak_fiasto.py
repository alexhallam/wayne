"""
Test speak_fiasto functionality.
"""

import pytest
import wayne


def test_speak_fiasto_basic():
    """Test basic formula parsing with speak_fiasto."""
    formula = 'y ~ x1 + x2'
    result = wayne.speak_fiasto(formula)
    
    # Should return a dictionary with expected keys
    assert isinstance(result, dict)
    assert 'columns' in result
    assert 'metadata' in result
    
    # Check that columns are parsed correctly
    assert 'y' in result['columns']
    assert 'x1' in result['columns']
    assert 'x2' in result['columns']
    
    # Check that y is identified as response variable
    assert 'Response' in result['columns']['y']['roles']


def test_speak_fiasto_interactions():
    """Test interaction formula parsing."""
    formula = 'y ~ x1*x2'
    result = wayne.speak_fiasto(formula)
    
    assert isinstance(result, dict)
    assert 'columns' in result
    
    # Should have main effects and interaction terms
    columns = result['columns']
    assert 'y' in columns
    assert 'x1' in columns
    assert 'x2' in columns


def test_speak_fiasto_polynomials():
    """Test polynomial formula parsing."""
    formula = 'y ~ poly(x, 3)'
    result = wayne.speak_fiasto(formula)
    
    assert isinstance(result, dict)
    assert 'columns' in result
    
    # Should have response and polynomial terms
    columns = result['columns']
    assert 'y' in columns
    assert 'Response' in columns['y']['roles']


def test_speak_fiasto_no_intercept():
    """Test formula without intercept."""
    formula = 'y ~ x1 + x2 - 1'
    result = wayne.speak_fiasto(formula)
    
    assert isinstance(result, dict)
    assert 'metadata' in result
    
    # Should indicate no intercept
    metadata = result['metadata']
    assert 'has_intercept' in metadata
    assert metadata['has_intercept'] is False


def test_speak_fiasto_with_intercept():
    """Test formula with intercept (default)."""
    formula = 'y ~ x1 + x2'
    result = wayne.speak_fiasto(formula)
    
    assert isinstance(result, dict)
    assert 'metadata' in result
    
    # Should indicate has intercept by default
    metadata = result['metadata']
    assert 'has_intercept' in metadata
    assert metadata['has_intercept'] is True


def test_speak_fiasto_complex_formula():
    """Test complex formula with multiple terms."""
    formula = 'mpg ~ cyl + wt*hp + poly(disp, 4) - 1'
    result = wayne.speak_fiasto(formula)
    
    assert isinstance(result, dict)
    assert 'columns' in result
    assert 'metadata' in result
    
    # Check response variable
    assert 'mpg' in result['columns']
    assert 'Response' in result['columns']['mpg']['roles']
    
    # Should indicate no intercept
    assert result['metadata']['has_intercept'] is False


def test_speak_fiasto_invalid_formula():
    """Test that invalid formula raises ValueError."""
    with pytest.raises(ValueError) as exc_info:
        wayne.speak_fiasto('invalid formula syntax')
    
    assert "Failed to parse formula" in str(exc_info.value)


def test_speak_fiasto_empty_formula():
    """Test that empty formula raises ValueError."""
    with pytest.raises(ValueError) as exc_info:
        wayne.speak_fiasto('')
    
    assert "Failed to parse formula" in str(exc_info.value)


def test_speak_fiasto_return_type():
    """Test that speak_fiasto returns expected data structure."""
    formula = 'y ~ x1 + x2'
    result = wayne.speak_fiasto(formula)
    
    # Should be a dictionary
    assert isinstance(result, dict)
    
    # Should have columns as dict
    assert isinstance(result['columns'], dict)
    
    # Each column should have metadata
    for col_name, col_info in result['columns'].items():
        assert isinstance(col_info, dict)
        assert 'roles' in col_info
        assert isinstance(col_info['roles'], list)