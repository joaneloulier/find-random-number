from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QHBoxLayout,
    QPushButton,
)
from .login_tab import LoginTab
from .signals import AppSignals

from PySide6.QtCore import Qt
import time


class GameTab(QWidget):
    def __init__(self, stack):
        super().__init__(stack)
        AppSignals.instance().UsernameSignal.connect(self.get_username)
        self.stack = stack
        layout = QVBoxLayout(self)
        layout.setSpacing(40)
        layout.addStretch()
        layout.addWidget(self._game_card())
        layout.addStretch()

    def get_username(self, username: str):
        self.username = username
        self.label.setText(
            f"Bonjour {self.username} ! Devine un nombre entre 1 et 100."
        )

    def _game_card(self):
        widget = QWidget()
        game_layout = QVBoxLayout(widget)

        # Créer le label avec un texte temporaire, on le met à jour plus tard via le signal
        self.label = QLabel("En attente du joueur...")
        self.label.setAlignment(Qt.AlignCenter)
        game_layout.addWidget(self.label)

        self.guess = QLineEdit()
        game_layout.addWidget(self.guess, alignment=Qt.AlignCenter)

        game_layout.setSpacing(30)
        btnCancel = QPushButton("Annuler")
        btnCancel.clicked.connect(self.on_btnCancel_clicked)

        btnValidate = QPushButton("Valider")
        btnValidate.clicked.connect(self.on_btnValidate_clicked)

        btn_box = QHBoxLayout()
        btn_box.addStretch()
        btn_box.addWidget(btnCancel)
        btn_box.addSpacing(20)
        btn_box.addWidget(btnValidate)
        btn_box.addStretch()

        game_layout.addLayout(btn_box)

        return widget

    def on_btnValidate_clicked(self):
        try:
            guess = int(self.guess.text())
            self.guess.clear()

        except Exception:
            self.guess.clear()
            print("erreur")

    def on_btnCancel_clicked(self):
        self.guess.clear()


"""L'idée ici c'est de rentrer un nombre, puis d'appuyer
sur valider on fait try le nombre Votre essai, valider,
soit c'est un entier, dans ce cas on l'envoei au backend pour
le tester. """

# problème : game card est appelée avant get_username. ça ne fonctionne pas.
# ou peut-être que je réécris ce self.username, remarque je ne pense pas car le pr

# résolution du problème : dès que le signal arrive on change le label = dans get_username
