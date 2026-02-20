"""
Centralisation des signaux pour la communication entre frontend et backend.
"""

from PySide6.QtCore import QObject, Signal


class AppSignals(QObject):
    UsernameSignal = Signal(str)
    GuessSignal = Signal(int)
    ComparisonGuessSol = Signal(
        str
    )  # lower si le guess est plus petit que la sol, higher sinon.
    SolutionFoundSignal = Signal()
    NumberOfTriesSignal = Signal(int)
    ReplaySignal = Signal()

    _instance = None

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
