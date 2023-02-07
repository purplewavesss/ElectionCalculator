import sys
import qdarkstyle
from PyQt5 import QtWidgets
from MainWindow import MainWindow
from Settings import Settings
from triggers import implement_triggers


def main():
    # Initialize settings
    settings = Settings()

    # Initialize windows/apps
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow(settings)

    # Implement triggers
    implement_triggers(window, settings)

    # Set stylesheet
    app.setStyleSheet(qdarkstyle.load_stylesheet())

    # Open window
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
