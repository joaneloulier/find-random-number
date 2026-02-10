from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLineEdit,
    QLabel,
    QHBoxLayout,
    QPushButton,
)

from PySide6.QtCore import Qt, Signal
from .signals import AppSignals

import time


class LoginTab(QWidget):
    def __init__(self, stack):
        super().__init__(stack)
        self.stack = stack
        layout = QVBoxLayout(self)
        layout.setSpacing(40)
        layout.addStretch()
        layout.addWidget(self._username_card())
        layout.addStretch()

    def _username_card(self):
        widget = QWidget()

        pseudo_layout = QVBoxLayout(widget)
        label = QLabel("Entre ton nom pour pouvoir jouer :")
        label.setAlignment(Qt.AlignCenter)
        pseudo_layout.addWidget(label)

        self.username = QLineEdit()

        pseudo_layout.setSpacing(30)
        pseudo_layout.addWidget(self.username, alignment=Qt.AlignCenter)

        btnCancel = QPushButton("Annuler")
        btnCancel.clicked.connect(self.on_btnCancel_clicked)

        btnValidate = QPushButton("Valider")
        btnValidate.clicked.connect(self.on_btnValidate_clicked)
        self.username.returnPressed.connect(self.on_btnValidate_clicked)

        # btnGoToResults = QPushButton("Tab Results")
        # btnGoToResults.clicked.connect(self._tab_results)

        btn_box = QHBoxLayout()
        btn_box.addStretch()
        btn_box.addWidget(btnCancel)
        btn_box.addSpacing(20)
        btn_box.addWidget(btnValidate)
        btn_box.addStretch()
        # btn_box.addWidget(btnGoToResults)

        pseudo_layout.addLayout(btn_box)

        return widget

    def on_btnValidate_clicked(self):
        username = self.username.text()
        print(username)
        AppSignals.instance().UsernameSignal.emit(username)
        self.stack.setCurrentIndex(1)

    def on_btnCancel_clicked(self):
        self.username.clear()

    def _tab_results(self):
        self.stack.setCurrentIndex(2)
