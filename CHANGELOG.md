## [0.1.7] - 2025-09-20

Bumping for workflow testing

## [0.1.6] - 2025-09-20

### Fixed
- **Interaction term naming now matches fiasto-py 0.1.4 output exactly**
- Interaction terms now use proper naming convention (e.g., `wt_hp` instead of `wt_z`)



## [0.1.5] - 2025-09-20

### Added
- **Wayne Speak Fiasto**: Clean interface to fiasto-py parsing functionality
  - `wayne.speak_fiasto()` - Parse formulas and get raw fiasto-py results
  - Users can now access fiasto parsing without directly importing fiasto-py
  - Includes tests for fiasto parsing functionality
  

### Fixed
- **Orthogonal polynomials now match R's `poly()` function exactly**
- Interaction term naming now matches fiasto-py 0.1.4 output exactly
- Removed custom `_z` suffix logic that was inconsistent with fiasto-py naming
- Interaction terms now use proper naming convention (e.g., `wt_hp` instead of `wt_z`)
- Implemented R's exact three-term recurrence relation algorithm for orthogonal polynomials

### Changed
- Updated to use fiasto-py 0.1.4 for improved interaction term handling
- Interaction terms are now processed as separate variables with `InteractionTerm` role

## [0.1.4] - 2025-09-09

### Changed
- Interactions and ordering

## [0.1.3] - 2025-09-06

### Changed

- Complete rewrite using fiasto-py as the core parsing engine
- Removed all Rust dependencies and maturin build system
- Switched to pure Python implementation with setuptools
- Improved code organization with dedicated module for main function
- Enhanced formula support for interactions and polynomial transformations

### Added

- Full support for complex formulas with interactions (e.g., `wt*hp`)
- Polynomial transformation support (e.g., `poly(disp, 4)`)
- Proper column ordering to match R's model.matrix() output
- Clean, maintainable code structure

## [0.1.1] - 2025-09-04

### Added

- had to change pypi name from wayne to `wayne-trade`

## [0.1.0] - 2025-09-04

### Added

- Initial release