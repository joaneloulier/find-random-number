from PySide6.QtWidgets import QWidget


class ResultsTab(QWidget):
    def __init__(self, stack):
        super().__init__(stack)
        self.stack = stack
