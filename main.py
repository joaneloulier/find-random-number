import sys
from pathlib import Path

from PySide6.QtWidgets import QApplication
from gui.main_window import MainWindow

app = QApplication(sys.argv)
qss_file = Path(__file__).parent / "gui/styles.qss"
with open(qss_file, "r") as f:
    app.setStyleSheet(f.read())
window = MainWindow()
window.show()
sys.exit(app.exec())
