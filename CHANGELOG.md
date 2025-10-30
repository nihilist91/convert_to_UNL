# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0] - 2025-10-30

### Added
- **Multi-format Excel support**: Application now automatically detects and processes both CNTR and BOUDOUR format Excel files
- Automatic format detection engine with intelligent column mapping
- Support for BOUDOUR format with flexible header detection
- Auto-detection fallback using pattern recognition for files without clear headers
- Format detection feedback in status messages and success dialogs

### Changed
- `extract_from_excel()` method now includes format detection logic
- Enhanced error messages to indicate supported formats
- Updated USER_GUIDE.md with comprehensive format documentation

### Fixed
- **CRITICAL**: Fixed "Could not find data header in Excel file" error for BOUDOUR format files
- **CRITICAL**: Fixed RIB numbers with spaces not being processed (e.g., "007 323 0009123000301876 32")
- All RIB cleaning now removes both single quotes and spaces consistently across all format handlers
- Application now works with different Excel layouts and column arrangements

### Technical Details
- Added `detect_excel_format()` method to identify file format
- Added `extract_cntr_format()` method for traditional CNTR files
- Added `extract_boudour_format()` method with header keyword detection
- Added `extract_boudour_auto_detect()` method for intelligent pattern-based extraction
- Enhanced RIB cleaning in CNTR format handler to remove spaces (previously only removed quotes)
- Enhanced RIB cleaning in UNL generation to ensure consistency
- RIB pattern detection (20-24 digit validation)
- Flexible amount parsing with comma handling
- Automatic row numbering when numbers not present in file

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
