#from db.db import engine
#from db.models import Base
from gui.gui import MainWindow
from logic.calcert import calcert

def main():
    backend = calcert
    window = MainWindow(backend)
    window.show()

main()



#Base.metadata.create_all(bind=engine)