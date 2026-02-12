from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QHBoxLayout,
    QPushButton,
)
from .signals import AppSignals

from PySide6.QtCore import Qt


class GameTab(QWidget):
    def __init__(self, stack):
        super().__init__(stack)
        AppSignals.instance().UsernameSignal.connect(self.get_username)
        AppSignals.instance().ComparisonGuessSol.connect(self.show_result)
        AppSignals.instance().SolutionFoundSignal.connect(self._go_to_next_tab)
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

    def show_result(self, comparison_signal: str):
        if comparison_signal == "lower":
            self.results_label.setText(
                "MAUVAISE REPONSE : Le nombre cherché est plus grand."
            )
        elif comparison_signal == "higher":
            self.results_label.setText(
                "MAUVAISE REPONSE : Le nombre cherché est plus petit."
            )

    def _game_card(self):
        widget = QWidget()
        game_layout = QVBoxLayout(widget)

        self.label = QLabel("En attente du joueur...")
        self.label.setAlignment(Qt.AlignCenter)
        game_layout.addWidget(self.label)

        self.results_label = QLabel(" ")
        self.results_label.setAlignment(Qt.AlignCenter)
        game_layout.addWidget(self.results_label)

        self.guess = QLineEdit()
        game_layout.addWidget(self.guess, alignment=Qt.AlignCenter)
        self.guess.returnPressed.connect(self.on_btnValidate_clicked)

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
            AppSignals.instance().GuessSignal.emit(guess)
            self.guess.clear()

        except Exception:
            self.guess.clear()

    def on_btnCancel_clicked(self):
        self.guess.clear()

    def _go_to_next_tab(self):
        self.stack.setCurrentIndex(2)
