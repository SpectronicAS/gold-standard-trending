from db.db import engine
from db.models import Base
from gui.gui import MainWindow
from PyQt6.QtWidgets import QApplication
import sys

def main():
    Base.metadata.create_all(bind=engine)
    app = QApplication(sys.argv)

    window = MainWindow()

    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
