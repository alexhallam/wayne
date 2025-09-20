#!/usr/bin/env python3
"""
Compare wayne's polynomial output with R's poly(disp, 4) output
"""

import wayne
import polars as pl
import numpy as np

# Load the data
mtcars = pl.read_csv("data/mtcars.csv")
r_poly = pl.read_csv("data/mtcars_poly_4.csv")

print("Comparing wayne vs R poly(disp, 4) output...")
print("=" * 60)

# Test wayne's polynomial generation
formula = "mpg ~ wt + hp + cyl + wt*hp + poly(disp, 4) - 1"
wayne_result = wayne.trade_formula_for_matrix(mtcars, formula)

print(f"Wayne formula: {formula}")
print(f"Wayne result shape: {wayne_result.shape}")
print(f"Wayne columns: {wayne_result.columns}")

# Extract polynomial columns from wayne
wayne_poly_cols = [col for col in wayne_result.columns if col.startswith('disp_poly_')]
print(f"Wayne polynomial columns: {wayne_poly_cols}")

# Extract polynomial columns from R
r_poly_cols = [col for col in r_poly.columns if col.startswith('poly_disp_')]
print(f"R polynomial columns: {r_poly_cols}")

print("\n" + "=" * 60)
print("COMPARISON:")

# Compare the polynomial values
for i, (wayne_col, r_col) in enumerate(zip(wayne_poly_cols, r_poly_cols)):
    wayne_values = wayne_result[wayne_col].to_list()
    r_values = r_poly[r_col].to_list()
    
    print(f"\nPolynomial term {i+1}:")
    print(f"  Wayne column: {wayne_col}")
    print(f"  R column: {r_col}")
    
    # Check if values are close (within tolerance)
    wayne_array = np.array(wayne_values)
    r_array = np.array(r_values)
    
    # Calculate differences
    diff = np.abs(wayne_array - r_array)
    max_diff = np.max(diff)
    mean_diff = np.mean(diff)
    
    print(f"  Max difference: {max_diff:.10f}")
    print(f"  Mean difference: {mean_diff:.10f}")
    
    # Check if they're close enough (tolerance of 1e-10)
    tolerance = 1e-10
    is_close = np.allclose(wayne_array, r_array, atol=tolerance)
    print(f"  Within tolerance ({tolerance}): {is_close}")
    
    if not is_close:
        print(f"  ❌ MISMATCH DETECTED!")
        print(f"  First 5 Wayne values: {wayne_values[:5]}")
        print(f"  First 5 R values: {r_values[:5]}")
    else:
        print(f"  ✅ MATCH!")

print("\n" + "=" * 60)
print("SUMMARY:")
print(f"Wayne polynomial columns: {len(wayne_poly_cols)}")
print(f"R polynomial columns: {len(r_poly_cols)}")
print(f"Columns match: {len(wayne_poly_cols) == len(r_poly_cols)}")
