from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QComboBox, QMainWindow, QDialog, QDialogButtonBox, QLineEdit, QPushButton, QGridLayout, QHBoxLayout, QVBoxLayout, QLabel, QWidget, QFileDialog, QTableWidget, QTableWidgetItem, QAbstractItemView
from db.crud import add_cal, edit_cal, delete_cal, query_cals, query_data
from logic.calcert import Calcert
import pyqtgraph as pg
from logic.stats import calc_stats, get_results

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
        self.searchBtn = QPushButton("Search")

        self.table = QTableWidget()
        self.setup_table()
        self.populate_table()

        self.plot_wls = pg.PlotWidget()
        self.plot_abs = pg.PlotWidget()
        
        self.set_plots()

        layout1.addWidget(self.table)
        
        layout1.addLayout(layout2)

        layout3.addWidget(self.addBtn, 0, 0)
        layout3.addWidget(self.delBtn, 0, 1)


        layout2.addWidget(self.plot_wls)
        layout2.addWidget(self.plot_abs)
        layout2.addLayout(layout3)
        layout2.addSpacing(20)
        layout4.addWidget(self.inputLine)
        layout4.addWidget(self.searchBtn)
        layout2.addLayout(layout4)
        


        widget = QWidget()
        widget.setLayout(layout1)
        self.setCentralWidget(widget)
    
    def set_plots(self):
        x = len(calc_stats(get_results())[0])
        self.plot_wls.showGrid(x=True, y=True)
        self.plot_wls.setBackground("w")
        self.plot_wls.setXRange(0, x)

        self.plot_abs.showGrid(x=True, y=True)
        self.plot_abs.setBackground("w")
        self.plot_abs.setXRange(0, x)

    def plot_graph(self, graph, x, y, pen, brush):
        graph.plot(x , y, pen=pen, symbol="+", symbolSize=15, symbolBrush=brush)

    def new_cal(self):
        dlg = BioCalDialog(self)
        if dlg.exec():
            data = dlg.get_data()
            calcert = Calcert(data, dlg.combobox.currentText())
            add_cal(calcert.return_dict())
            self.set_plots()          
            self.populate_table()
            plot_data = calc_stats(get_results())
            count = 1
            temp = 1
            points = []
            while temp <= len(plot_data[0]):
                points.append(temp)
                temp = temp + 1
            for dat in plot_data:
                match count:
                    case 1 | 2 | 3 | 4 | 5 :
                        pen = pg.mkPen(color=(0,0,255))
                        self.plot_graph(self.plot_wls, points, dat, pen, "r")
                        count = count + 1
                    case 11 | 12 | 13 | 14 | 15:
                        pen = pg.mkPen(color=(255,0,0))
                        self.plot_graph(self.plot_wls, points, dat, pen, "b")
                        count = count + 1
                    case 6 | 7 | 8 | 9 | 10 :
                        pen = pg.mkPen(color=(0,0,255))
                        self.plot_graph(self.plot_abs, points, dat, pen, "r")
                        count = count + 1
                    case 16 | 17 | 18 | 19 | 20:
                        pen = pg.mkPen(color=(255,0,0))
                        self.plot_graph(self.plot_abs, points, dat, pen, "b")
                        count = count + 1

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
            self.set_plots()
    
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
        self.absLocation.setPlaceholderText("Enter File Location of Abs Sample")
        btn = QPushButton()
        btn2 = QPushButton()
        label = QLabel("Add Bio-Cal Results:")
        label.setStyleSheet("font-weight:bold; font-size: 18px")
        self.combobox = QComboBox()
        self.combobox.addItems(["MRB", "MFB", "AS"])

        layout1.addWidget(label)
        layout1.addStretch(20)
        
        layout1.addWidget(self.combobox)
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
