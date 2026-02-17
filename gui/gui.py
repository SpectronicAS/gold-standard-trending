import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog, QDialogButtonBox, QLineEdit, QListWidget, QPushButton, QGridLayout, QHBoxLayout, QVBoxLayout, QLabel, QWidget



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Monthly Bio-Cal Tracker")
        self.setFixedSize(QSize(1200, 700))

        layout1 = QHBoxLayout()
        layout2 = QVBoxLayout()
        layout3 = QGridLayout()
        layout4 = QGridLayout()

        addBtn = QPushButton("Add Cal")
        delBtn = QPushButton("Delete Cal")
        editBtn = QPushButton("Edit Cal")
        calcBtn = QPushButton("Calculate Stats")

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

        self.setWindowTitle("Add BioCal Results")

        QBtn = (
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        )


        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()