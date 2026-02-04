from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QGraphicsOpacityEffect


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Trouve le nombre")
        self.resize(640, 436)

        central = QWidget()
        self.setCentralWidget(central)

        layout = QVBoxLayout(central)

        main_widget = QWidget()
        layout.addWidget(main_widget)

        main_widget.setStyleSheet("""
        QWidget {
            background-color: rgba(255, 255, 255, 128);
            margin: 40;
        }
        """)
