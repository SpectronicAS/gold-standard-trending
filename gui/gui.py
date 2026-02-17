import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog, QDialogButtonBox, QLineEdit, QListWidget, QPushButton, QGridLayout, QHBoxLayout, QVBoxLayout, QLabel, QWidget, QFileDialog



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Monthly Bio-Cal Tracker")
        self.setFixedSize(QSize(1200, 700))

        layout1 = QHBoxLayout()
        layout2 = QVBoxLayout()
        layout3 = QGridLayout()
        layout4 = QGridLayout()

        addBtn = QPushButton("Add Calibration")
        addBtn.clicked.connect(self.new_cal)
        delBtn = QPushButton("Delete Calibration")
        editBtn = QPushButton("Edit Calibration")
        calcBtn = QPushButton("Calculate Statistics")

        self.inputLine = QLineEdit("")
        self.inputLine.setPlaceholderText("Search Bar")
        searchBtn = QPushButton("Search")

        self.listBox = QListWidget()


        layout1.addWidget(self.listBox)
        layout1.addLayout(layout2)

        layout3.addWidget(addBtn, 0, 0)
        layout3.addWidget(delBtn, 0, 1)
        layout3.addWidget(editBtn, 1,0)
        layout3.addWidget(calcBtn, 1,1)

        layout2.addStretch(1)
        layout2.addLayout(layout3)
        layout2.addSpacing(20)
        layout2.addWidget(self.inputLine)
        layout2.addSpacing(10)
        
        layout4.addWidget(QLabel(""), 0, 0)
        layout4.addWidget(searchBtn,0,1)

        layout2.addLayout(layout4)

        widget = QWidget()
        widget.setLayout(layout1)
        self.setCentralWidget(widget)
    
    def new_cal(self):
        dlg = BioCalDialog(self)
        dlg.exec()


class BioCalDialog(QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)

        self.setWindowTitle("Add Bio-Cal Results")

        QBtn = (
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        )

        layout1 = QVBoxLayout()
        layout2 = QHBoxLayout()
        layout3 = QHBoxLayout()

        self.wlLocation = QLineEdit()
        self.wlLocation.setPlaceholderText("Enter File Location of WL Scan")
        self.absLocation = QLineEdit()
        self.absLocation.setPlaceholderText("Ender File Location of Abs Sample")
        btn = QPushButton()
        btn2 = QPushButton()
        label = QLabel("Add Bio-Cal Results:")
        label.setStyleSheet("font-weight:bold; font-size: 18px")

        layout1.addWidget(label)
        layout1.addStretch(20)
        
        layout2.addWidget(self.wlLocation)
        btn.clicked.connect(self.browse_wl)
        btn.setText("Browse")
        layout2.addWidget(btn)

        layout1.addLayout(layout2)

        layout3.addWidget(self.absLocation)
        btn2.clicked.connect(self.browse_abs)
        btn2.setText("Browse")
        layout3.addWidget(btn2)

        layout1.addLayout(layout3)

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        layout1.addWidget(self.buttonBox)

        widget = QWidget()
        widget.setLayout(layout1)
        self.setLayout(layout1)
        self.setFixedSize(500,300)

    def browse_wl(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select File",
            "",
            "Wavelength Scans (*.sca)"
        )
        if file_path:
            self.wlLocation.setText(file_path)

    def browse_abs(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select File",
            "",
            "Absorbance Samples (*.qua)"
        )
        if file_path:
            self.wlLocation.setText(file_path)
app = QApplication(sys.argv)
