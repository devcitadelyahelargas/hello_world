import PyQt6.QtWidgets
import PyQt6.QtGui

from functools import partial

from PyQt6.QtWidgets import QMainWindow
from hello_world import Ui_MainWindow


class MainWidget():
    def __init__(self):

        self.main_window = QMainWindow()
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self.main_window)
        self.main_window.setWindowTitle("Hello World")
        self._ui.hello_world_button.clicked.connect(partial(self._hello_world_func, "hello world"))
        self._ui.checkBox.stateChanged.connect(self._hide_or_show_button_by_checkbox)
        self._ui.pushButton.clicked.connect(self._print)

    def _hello_world_func(self, text):
        self._ui.label_to_edit.setText(text)

    def _hide_or_show_button_by_checkbox(self):
        if self._ui.checkBox.isChecked():
            self._ui.hello_world_button.hide()
        else:
            self._ui.hello_world_button.show()
        print(self._curr_text)

    def _print(self):
        self._ui.lineEdit.setText("asafsdfasdfasd123")
