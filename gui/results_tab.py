from PySide6.QtWidgets import QWidget, QLabel, QGridLayout
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt


class ResultsTab(QWidget):
    def __init__(self, stack):
        super().__init__(stack)
        self.stack = stack
        grid = QGridLayout(self)

        label = QLabel()
        pixmap = QPixmap("gui/images/feu_artifices.png")
        if pixmap.isNull():
            print("Image non trouvée")
        label.setPixmap(pixmap)

        label_texte = QLabel("Bravo ! Vous avez trouvé le bon nombre !")

        grid.addWidget(label, 0, 0, Qt.AlignCenter)
        grid.addWidget(label_texte, 0, 0, Qt.AlignCenter)
