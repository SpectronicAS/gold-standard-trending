#from db.db import engine
#from db.models import Base
from gui.gui import MainWindow, app



window = MainWindow()
window.show()

app.exec()


#Base.metadata.create_all(bind=engine)