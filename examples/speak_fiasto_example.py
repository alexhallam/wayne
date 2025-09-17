"""
Example demonstrating the wayne.speak_fiasto() function.

This example shows how to use speak_fiasto to parse statistical formulas
and inspect their structure without needing to import fiasto-py directly.
"""

import wayne

def main():
    print("Wayne speak_fiasto() examples")
    print("=" * 40)
    
    # Example 1: Basic formula
    print("\n1. Basic formula parsing:")
    formula1 = "y ~ x1 + x2"
    parsed1 = wayne.speak_fiasto(formula1)
    print(f"Formula: {formula1}")
    print(f"Columns: {list(parsed1['columns'].keys())}")
    print(f"Has intercept: {parsed1['metadata']['has_intercept']}")
    
    # Example 2: Formula with interactions
    print("\n2. Formula with interactions:")
    formula2 = "mpg ~ cyl + wt*hp"
    parsed2 = wayne.speak_fiasto(formula2)
    print(f"Formula: {formula2}")
    print(f"Columns: {list(parsed2['columns'].keys())}")
    print(f"Has intercept: {parsed2['metadata']['has_intercept']}")
    
    # Example 3: Formula without intercept
    print("\n3. Formula without intercept:")
    formula3 = "y ~ x1 + x2 - 1"
    parsed3 = wayne.speak_fiasto(formula3)
    print(f"Formula: {formula3}")
    print(f"Columns: {list(parsed3['columns'].keys())}")
    print(f"Has intercept: {parsed3['metadata']['has_intercept']}")
    
    # Example 4: Complex formula with polynomials
    print("\n4. Complex formula with polynomials:")
    formula4 = "mpg ~ cyl + wt*hp + poly(disp, 3)"
    parsed4 = wayne.speak_fiasto(formula4)
    print(f"Formula: {formula4}")
    print(f"Columns: {list(parsed4['columns'].keys())}")
    print(f"Has intercept: {parsed4['metadata']['has_intercept']}")
    
    # Example 5: Inspecting variable roles
    print("\n5. Inspecting variable roles:")
    formula5 = "y ~ x1*x2 + poly(x3, 2)"
    parsed5 = wayne.speak_fiasto(formula5)
    print(f"Formula: {formula5}")
    for var_name, var_info in parsed5['columns'].items():
        roles = var_info['roles']
        print(f"  {var_name}: {roles}")
    
    # Example 6: Error handling
    print("\n6. Error handling:")
    try:
        wayne.speak_fiasto("invalid formula syntax")
    except ValueError as e:
        print(f"Caught expected error: {e}")
    
    print("\nDone! Use speak_fiasto() to parse formulas and inspect their structure.")
    print("This is useful for understanding how fiasto-py interprets your formulas")
    print("without needing to import fiasto-py directly.")

if __name__ == "__main__":
    main()