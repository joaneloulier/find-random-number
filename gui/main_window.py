from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QHBoxLayout,
    QPushButton,
    QStackedWidget,
)



from .game_tab import GameTab
from .login_tab import LoginTab
from PySide6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Trouve le nombre")
        self.resize(640, 436)

        central = QWidget()
        self.setCentralWidget(central)

        layout = QVBoxLayout(central)

        central.setObjectName("central_widget")
        central.setStyleSheet("""
        #central_widget {
            background-color: rgba(255, 255, 255, 128);
            margin: 50px;
        }
        """)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self.stack = QStackedWidget()
        layout.addWidget(self.stack)

        self.login_tab = LoginTab(self.stack)
        self.game_tab = GameTab(self.stack)

        self.stack.addWidget(self.login_tab)
        self.stack.addWidget(self.game_tab)


