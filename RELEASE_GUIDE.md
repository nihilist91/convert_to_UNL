# 📦 How to Release New Versions

Your app uses **GitHub Actions** for automatic EXE building - no local compilation needed!

## 🚀 Release Process (3 Simple Steps)

### 1. Update Version

Edit `version.py`:
```python
__version__ = "1.1.0"  # Increment version
```

### 2. Commit and Push

```bash
git add .
git commit -m "Release v1.1.0 - Added Word support"
git push origin main
```

### 3. Create Tag

```bash
git tag v1.1.0
git push origin v1.1.0
```

**Done!** GitHub Actions will:
- Build the EXE with Python 3.13 ✅
- Create a release ✅
- Upload the EXE ✅

---

## 📥 Download Links

After build completes (~3-5 min):

**Release page:**  
`https://github.com/nihilist91/convert_to_UNL/releases/tag/v1.1.0`

**Direct download:**  
`https://github.com/nihilist91/convert_to_UNL/releases/download/v1.1.0/Excel_to_UNL_Converter.exe`

---

## 📊 Monitor Builds

Check workflow status:  
https://github.com/nihilist91/convert_to_UNL/actions

---

## 🔢 Version Numbering

Use Semantic Versioning (MAJOR.MINOR.PATCH):

- `v1.0.1` = Bug fixes only
- `v1.1.0` = New features (e.g., Word support)
- `v2.0.0` = Breaking changes

---

## 💡 Why This Works Better

✅ No Python 3.13 installation needed locally  
✅ No compiler/bootloader issues  
✅ Consistent builds every time  
✅ All releases automatically tracked  
✅ Users get clean, tested EXE files  

---

**That's it! Simple and automated. 🎉**
