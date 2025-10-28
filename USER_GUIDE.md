# 📄 Excel to UNL Converter - User Guide

Modern desktop application to convert Excel virement files to UNL format.

## 🚀 Quick Start

### First Time Setup
```bash
pip install -r requirements.txt
```

### Run the Application
**Easiest:** Double-click `run_converter.bat`

**Or:** 
```bash
python excel_to_unl_converter.py
```

## 📝 How to Use

1. Click **"Browse Excel File"** → Select your Excel file
2. Fill in the header fields:
   - File Name (auto-generated)
   - Description (e.g., "ov 16/10/2025")
   - Generation Date (📅 use date picker)
   - Sender Code (default: 10)
   - Destination Code (default: 1050)
   - Remittance Number (default: 0001)
   - User Name
   - Phone Number
3. Click **"🔄 Convert to UNL"**
4. Review the preview
5. Click **"💾 Save UNL File"**
6. Done! ✅

## 📊 Excel Format Required

Your Excel file must have:
- **Row 13**: Headers (N°, NOM, PRENOM, RIB, AGENCE, MONTANT)
- **Row 14+**: Data rows
  - Column B: Number (1, 2, 3...)
  - Column C: Last name
  - Column D: First name
  - Column E: RIB (24 digits)
  - Column G: Amount

**Example:** See `samples/CNTR_PRIMAIR.xlsx`

## 📁 Folder Structure

```
virement_masse/
├── excel_to_unl_converter.py    ← Main app
├── run_converter.bat            ← Click to run
├── requirements.txt             ← Dependencies
├── test_conversion.py           ← Test script
├── USER_GUIDE.md                ← This file
└── samples/                     ← Examples
    ├── CNTR_PRIMAIR.xlsx
    └── *.unl files
```

## 🔧 Troubleshooting

**App won't start?**
```bash
pip install -r requirements.txt
```

**Excel not recognized?**
- Check "NOM" header is in row 13
- Data must start at row 14

**Text not visible?**
- Restart the app - all text should be black on white

## ✨ Features

- 📅 Date Picker (easy calendar selection)
- 👁️ Live Preview
- ✅ Auto Validation
- ⚡ Fast (< 1 second)
- 🎨 Clean Modern UI

---

For examples, check the `samples/` folder.
