import polars as pl
import numpy as np
import wayne

# Create sample data with more variables
np.random.seed(42)
n = 100
df = pl.DataFrame({
    'y': np.random.normal(0, 1, n),
    'x1': np.random.normal(0, 1, n),
    'x2': np.random.normal(0, 1, n),
    'x3': np.random.normal(0, 1, n)
})

# Test complex formula with interactions
model_matrix = wayne.trade_formula_for_matrix(df, 'y ~ x1 + x2*x3 + poly(x1, 2)')
print(model_matrix)