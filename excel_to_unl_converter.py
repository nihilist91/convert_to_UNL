"""
Excel/Word to UNL Converter - Desktop Application
Converts Excel or Word virement files to UNL format
"""
import sys
import os
from datetime import datetime
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QLabel, QLineEdit, QPushButton, 
                             QFileDialog, QTextEdit, QGroupBox, QGridLayout,
                             QMessageBox, QFrame, QDateEdit)
from PyQt6.QtCore import Qt, QDate
from PyQt6.QtGui import QFont, QIcon
import pandas as pd
from docx import Document
from version import __version__, __app_name__


class ExcelToUNLConverter(QMainWindow):
    def __init__(self):
        super().__init__()
        self.input_file = None
        self.output_data = []
        self.init_ui()
        
    def init_ui(self):
        """Initialize the user interface"""
        self.setWindowTitle(f"{__app_name__} v{__version__}")
        self.setGeometry(100, 100, 900, 700)
        
        # Create central widget and main layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setSpacing(15)
        main_layout.setContentsMargins(20, 20, 20, 20)
        
        # Title
        title_label = QLabel("📄 Excel/Word to UNL File Converter")
        title_font = QFont()
        title_font.setPointSize(16)
        title_font.setBold(True)
        title_label.setFont(title_font)
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(title_label)
        
        # File selection section
        file_group = self.create_file_selection_group()
        main_layout.addWidget(file_group)
        
        # Header information section
        header_group = self.create_header_input_group()
        main_layout.addWidget(header_group)
        
        # Action buttons
        button_layout = self.create_action_buttons()
        main_layout.addLayout(button_layout)
        
        # Preview section
        preview_group = self.create_preview_group()
        main_layout.addWidget(preview_group)
        
        # Developer credit footer
        footer_label = QLabel(f"Developed by: CHAARAOUI MOHAMMED | 0659226281 | Version {__version__}")
        footer_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        footer_font = QFont()
        footer_font.setPointSize(9)
        footer_font.setItalic(True)
        footer_label.setFont(footer_font)
        footer_label.setStyleSheet("color: #666666; padding: 5px;")
        main_layout.addWidget(footer_label)
        
        # Status bar
        self.statusBar().showMessage("Ready")
        
        # Apply stylesheet
        self.apply_stylesheet()
        
    def create_file_selection_group(self):
        """Create file selection group"""
        group = QGroupBox("📁 File Selection")
        layout = QHBoxLayout()
        
        self.file_label = QLabel("No file selected")
        self.file_label.setStyleSheet("padding: 5px; background-color: #f0f0f0; border-radius: 3px;")
        
        self.browse_btn = QPushButton("Browse Excel/Word File")
        self.browse_btn.clicked.connect(self.browse_file)
        self.browse_btn.setMinimumHeight(35)
        
        layout.addWidget(self.file_label, 3)
        layout.addWidget(self.browse_btn, 1)
        
        group.setLayout(layout)
        return group
        
    def create_header_input_group(self):
        """Create header information input group"""
        group = QGroupBox("📝 Header Information")
        layout = QGridLayout()
        layout.setSpacing(10)
        
        # Input fields with labels
        fields = [
            ("File Name:", "nom_fic", "text"),
            ("Description:", "des_fic", "text"),
            ("Generation Date (DD/MM/YYYY):", "dat_gen", "date"),
            ("Sender Code:", "cod_emet", "text"),
            ("Destination Code:", "cod_dest", "text"),
            ("Remittance Number:", "n_remise", "text"),
            ("User Name:", "utilisateur", "text"),
            ("Phone Number:", "telephone", "text")
        ]
        
        self.inputs = {}
        
        for i, field_info in enumerate(fields):
            label_text = field_info[0]
            field_name = field_info[1]
            field_type = field_info[2]
            
            label = QLabel(label_text)
            label.setMinimumWidth(200)
            
            # Create date picker for date field, regular input for others
            if field_type == "date":
                input_field = QDateEdit()
                input_field.setCalendarPopup(True)  # Show calendar popup
                input_field.setDisplayFormat("dd/MM/yyyy")  # Display format
                input_field.setDate(QDate.currentDate())  # Set to today
                input_field.setMinimumHeight(30)
                # Connect date change to update description
                input_field.dateChanged.connect(self.update_description_from_date)
                # Connect date change to update filename
                input_field.dateChanged.connect(self.update_filename)
            else:
                input_field = QLineEdit()
                input_field.setMinimumHeight(30)
                
                # Set default values for text fields
                if field_name == "cod_emet":
                    input_field.setText("10")
                    # Connect sender code change to update filename
                    input_field.textChanged.connect(self.update_filename)
                elif field_name == "cod_dest":
                    input_field.setText("1050")
                    # Connect destination code change to update filename
                    input_field.textChanged.connect(self.update_filename)
                elif field_name == "n_remise":
                    input_field.setText("0001")
                    # Connect remittance number change to update filename
                    input_field.textChanged.connect(self.update_filename)
                elif field_name == "des_fic":
                    # Set initial description based on current date
                    input_field.setText(f"ov {QDate.currentDate().toString('dd/MM/yyyy')}")
                
            self.inputs[field_name] = input_field
            
            layout.addWidget(label, i, 0)
            layout.addWidget(input_field, i, 1)
        
        # Initialize filename after all fields are created
        self.update_filename()
        
        group.setLayout(layout)
        return group
        
    def create_action_buttons(self):
        """Create action buttons"""
        layout = QHBoxLayout()
        layout.setSpacing(10)
        
        self.convert_btn = QPushButton("🔄 Convert to UNL")
        self.convert_btn.clicked.connect(self.convert_to_unl)
        self.convert_btn.setMinimumHeight(40)
        self.convert_btn.setEnabled(False)
        
        self.save_btn = QPushButton("💾 Save UNL File")
        self.save_btn.clicked.connect(self.save_unl)
        self.save_btn.setMinimumHeight(40)
        self.save_btn.setEnabled(False)
        
        self.clear_btn = QPushButton("🗑️ Clear")
        self.clear_btn.clicked.connect(self.clear_all)
        self.clear_btn.setMinimumHeight(40)
        
        layout.addWidget(self.convert_btn)
        layout.addWidget(self.save_btn)
        layout.addWidget(self.clear_btn)
        
        return layout
        
    def create_preview_group(self):
        """Create preview group"""
        group = QGroupBox("👁️ Preview")
        layout = QVBoxLayout()
        
        self.preview_text = QTextEdit()
        self.preview_text.setReadOnly(True)
        self.preview_text.setMinimumHeight(200)
        self.preview_text.setFont(QFont("Courier New", 9))
        
        layout.addWidget(self.preview_text)
        group.setLayout(layout)
        return group
        
    def apply_stylesheet(self):
        """Apply modern stylesheet"""
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f5f5f5;
            }
            QGroupBox {
                font-weight: bold;
                border: 2px solid #cccccc;
                border-radius: 5px;
                margin-top: 10px;
                padding-top: 10px;
                background-color: white;
                color: #000000;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px 0 5px;
                color: #000000;
            }
            QLabel {
                color: #000000;
                background-color: transparent;
            }
            QPushButton {
                background-color: #0078d4;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 8px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #005a9e;
            }
            QPushButton:pressed {
                background-color: #004578;
            }
            QPushButton:disabled {
                background-color: #cccccc;
                color: #666666;
            }
            QLineEdit {
                border: 1px solid #cccccc;
                border-radius: 3px;
                padding: 5px;
                background-color: white;
                color: #000000;
            }
            QLineEdit:focus {
                border: 2px solid #0078d4;
            }
            QDateEdit {
                border: 1px solid #cccccc;
                border-radius: 3px;
                padding: 5px;
                background-color: white;
                color: #000000;
            }
            QDateEdit:focus {
                border: 2px solid #0078d4;
            }
            QDateEdit::drop-down {
                border: none;
                background-color: #0078d4;
                width: 20px;
                border-top-right-radius: 3px;
                border-bottom-right-radius: 3px;
            }
            QDateEdit::down-arrow {
                image: none;
                border-left: 4px solid transparent;
                border-right: 4px solid transparent;
                border-top: 6px solid white;
                width: 0px;
                height: 0px;
            }
            QCalendarWidget {
                background-color: white;
                color: #000000;
            }
            QCalendarWidget QToolButton {
                color: #000000;
                background-color: white;
                border: 1px solid #cccccc;
                border-radius: 3px;
                padding: 5px;
            }
            QCalendarWidget QToolButton:hover {
                background-color: #0078d4;
                color: white;
            }
            QCalendarWidget QMenu {
                background-color: white;
                color: #000000;
            }
            QCalendarWidget QSpinBox {
                background-color: white;
                color: #000000;
                border: 1px solid #cccccc;
            }
            QCalendarWidget QWidget#qt_calendar_navigationbar {
                background-color: #0078d4;
            }
            QCalendarWidget QAbstractItemView {
                selection-background-color: #0078d4;
                selection-color: white;
                color: #000000;
                background-color: white;
            }
            QTextEdit {
                border: 1px solid #cccccc;
                border-radius: 3px;
                background-color: #fafafa;
                color: #000000;
            }
            QStatusBar {
                color: #000000;
            }
            QMessageBox {
                background-color: white;
                color: #000000;
            }
            QMessageBox QLabel {
                color: #000000;
                background-color: white;
            }
            QMessageBox QPushButton {
                background-color: #0078d4;
                color: white;
                border: none;
                border-radius: 3px;
                padding: 6px 20px;
                min-width: 60px;
            }
            QMessageBox QPushButton:hover {
                background-color: #005a9e;
            }
        """)
    
    def update_description_from_date(self, date):
        """Update description field when date changes"""
        date_str = date.toString("dd/MM/yyyy")
        self.inputs['des_fic'].setText(f"ov {date_str}")
    
    def update_filename(self):
        """Update filename based on date and remittance number"""
        # Get date from date picker
        date_obj = self.inputs['dat_gen'].date()
        # Format: DDMMYY (reverse of the actual date format)
        day = date_obj.toString("dd")
        month = date_obj.toString("MM")
        year = date_obj.toString("yy")
        date_part = f"{day}{month}{year}"  # e.g., "161025" for 16/10/2025
        
        # Get remittance number (should be 4 digits, use 0000 if empty)
        remise = self.inputs['n_remise'].text().strip()
        if not remise:
            remise = "0000"
        else:
            remise = remise.zfill(4)  # Pad with zeros to 4 digits
        
        # Get sender and destination codes (use empty if not set)
        cod_emet = self.inputs['cod_emet'].text().strip()
        cod_dest = self.inputs['cod_dest'].text().strip()
        
        # Format: bvov + cod_emet + cod_dest + 00000 + date (DDMMYY) + remise
        # Example: bvov10105000002510160001
        # If fields are empty: bvov000000000000000000000
        filename = f"bvov{cod_emet}{cod_dest}0000{date_part}{remise}.unl"
        
        self.inputs['nom_fic'].setText(filename)
        
    def browse_file(self):
        """Browse for Excel or Word file"""
        file_name, _ = QFileDialog.getOpenFileName(
            self,
            "Select Excel or Word File",
            "",
            "Office Files (*.xlsx *.xls *.docx *.doc);;Excel Files (*.xlsx *.xls);;Word Files (*.docx *.doc);;All Files (*)"
        )
        
        if file_name:
            self.input_file = file_name
            self.file_label.setText(os.path.basename(file_name))
            self.convert_btn.setEnabled(True)
            self.statusBar().showMessage(f"File loaded: {os.path.basename(file_name)}")
                
    def convert_to_unl(self):
        """Convert Excel or Word to UNL format"""
        if not self.input_file:
            QMessageBox.warning(self, "Warning", "Please select a file first!")
            return
            
        # Validate inputs
        required_fields = ['nom_fic', 'des_fic', 'dat_gen', 'cod_emet', 
                          'cod_dest', 'n_remise', 'utilisateur', 'telephone']
        
        for field in required_fields:
            if field == 'dat_gen':
                # Date field is always valid (QDateEdit always has a date)
                continue
            if not self.inputs[field].text().strip():
                QMessageBox.warning(self, "Warning", f"Please fill in all required fields!")
                return
        
        try:
            # Determine file type and extract data
            file_ext = os.path.splitext(self.input_file)[1].lower()
            
            if file_ext in ['.xlsx', '.xls']:
                # First detect format
                df = pd.read_excel(self.input_file, header=None)
                detected_format = self.detect_excel_format(df)
                
                if detected_format:
                    self.statusBar().showMessage(f"Detected format: {detected_format}. Processing...")
                
                data_rows = self.extract_from_excel()
            elif file_ext in ['.docx', '.doc']:
                data_rows = self.extract_from_word()
            else:
                QMessageBox.critical(self, "Error", "Unsupported file format!")
                return
            
            if not data_rows:
                QMessageBox.critical(self, "Error", "No valid data found in file!")
                return
            
            # Generate UNL content
            self.generate_unl_content(data_rows)
            
            self.save_btn.setEnabled(True)
            format_info = f" (Format: {detected_format})" if file_ext in ['.xlsx', '.xls'] and detected_format else ""
            self.statusBar().showMessage(f"Conversion successful! {len(data_rows)} records processed{format_info}")
            QMessageBox.information(self, "Success", 
                                  f"Conversion completed successfully!\n{len(data_rows)} records processed{format_info}")
            
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred during conversion:\n{str(e)}")
            self.statusBar().showMessage("Conversion failed!")
    
    def extract_from_excel(self):
        """Extract data from Excel file - supports multiple formats"""
        # Read Excel file
        df = pd.read_excel(self.input_file, header=None)
        
        # Detect file format by searching for known headers
        file_format = self.detect_excel_format(df)
        
        if file_format == 'CNTR':
            return self.extract_cntr_format(df)
        elif file_format == 'BOUDOUR':
            return self.extract_boudour_format(df)
        else:
            raise Exception("Could not detect file format. Supported formats: CNTR (with 'NOM' header) or BOUDOUR format.")
    
    def detect_excel_format(self, df):
        """Detect the format of the Excel file"""
        # Search for CNTR format markers (NOM in column 2)
        for i, row in df.iterrows():
            if pd.notna(row[2]) and str(row[2]).strip().upper() == 'NOM':
                return 'CNTR'
        
        # Search for BOUDOUR format markers
        # Common BOUDOUR headers might be in different columns or have different patterns
        # Check for patterns like: numero, designation, rib, compte, montant, etc.
        for i, row in df.iterrows():
            row_str = ' '.join([str(cell).upper() for cell in row if pd.notna(cell)])
            # Look for common BOUDOUR patterns (added COMPTE, PRÉNOM, DHS)
            if any(keyword in row_str for keyword in ['DESIGNATION', 'BÉNÉFICIAIRE', 'BENEFICIAIRE', 'RIB', 'MONTANT', 'COMPTE', 'PRÉNOM', 'PRENOM', 'DHS']):
                return 'BOUDOUR'
        
        # If no specific format detected, return None
        return None
    
    def extract_cntr_format(self, df):
        """Extract data from CNTR format Excel file"""
        # Find the data section (starts after "NOM" header)
        data_start_row = None
        for i, row in df.iterrows():
            if pd.notna(row[2]) and str(row[2]).strip().upper() == 'NOM':
                data_start_row = i + 1
                break
        
        if data_start_row is None:
            raise Exception("Could not find 'NOM' header in CNTR format file!")
        
        # Extract data rows
        data_rows = []
        for i in range(data_start_row, len(df)):
            row = df.iloc[i]
            # Stop at SOMME row
            if pd.notna(row[1]) and str(row[1]).upper() == 'SOMME':
                break
                
            # Skip if no number in column 1
            if pd.isna(row[1]):
                continue
                
            try:
                num = int(row[1])
                nom = str(row[2]) if pd.notna(row[2]) else ""
                prenom = str(row[3]) if pd.notna(row[3]) else ""
                rib = str(row[4]) if pd.notna(row[4]) else ""
                montant = float(row[6]) if pd.notna(row[6]) else 0.0
                
                # Clean RIB (remove single quotes and spaces)
                rib = rib.replace("'", "").replace(" ", "").strip()
                
                data_rows.append({
                    'num': num,
                    'nom': nom,
                    'prenom': prenom,
                    'rib': rib,
                    'montant': montant
                })
            except (ValueError, TypeError):
                continue
        
        return data_rows
    
    def extract_boudour_format(self, df):
        """Extract data from BOUDOUR format Excel file"""
        # BOUDOUR format typically has headers in the first few rows
        # We need to find the header row and then extract data
        
        header_row = None
        col_mapping = {}
        
        # Search for the header row (contains RIB, MONTANT, etc.)
        for i, row in df.iterrows():
            row_values = [str(cell).upper().strip() if pd.notna(cell) else "" for cell in row]
            
            # Check if this row has headers across MULTIPLE columns (not just one long text)
            # Count non-empty columns
            non_empty_cols = sum(1 for val in row_values if val)
            
            # Count how many columns contain header keywords
            header_cols = sum(1 for val in row_values if any(keyword in val for keyword in [
                'RIB', 'COMPTE', 'MONTANT', 'DHS', 'BÉNÉFICIAIRE', 'BENEFICIAIRE', 'PRÉNOM', 'PRENOM', 'NOM', 'AGENCE'
            ]))
            
            # Consider it a header row if it has:
            # - At least 3 non-empty columns
            # - At least 2 columns with header keywords
            if non_empty_cols >= 3 and header_cols >= 2:
                header_row = i
                
                # Map column positions
                for col_idx, cell_value in enumerate(row_values):
                    if any(rib_key in cell_value for rib_key in ['NUMÉRO DU COMPTE', 'NUMERO DU COMPTE', 'RIB']) and 'NOM' not in cell_value:
                        col_mapping['rib'] = col_idx
                    elif 'MONTANT' in cell_value or ('DHS' in cell_value and 'MONTANT' not in row_values[col_idx-1] if col_idx > 0 else True):
                        col_mapping['montant'] = col_idx
                    elif any(name_key in cell_value for name_key in ['NOM ET PRÉNOM', 'NOM ET PRENOM', 'PRÉNOM', 'PRENOM']) and 'TITULAIRE' not in cell_value and 'COMPTE' not in cell_value:
                        col_mapping['nom'] = col_idx
                    elif any(num_key in cell_value for num_key in ['N°', 'NO']) and 'COMPTE' not in cell_value and 'NUMÉRO' not in cell_value:
                        col_mapping['num'] = col_idx
                
                break
        
        if header_row is None:
            # If no header found, try to auto-detect based on data patterns
            # Assume: first numeric column = num, first long text = name, RIB pattern, last numeric = montant
            return self.extract_boudour_auto_detect(df)
        
        # Extract data starting from next row after header
        data_rows = []
        num_counter = 1  # Counter for rows without explicit number
        
        for i in range(header_row + 1, len(df)):
            row = df.iloc[i]
            
            # Skip empty rows
            if row.isna().all():
                continue
            
            # Check for TOTAL/SOMME row
            row_str = ' '.join([str(cell).upper() for cell in row if pd.notna(cell)])
            if any(keyword in row_str for keyword in ['TOTAL', 'SOMME', 'MONTANT TOTAL']):
                break
            
            try:
                # Extract number (use counter if not in file)
                if 'num' in col_mapping and pd.notna(row[col_mapping['num']]):
                    num = int(row[col_mapping['num']])
                else:
                    num = num_counter
                
                # Extract name
                nom = ""
                prenom = ""
                if 'nom' in col_mapping and pd.notna(row[col_mapping['nom']]):
                    full_name = str(row[col_mapping['nom']]).strip()
                    # Try to split name into nom and prenom
                    name_parts = full_name.split(maxsplit=1)
                    nom = name_parts[0] if len(name_parts) > 0 else ""
                    prenom = name_parts[1] if len(name_parts) > 1 else ""
                
                # Extract RIB
                rib = ""
                if 'rib' in col_mapping and pd.notna(row[col_mapping['rib']]):
                    rib = str(row[col_mapping['rib']]).replace("'", "").replace(" ", "").strip()
                
                # Extract montant
                montant = 0.0
                if 'montant' in col_mapping and pd.notna(row[col_mapping['montant']]):
                    montant_str = str(row[col_mapping['montant']]).replace(",", "").replace(" ", "")
                    montant = float(montant_str)
                
                # Only add row if it has at least a name or RIB
                if nom or rib:
                    data_rows.append({
                        'num': num,
                        'nom': nom,
                        'prenom': prenom,
                        'rib': rib,
                        'montant': montant
                    })
                    num_counter += 1
                    
            except (ValueError, TypeError) as e:
                # Skip rows that can't be parsed
                continue
        
        return data_rows
    
    def extract_boudour_auto_detect(self, df):
        """Auto-detect BOUDOUR format when no clear headers are found"""
        data_rows = []
        num_counter = 1
        
        # Start from first row and try to extract data
        for i, row in df.iterrows():
            # Skip empty rows
            if row.isna().all():
                continue
            
            # Check for TOTAL/SOMME row
            row_str = ' '.join([str(cell).upper() for cell in row if pd.notna(cell)])
            if any(keyword in row_str for keyword in ['TOTAL', 'SOMME', 'MONTANT TOTAL']):
                break
            
            try:
                # Try to find RIB pattern (usually 24 digits)
                rib = ""
                montant = 0.0
                nom = ""
                
                for col_idx, cell_value in enumerate(row):
                    if pd.isna(cell_value):
                        continue
                    
                    cell_str = str(cell_value).replace("'", "").replace(" ", "").strip()
                    
                    # Check if it's a RIB (numeric, 20-24 digits)
                    if cell_str.isdigit() and 20 <= len(cell_str) <= 24:
                        rib = cell_str
                    # Check if it's a montant (numeric with decimals)
                    elif cell_str.replace(".", "", 1).replace(",", "", 1).isdigit():
                        try:
                            montant = float(cell_str.replace(",", ""))
                        except:
                            pass
                    # Otherwise might be a name
                    elif len(cell_str) > 3 and not cell_str.replace(".", "").isdigit():
                        if not nom:  # Take first text field as name
                            nom = cell_str
                
                # Only add if we have meaningful data
                if rib or nom:
                    name_parts = nom.split(maxsplit=1)
                    data_rows.append({
                        'num': num_counter,
                        'nom': name_parts[0] if len(name_parts) > 0 else nom,
                        'prenom': name_parts[1] if len(name_parts) > 1 else "",
                        'rib': rib,
                        'montant': montant
                    })
                    num_counter += 1
                    
            except Exception as e:
                continue
        
        return data_rows
    
    def extract_from_word(self):
        """Extract data from Word file"""
        # TODO: Implement Word extraction logic once user provides real Word format
        # For now, return empty list as placeholder
        raise Exception("Word file support is not yet implemented. Please provide the Word file format.")
            
    def generate_unl_content(self, data_rows):
        """Generate UNL file content"""
        unl_lines = []
        
        # Header section
        unl_lines.append(f"@nom_fic  :{self.inputs['nom_fic'].text()}")
        unl_lines.append(f"@des_fic  :{self.inputs['des_fic'].text()}")
        
        # Get date from QDateEdit widget
        date_obj = self.inputs['dat_gen'].date()
        date_str = date_obj.toString("dd/MM/yyyy")
        unl_lines.append(f"@dat_gen  :{date_str}")
        
        unl_lines.append(f"@cod_emet :{self.inputs['cod_emet'].text()}")
        unl_lines.append(f"@cod_dest :{self.inputs['cod_dest'].text()}")
        unl_lines.append(f"@n_remise :{self.inputs['n_remise'].text()}")
        unl_lines.append(f"@nbr_enr  : {len(data_rows)}")
        unl_lines.append(f"@taille   :")
        unl_lines.append(f"@ utilisateur: {self.inputs['utilisateur'].text()}")
        unl_lines.append(f"@ {self.inputs['telephone'].text()}")
        
        # Parse date for data rows
        day = date_obj.toString("dd")
        month = date_obj.toString("MM")
        year = date_obj.toString("yyyy")
        
        cod_emet = self.inputs['cod_emet'].text()
        
        # Data rows
        for row in data_rows:
            num_str = f"{row['num']:02d}"
            # Combine name and remove extra spaces
            name = f"{row['nom']} {row['prenom']}"
            name = ' '.join(name.split())  # Remove extra spaces
            
            # Format RIB - ensure it's clean (remove quotes and spaces)
            rib = row['rib'].replace("'", "").replace(" ", "").strip()
            
            montant = f"{row['montant']:.2f}"
            
            line = f"{cod_emet}|{year}|{month}|{day}|{num_str}|{name}|{rib}|{montant}|"
            unl_lines.append(line)
        
        # Store output
        self.output_data = unl_lines
        
        # Display preview (first 20 lines)
        preview_lines = unl_lines[:20]
        if len(unl_lines) > 20:
            preview_lines.append(f"\n... and {len(unl_lines) - 20} more lines")
        
        self.preview_text.setPlainText('\n'.join(preview_lines))
        
    def save_unl(self):
        """Save UNL file"""
        if not self.output_data:
            QMessageBox.warning(self, "Warning", "Please convert a file first!")
            return
            
        default_name = self.inputs['nom_fic'].text()
        file_name, _ = QFileDialog.getSaveFileName(
            self,
            "Save UNL File",
            default_name,
            "UNL Files (*.unl);;All Files (*)"
        )
        
        if file_name:
            try:
                with open(file_name, 'w', encoding='utf-8') as f:
                    f.write('\n'.join(self.output_data))
                    f.write('\n')
                
                QMessageBox.information(self, "Success", f"File saved successfully!\n{file_name}")
                self.statusBar().showMessage(f"File saved: {os.path.basename(file_name)}")
                
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to save file:\n{str(e)}")
                
    def clear_all(self):
        """Clear all fields and reset"""
        self.excel_file = None
        self.output_data = []
        self.file_label.setText("No file selected")
        self.preview_text.clear()
        
        # Reset input fields to defaults
        for field_name, input_field in self.inputs.items():
            if field_name == "dat_gen":
                # Reset date picker to today
                input_field.setDate(QDate.currentDate())
            elif field_name == "des_fic":
                # Keep description, don't clear it
                continue
            else:
                # Clear all other fields including codes and remittance
                input_field.clear()
        
        self.convert_btn.setEnabled(False)
        self.save_btn.setEnabled(False)
        self.statusBar().showMessage("Cleared")


def main():
    app = QApplication(sys.argv)
    
    # Set application style
    app.setStyle('Fusion')
    
    window = ExcelToUNLConverter()
    window.show()
    
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
