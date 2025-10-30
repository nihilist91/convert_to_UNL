# GitHub Actions Workflow Guide - Building EXE on GitHub

This guide explains how to automatically build the EXE file using GitHub Actions.

## 📋 How It Works

The workflow is **already configured** in `.github/workflows/windows-release.yml` and will:

1. ✅ Automatically trigger when you push a **version tag** (e.g., `v1.1.0`)
2. ✅ Build the EXE file on Windows
3. ✅ Create a GitHub Release
4. ✅ Upload the EXE file to the release

---

## 🚀 How to Build and Release

### Option 1: Create Release via Git Tags (Recommended)

#### Step 1: Commit Your Changes
```bash
git add .
git commit -m "Release v1.1.0 - Multi-format support"
```

#### Step 2: Create a Git Tag
```bash
# Tag format: v{MAJOR}.{MINOR}.{PATCH}
git tag v1.1.0

# Or with a message
git tag -a v1.1.0 -m "Release v1.1.0 - Multi-format Excel support"
```

#### Step 3: Push Tag to GitHub
```bash
# Push commits
git push origin main

# Push the tag (this triggers the workflow!)
git push origin v1.1.0
```

#### Step 4: Watch the Workflow Run
1. Go to: https://github.com/nihilist91/convert_to_UNL/actions
2. You'll see "Build and release Windows EXE" running
3. Wait ~5 minutes for completion
4. Check the "Releases" page for your new release!

---

### Option 2: Create Release via GitHub Web Interface

#### Step 1: Push Your Code
```bash
git add .
git commit -m "Release v1.1.0 - Multi-format support"
git push origin main
```

#### Step 2: Create Release on GitHub
1. Go to: https://github.com/nihilist91/convert_to_UNL
2. Click **"Releases"** (right sidebar)
3. Click **"Draft a new release"**
4. In **"Choose a tag"**: Type `v1.1.0` and select **"Create new tag: v1.1.0 on publish"**
5. **Release title**: `Release v1.1.0`
6. **Description**: Add release notes (copy from CHANGELOG.md)
7. Click **"Publish release"**
8. This will trigger the workflow automatically!

---

## 📁 What the Workflow Does

```yaml
name: Build and release Windows EXE

on:
  push:
    tags:
      - 'v*'  # Triggers on any tag starting with 'v'

jobs:
  build-windows-exe:
    runs-on: windows-latest  # Uses Windows runner
    
    steps:
      1. Checkout code
      2. Setup Python 3.13
      3. Install dependencies from requirements.txt
      4. Install PyInstaller
      5. Build EXE using Excel_to_UNL_Converter.spec
      6. Create GitHub Release
      7. Upload EXE to release
```

---

## 🔍 Monitoring the Build

### Check Workflow Status

**Via GitHub Website:**
1. Go to: https://github.com/nihilist91/convert_to_UNL/actions
2. Click on the running workflow
3. Expand steps to see detailed logs
4. Green checkmark = success ✅
5. Red X = failed ❌

**Via Git Command:**
```bash
# Install GitHub CLI (if not installed)
# Then check workflow runs
gh run list
gh run view  # View latest run
```

### Build Time
- Typical build time: **3-5 minutes**
- Steps breakdown:
  - Checkout: ~10 seconds
  - Setup Python: ~30 seconds
  - Install dependencies: ~1-2 minutes
  - Build EXE: ~1-2 minutes
  - Create release: ~10 seconds

---

## 📦 After Build Completes

### Download the EXE

**Via GitHub Releases:**
1. Go to: https://github.com/nihilist91/convert_to_UNL/releases
2. Find your release (e.g., "Release v1.1.0")
3. Download `Excel_to_UNL_Converter.exe` from Assets

**Direct Link Format:**
```
https://github.com/nihilist91/convert_to_UNL/releases/download/v1.1.0/Excel_to_UNL_Converter.exe
```

