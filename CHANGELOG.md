# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-10-28

### Added
- Excel file to UNL conversion functionality
- Modern PyQt6 graphical user interface
- Auto-filename generation (24 characters: bvov{codes}00000{date}{remise}.unl)
- Auto-description update in "ov {date}" format
- Date picker with calendar popup
- Real-time UNL preview before saving
- Data validation for all required fields
- Developer credit footer with contact info
- Standalone EXE distribution (no Python needed)
- Comprehensive user guide
- Sample files for testing
- Batch build scripts

### Features
- Browse and select Excel files (.xlsx, .xls)
- Input fields for all UNL header information
- Calendar widget for date selection
- Preview pane showing generated UNL content
- Clear button to reset form (preserves description)
- Status bar with operation feedback
- Error handling and validation
- Clean white background with black text for readability

### Technical
- Python 3.14
- PyQt6 for GUI
- pandas for Excel reading
- openpyxl for Excel format support
- PyInstaller for EXE creation
- Version management system

---

## [Unreleased]

### Planned for v1.1.0
- Word document (.docx, .doc) support
- Batch file conversion
- Settings persistence (remember last used values)
- Export/import settings profiles
- Dark mode theme option
- Multi-language support (French/Arabic)

### Future Ideas
- Drag and drop file support
- Recent files list
- File validation before conversion
- Excel template download
- Automatic backup of UNL files
- Email integration to send UNL files

---

## Version Numbering

This project uses Semantic Versioning:
- **MAJOR.MINOR.PATCH** (e.g., 1.0.0)
- **MAJOR**: Breaking changes (v2.0.0)
- **MINOR**: New features, backward compatible (v1.1.0)
- **PATCH**: Bug fixes, backward compatible (v1.0.1)
