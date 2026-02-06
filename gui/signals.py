"""
Centralisation des signaux pour la communication entre frontend et backend.
"""

from PySide6.QtCore import QObject, Signal
from PySide6.QtGui import QPixmap



class AppSignals(QObject):
    


    _instance = None

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
 