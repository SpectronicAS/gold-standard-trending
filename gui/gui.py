from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog, QDialogButtonBox, QLineEdit, QListWidget, QPushButton, QGridLayout, QHBoxLayout, QVBoxLayout, QLabel, QWidget, QFileDialog, QTableWidget, QTableWidgetItem, QAbstractItemView
from db.crud import add_cal, edit_cal, delete_cal, query_cals, query_data
from logic.calcert import Calcert

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Monthly Bio-Cal Tracker")
        self.setFixedSize(QSize(1200, 700))


        layout1 = QHBoxLayout()
        layout2 = QVBoxLayout()
        layout3 = QGridLayout()
        layout4 = QGridLayout()

        self.addBtn = QPushButton("Add Calibration")
        self.addBtn.clicked.connect(self.new_cal)
        self.delBtn = QPushButton("Delete Calibration")
        self.delBtn.clicked.connect(self.del_cal)
        self.editBtn = QPushButton("Edit Calibration")
        self.calcBtn = QPushButton("Calculate Statistics")

        self.inputLine = QLineEdit("")
        self.inputLine.setPlaceholderText("Search Bar")
        searchBtn = QPushButton("Search")

        self.table = QTableWidget()
        self.setup_table()
        self.populate_table()


        layout1.addWidget(self.table)
        layout1.addLayout(layout2)

        layout3.addWidget(self.addBtn, 0, 0)
        layout3.addWidget(self.delBtn, 0, 1)
        layout3.addWidget(self.editBtn, 1,0)
        layout3.addWidget(self.calcBtn, 1,1)

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
        if dlg.exec():
            data = dlg.get_data()
            calcert = Calcert(data, "mfb")
            add_cal(calcert.return_dict())
            self.populate_table()

    def setup_table(self):
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(
            ["ID", "Created At", "Result"]
        )
        self.table.setEditTriggers(
            QAbstractItemView.EditTrigger.NoEditTriggers
        )

        self.table.setSelectionBehavior(
            QAbstractItemView.SelectionBehavior.SelectRows
        )

        self.table.setSelectionMode(
            QAbstractItemView.SelectionMode.SingleSelection
        )

        self.table.setSortingEnabled(True)

    def populate_table(self):
        rows = query_data()
        self.table.setRowCount(len(rows))
        
        for row_index, row in enumerate(rows):
            self.table.setItem(
                row_index, 0,
                QTableWidgetItem(str(row.id))
            )
            self.table.setItem(
                row_index, 1,
                QTableWidgetItem(
                    row.created_at.strftime("%Y-%m-%d %H:%M")
                )
            )
            self.table.setItem(
                row_index, 2,
                QTableWidgetItem(f"{row.result}")
            )
            self.table.resizeColumnsToContents()

    def model_results(self, wl_results, abs_results):
        result = {}
        for i, value in enumerate(wl_results):
            result[f"wl{i}"] = value
        for i, value in enumerate(abs_results):
            result[f"abs{i}"] = value
        return result

    def del_cal(self):
        row = self.table.currentRow()
        if row < 0:
            return
        else:
            delete_cal(int(self.table.item(row,0).text()))
            self.populate_table()
    
    


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
            self.absLocation.setText(file_path)

    def get_data(self):
        return {
            "wl_file_path": self.wlLocation.text(),
            "abs_file_path": self.absLocation.text()
        }