### Update README Badges
Your README already has a download link that automatically points to the latest release:
```markdown
[📥 Download Latest Release](https://github.com/nihilist91/convert_to_UNL/releases)
```

---

## 🛠️ Current Workflow Configuration

### Trigger Condition
```yaml
on:
  push:
    tags:
      - 'v*'
```
This means the workflow **only runs when you push a tag** starting with `v`.

### Python Version
```yaml
python-version: '3.13'
```
The workflow uses Python 3.13 (latest stable).

### Build Command
```yaml
pyinstaller Excel_to_UNL_Converter.spec --noconfirm
```
Uses the spec file to build with all configurations.

### Output Location
```
dist\Excel_to_UNL_Converter.exe
```

---

## 📋 Complete Release Checklist

For releasing v1.1.0 with multi-format support:

- [x] 1. Update code with new features
- [x] 2. Update `version.py` to `1.1.0`
- [x] 3. Update `CHANGELOG.md` with release notes
- [x] 4. Update `README.md` with new version badge
- [ ] 5. Commit all changes
- [ ] 6. Create git tag `v1.1.0`
- [ ] 7. Push commits and tag to GitHub
- [ ] 8. Wait for workflow to complete
- [ ] 9. Verify release on GitHub
- [ ] 10. Test downloaded EXE

---

## 🎯 Quick Commands for v1.1.0 Release

```bash
# 1. Commit changes
git add .
git commit -m "Release v1.1.0 - Add multi-format Excel support (CNTR + BOUDOUR)"

# 2. Create and push tag
git tag -a v1.1.0 -m "v1.1.0 - Multi-format Excel support with automatic detection"
git push origin main
git push origin v1.1.0

# 3. Watch the workflow
# Open: https://github.com/nihilist91/convert_to_UNL/actions

# 4. After build completes, check releases
# Open: https://github.com/nihilist91/convert_to_UNL/releases
```

---

## 🐛 Troubleshooting

### Workflow Not Triggering?

**Check:**
1. ✅ Did you push the tag? `git push origin v1.1.0`
2. ✅ Does tag start with 'v'? (e.g., `v1.1.0` not `1.1.0`)
3. ✅ Check Actions tab: https://github.com/nihilist91/convert_to_UNL/actions

### Build Failing?

**Common Issues:**
1. **Missing dependencies**: Check `requirements.txt` is up to date
2. **Spec file errors**: Verify `Excel_to_UNL_Converter.spec` is correct
3. **Python version**: Workflow uses Python 3.13
4. **Import errors**: Check all imports in code work

**View Logs:**
1. Go to Actions tab
2. Click on failed workflow
3. Expand red steps
4. Read error messages

### Release Not Created?

**Check:**
1. ✅ Workflow completed successfully
2. ✅ Permissions: Workflow has `contents: write` permission
3. ✅ Tag format: Should be `v*` (e.g., `v1.1.0`)

---

## 🔐 Permissions

The workflow already has the required permissions:
```yaml
permissions:
  contents: write  # Allows creating releases
```

No additional configuration needed!

---

## 📝 Version Numbering Convention

Follow [Semantic Versioning](https://semver.org/):

```
v{MAJOR}.{MINOR}.{PATCH}

MAJOR: Breaking changes (v2.0.0)
MINOR: New features, backward compatible (v1.1.0) ← Current
PATCH: Bug fixes (v1.0.1)
```

Examples:
- `v1.0.0` - Initial release
- `v1.1.0` - Added multi-format support (current)
- `v1.1.1` - Bug fix for format detection
- `v1.2.0` - Add Word file support
- `v2.0.0` - Major rewrite

---

## 🎉 That's It!

Your workflow is ready to go. Just push a tag and watch the magic happen! 🚀

**Next Release:**
```bash
git tag v1.1.0
git push origin v1.1.0
```

Then check: https://github.com/nihilist91/convert_to_UNL/releases
