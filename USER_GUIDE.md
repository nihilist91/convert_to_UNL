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

## 📊 Supported Excel Formats

The application **automatically detects** the Excel file format and processes it accordingly. It supports:

### 1. CNTR Format
Traditional format with specific column layout:
- **Row with "NOM" header**: The application looks for "NOM" in column C
- **Data starts**: Next row after "NOM" header
- **Column Layout**:
  - Column B: Number (1, 2, 3...)
  - Column C: Last name (NOM)
  - Column D: First name (PRENOM)
  - Column E: RIB (24 digits)
  - Column G: Amount (MONTANT)
- **Ends at**: Row containing "SOMME"

**Example:** See `samples/CNTR_PRIMAIR.xlsx`

### 2. BOUDOUR Format
Flexible format with automatic column detection:
- **Header Detection**: Looks for keywords like "RIB", "MONTANT", "DESIGNATION", "BÉNÉFICIAIRE"
- **Automatic Column Mapping**: The application automatically identifies which columns contain:
  - Names/Beneficiaries
  - RIB numbers
  - Amounts
  - Row numbers (if present)
- **Flexible Layout**: Works with different column arrangements
- **Ends at**: Row containing "TOTAL" or "SOMME"

### Auto-Detection
If no clear headers are found, the application uses intelligent pattern recognition:
- **RIB Detection**: Looks for 20-24 digit numbers
- **Amount Detection**: Identifies decimal numbers
- **Name Detection**: Recognizes text fields
- Assigns sequential numbers automatically

### Format Detection Messages
When you convert a file, you'll see which format was detected:
- "Detected format: CNTR. Processing..."
- "Detected format: BOUDOUR. Processing..."
- Success message shows: "X records processed (Format: CNTR/BOUDOUR)"

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
