# 📊 Excel/Word to UNL Converter

<div align="center">

![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![Platform](https://img.shields.io/badge/platform-Windows-lightgrey.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

**A modern desktop application to convert Excel and Word virement files to UNL format**

[📥 Download Latest Release](https://github.com/nihilist91/convert_to_UNL/releases) | [📖 User Guide](USER_GUIDE.md) | [🐛 Report Bug](https://github.com/nihilist91/convert_to_UNL/issues)

</div>

---

## ✨ Features

- ✅ **Excel to UNL Conversion** - Convert Excel virement files to UNL format
- ✅ **Modern Interface** - Clean PyQt6 GUI with intuitive controls
- ✅ **Auto-Filename Generation** - Automatically generates 24-character filenames
- ✅ **Auto-Description** - Updates description based on selected date
- ✅ **Date Picker** - Calendar widget for easy date selection
- ✅ **Real-time Preview** - See UNL output before saving
- ✅ **Data Validation** - Ensures all required fields are filled
- ⏳ **Word Support** - Coming in v1.1.0!

---

## 📥 Download & Installation

### Option 1: Download EXE (Recommended)

1. Go to [Releases](https://github.com/nihilist91/convert_to_UNL/releases)
2. Download `Excel_to_UNL_Converter.exe`
3. Run the EXE - **No installation needed!**

**System Requirements:**
- Windows 10/11 (64-bit)
- No Python or other dependencies required

### Option 2: Run from Source

```bash
# Clone repository
git clone https://github.com/nihilist91/convert_to_UNL.git
cd convert_to_UNL

# Create virtual environment
python -m venv .venv
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run application
python excel_to_unl_converter.py
```

---

## 🚀 Quick Start

1. **Launch the application**
2. **Browse** for your Excel file
3. **Fill in** the required fields (auto-filled where possible)
4. **Select date** using the calendar picker
5. **Click Convert** to generate UNL
6. **Preview** the output
7. **Save** the UNL file

📖 For detailed instructions, see [USER_GUIDE.md](USER_GUIDE.md)

---

## 📸 Screenshots

### Main Interface
*Modern PyQt6 interface with all controls in one window*

### File Selection
*Browse and select Excel files for conversion*

### Preview & Save
*Real-time preview of UNL output before saving*

---

## 🔧 Technical Details

### Built With
- **Python 3.14** - Programming language
- **PyQt6** - Modern GUI framework
- **pandas** - Excel file processing
- **openpyxl** - Excel file format support
- **PyInstaller** - Standalone EXE creation

### File Format
- **Input:** Excel (.xlsx, .xls) | Word (.docx, .doc - coming soon)
- **Output:** UNL (pipe-delimited text format)

### Filename Convention
```
bvov{cod_emet}{cod_dest}00000{DDMMYY}{remise}.unl
Example: bvov10105000002510160001.unl
```

---

## 📋 Version History

### v1.0.0 (2025-10-28)
- ✅ Excel file to UNL conversion
- ✅ Modern PyQt6 interface
- ✅ Auto-filename generation
- ✅ Auto-description update
- ✅ Date picker with calendar
- ✅ Real-time preview
- ✅ Standalone EXE distribution

### Coming in v1.1.0
- ⏳ Word document support
- ⏳ Batch conversion
- ⏳ Settings persistence

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

## 📞 Support & Contact

**Developer:** CHAARAOUI MOHAMMED  
**Phone:** 0659226281  
**Email:** [Contact via GitHub](https://github.com/nihilist91)

For bugs or feature requests, please [open an issue](https://github.com/nihilist91/convert_to_UNL/issues).

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 🙏 Acknowledgments

- Built with Python and PyQt6
- Inspired by the need for efficient UNL file generation
- Thanks to all users and contributors

---

<div align="center">

**Made with ❤️ by CHAARAOUI MOHAMMED**

[⬆ Back to Top](#-excelword-to-unl-converter)

</div>
