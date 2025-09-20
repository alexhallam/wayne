# Wayne Release Process

This document explains how to release new versions of wayne to PyPI automatically.

## 🚀 How Releases Work

### Automatic Release Trigger
Releases are automatically triggered when you push changes to the `main` branch that modify:
- `CHANGELOG.md` 
- `pyproject.toml`

### Release Process
1. **Version Detection**: The workflow extracts the version from the latest entry in `CHANGELOG.md`
2. **Version Update**: Updates `pyproject.toml` to match the CHANGELOG version
3. **Build**: Builds the package using `uv build`
4. **PyPI Check**: Checks if the version already exists on PyPI
5. **Publish**: Publishes to PyPI if it's a new version
6. **GitHub Release**: Creates a GitHub release with changelog content

## 📝 How to Release a New Version

### Step 1: Update CHANGELOG.md
Add a new version entry at the top of `CHANGELOG.md`:

```markdown
## [0.1.7] - 2025-01-09

### Added
- New feature description

### Fixed
- Bug fix description

### Changed
- Change description
```

### Step 2: Commit and Push
```bash
git add CHANGELOG.md
git commit -m "Release v0.1.7"
git push origin main
```

### Step 3: Monitor the Release
- Check the [Actions tab](https://github.com/alexhallam/wayne/actions) in your GitHub repository
- The workflow will automatically detect your version and publish to PyPI
- A GitHub release will be created with the changelog content

## 🔧 Setup Requirements

### PyPI API Token
You need to set up a PyPI API token in your GitHub repository:

1. Go to [PyPI Account Settings](https://pypi.org/manage/account/token/)
2. Create a new API token (scope: "Entire account" or "Specific project: wayne-trade")
3. Copy the token (starts with `pypi-`)
4. In your GitHub repository, go to Settings → Secrets and variables → Actions
5. Add a new repository secret named `PYPI_API_TOKEN` with your token value

### Manual Release (Optional)
You can also trigger releases manually:
1. Go to Actions → Release to PyPI
2. Click "Run workflow"
3. Select the main branch and click "Run workflow"

## 🐍 Python Version Requirements

**Important**: wayne requires Python 3.13+ due to fiasto-py dependency requirements. The GitHub Actions workflow uses Python 3.13 to ensure compatibility.

## 📋 Version Format

The workflow expects CHANGELOG entries in this format:
```markdown
## [X.Y.Z] - YYYY-MM-DD
```

Examples:
- `## [0.1.7] - 2025-01-09`
- `## [1.0.0] - 2025-01-09`
- `## [0.2.0] - 2025-01-09`

## 🛡️ Safety Features

- **Duplicate Prevention**: Checks if version already exists on PyPI before publishing
- **Changelog Required**: Only triggers on CHANGELOG.md changes
- **Version Sync**: Automatically updates pyproject.toml to match CHANGELOG version
- **Manual Override**: Can be triggered manually if needed

## 🔍 Troubleshooting

### Release Failed?
1. Check the [Actions tab](https://github.com/alexhallam/wayne/actions) for error details
2. Common issues:
   - Missing `PYPI_API_TOKEN` secret
   - Version already exists on PyPI
   - Invalid version format in CHANGELOG.md

### Version Already Exists?
If you try to release a version that already exists on PyPI:
1. Update the version in CHANGELOG.md to a new version
2. Commit and push again

### Manual Release Needed?
1. Go to Actions → Release to PyPI
2. Click "Run workflow"
3. This bypasses the CHANGELOG.md change requirement

## 📦 What Gets Released

The workflow will:
- ✅ Build the package using `uv build`
- ✅ Publish to PyPI as `wayne-trade`
- ✅ Create a GitHub release
- ✅ Include changelog content in the GitHub release
- ✅ Tag the release with `v{version}`

## 🎯 Best Practices

1. **Always update CHANGELOG.md first** - this is what triggers the release
2. **Use semantic versioning** - follow MAJOR.MINOR.PATCH format
3. **Test locally first** - run `uv build` to ensure the package builds
4. **Check PyPI** - verify the release appears on [PyPI](https://pypi.org/project/wayne-trade/)

## 📞 Support

If you have issues with the release process:
1. Check the GitHub Actions logs
2. Verify your PyPI API token is correct
3. Ensure your CHANGELOG.md format matches the expected pattern
4. Check that the version doesn't already exist on PyPI
