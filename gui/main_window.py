from PySide6.QtWidgets import QMainWindow, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Trouve le nombre")
        self.resize(640, 436)
