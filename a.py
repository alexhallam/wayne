import fiasto_py
import json

formula = "mpg ~ cyl + wt*hp + poly(disp, 4) - 1"
parsed = fiasto_py.parse_formula(formula)

print("Formula:", formula)
print("\nParsed result:")
print(json.dumps(parsed, indent=2))

# Look specifically at the columns and generated columns
print("\n" + "="*50)
print("COLUMNS ANALYSIS:")
for var_name, var_info in parsed["columns"].items():
    print(f"\nVariable: {var_name}")
    print(f"  Roles: {var_info.get('roles', [])}")
    print(f"  Generated columns: {var_info.get('generated_columns', [])}")
    print(f"  Interactions: {var_info.get('interactions', [])}")