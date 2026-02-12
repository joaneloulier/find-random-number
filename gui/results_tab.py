from PySide6.QtWidgets import QWidget, QLabel, QGridLayout, QVBoxLayout, QPushButton
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from .signals import AppSignals


class ResultsTab(QWidget):
    def __init__(self, stack):
        super().__init__(stack)
        self.stack = stack

        AppSignals.instance().NumberOfTriesSignal.connect(self.get_number_of_tries)
        grid = QGridLayout(self)

        label = QLabel()
        pixmap = QPixmap("gui/images/feu_artifices.png")
        if pixmap.isNull():
            print("Image non trouvée")
        label.setPixmap(pixmap)

        texts = QVBoxLayout()

        label_texte = QLabel("Bravo ! Vous avez trouvé le bon nombre !")
        self.label_tries = QLabel("Il vous aura fallu 0 tentatives")

        BtnRetry = QPushButton("Rejouer")
        BtnRetry.clicked.connect(self.go_to_first_tab)

        texts.addWidget(label_texte, alignment=Qt.AlignCenter)
        texts.addWidget(self.label_tries, alignment=Qt.AlignCenter)
        texts.addSpacing(40)
        texts.addWidget(BtnRetry, alignment=Qt.AlignCenter)

        grid.addWidget(label, 0, 0, Qt.AlignCenter)
        grid.addLayout(texts, 0, 0, Qt.AlignCenter)

    def get_number_of_tries(self, number_of_tries: int):
        self.label_tries.setText(f"Il vous aura fallu {number_of_tries} tentatives.")

    def go_to_first_tab(self):
        self.stack.setCurrentIndex(0)
