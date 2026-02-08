from PySide6.QtWidgets import QWidget

"""
Classe qui va me servir à faire le pont entre l'interface et le backend.

1. Dès que le username clique sur commencer le jeu, le jeu est lancé, 
le backend envoie le nombre à deviner.
2. le worker récupère le nombre devine et utilise les fcts du backend pour
savoir si c'est le bon et lance les messages en fonction de si le nombre
est plus ou plus petit.

"""
class Worker(QWidget):
    def __init__(self):
        super().__init__()

        AppSignals.instance().