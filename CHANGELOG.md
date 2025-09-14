## [0.1.4] - 2025-09-14

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