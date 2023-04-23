import pyautogui as pag
import sys
import time
import threading
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QFont, QPixmap
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.msg_label = QLabel("Enter the message you wanna spam:", self)
        self.msg_label.setAlignment(Qt.AlignmentFlag(5))
        self.msg_label.setFont(QFont("Cascadia Code"))
        self.msg_label_input = QLineEdit(self)
        self.msg_label_input.setAlignment(Qt.AlignmentFlag(5))
        self.msg_label_input.setFont(QFont("Cascadia Code"))

        self.count_label = QLabel(
            "Spam this many times(Only enter a number!):", self)
        self.count_label.setAlignment(Qt.AlignmentFlag(5))
        self.count_label.setFont(QFont("Cascadia Code"))

        self.count_label_input = QLineEdit(self)
        self.count_label_input.setAlignment(Qt.AlignmentFlag(5))
        self.count_label_input.setFont(QFont("Cascadia Code"))

        self.start_spam_button = QPushButton()
        self.start_spam_button.setText("Spamde")
        self.start_spam_button.setFont(QFont("Cascadia Code"))
        self.start_spam_button.clicked.connect(self.spam)

        self.warn_text = QLabel(
            "Quickly open the text area where you want to spam after\n clicking the above button, you'd have 4 seconds!", self)
        self.warn_text.setAlignment(Qt.AlignmentFlag(5))
        self.warn_text.setFont(
            QFont("Cascadia Code", pointSize=8))

        self.error_text = QLabel(" ")
        self.error_text.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.warn_text.setFont(QFont("Cascadia Code", pointSize=8))

        layout = QVBoxLayout(self)
        layout.addWidget(self.msg_label)
        layout.addWidget(self.msg_label_input)
        layout.addWidget(self.count_label)
        layout.addWidget(self.count_label_input)
        layout.addWidget(self.start_spam_button,
                         alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.warn_text)
        layout.addWidget(self.error_text)
        self.window_settings()

    def window_settings(self):
        self.setWindowTitle('Spamde')
        self.setWindowIcon(QIcon('spamde.ico'))
        self.set_taskbar_icon()
        self.adjustSize()

    def set_taskbar_icon(self):
        icon = QIcon(QPixmap('spamde.ico'))
        try:
            if (sys.platform == 'win32'):
                import ctypes
                ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(
                    'myappid')
                self.setWindowIcon(icon)
        except:
            pass

    def spam(self):
        def _spamm():
            try:
                self.start_spam_button.setEnabled(False)
                self.msg = self.msg_label_input.text()
                self.count = int(self.count_label_input.text())
                time.sleep(4)
                while (self.count > 0):
                    pag.typewrite(self.msg)
                    pag.press('enter')
                    self.count -= 1
            except ValueError:
                self.error_text.setText("Enter a number, you du*b bi**h!")
            time.sleep(3)
            self.error_text.setText(" ")
            self.start_spam_button.setEnabled(True)

        self.exec_spam = threading.Thread(target=_spamm)
        self.exec_spam.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec())
