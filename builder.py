import sys

from PyQt6.QtWidgets import QApplication

from main_widget import MainWidget


def build_main_window():
    # init main window and application
    app = QApplication(sys.argv)
    widget = MainWidget()

    # show the window

    widget.main_window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    build_main_window()


