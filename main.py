import pyautogui as pag
import sys
import time
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
        self.warn_text .setAlignment(Qt.AlignmentFlag(5))
        self.warn_text.setFont(
            QFont("Cascadia Code", pointSize=8))

        layout = QVBoxLayout(self)
        layout.addWidget(self.msg_label)
        layout.addWidget(self.msg_label_input)
        layout.addWidget(self.count_label)
        layout.addWidget(self.count_label_input)
        layout.addWidget(self.start_spam_button,
                         alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.warn_text)
        self.window_settings()

    def window_settings(self):
        self.setWindowTitle('Spamde')
        self.setWindowIcon(QIcon('spamde.png'))
        self.set_taskbar_icon()
        self.setMaximumSize(360, 170)
        self.setMinimumSize(360, 170)

    def set_taskbar_icon(self):
        icon = QIcon(QPixmap('spamde.png'))
        try:
            if (sys.platform == 'win32'):
                import ctypes
                ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(
                    'myappid')
                self.setWindowIcon(icon)
        except:
            pass

    def spam(self):
        try:
            msg = self.msg_label_input.text()
            count = int(self.count_label_input.text())
            time.sleep(4)
            while (count > 0):
                pag.typewrite(msg)
                pag.press('enter')
                count -= 1
        except ValueError:
            self.error_text.setText("Enter a number, you du*b bi**h!")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec())
