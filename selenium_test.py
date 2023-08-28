import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")

        self.button = QPushButton("Open Second Window", self)
        self.button.clicked.connect(self.open_second_window)

    def open_second_window(self):
        self.second_window = SecondWindow()
        self.second_window.show()


class SecondWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Second Window")

        self.label = QLabel("This is the second window.", self)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec())
