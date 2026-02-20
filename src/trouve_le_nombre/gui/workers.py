from PySide6.QtWidgets import QWidget

"""
Classe qui va me servir à faire le pont entre l'interface et le backend.

1. Dès que le username clique sur commencer le jeu, le jeu est lancé, 
le backend envoie le nombre à deviner.
2. le worker récupère le nombre devine et utilise les fcts du backend pour
savoir si c'est le bon et lance les messages en fonction de si le nombre
est plus ou plus petit.

Pourquoi j'ai encore tant de mal avec les imports ?? ENFER.

"""

from .signals import AppSignals
from backend import backend


class Worker(QWidget):
    def __init__(self):
        super().__init__()
        AppSignals.instance().GuessSignal.connect(self.on_guess_received)
        AppSignals.instance().ReplaySignal.connect(self.generate_number_from_backend)
        self.generate_number_from_backend()

    def generate_number_from_backend(self):
        """Function used when the worker is initialized, ie the main_window
        initialized and when the user clicks on the button Rejouer from the
        ResultsTab.
        Sets the counter back to 0 and generates a new solution.
        """
        self.solution = backend.generate_number()
        self.compteur = 0

    def on_guess_received(self, guess: int):
        self.compteur += 1
        if backend.correct_answer(self.solution, guess):
            AppSignals.instance().SolutionFoundSignal.emit()
            AppSignals.instance().NumberOfTriesSignal.emit(self.compteur)
        else:
            if backend.guess_lower_than_sol(self.solution, guess):
                AppSignals.instance().ComparisonGuessSol.emit("lower")
            else:
                AppSignals.instance().ComparisonGuessSol.emit("higher")
