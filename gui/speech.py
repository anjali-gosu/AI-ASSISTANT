# gui/speech.py

from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QFont

from gui.theme import *


class SpeechBubble(QLabel):

    def __init__(self, title, parent=None):
        super().__init__(parent)

        self.title = title
        self.full_text = ""
        self.current_index = 0

        self.setAlignment(Qt.AlignCenter)
        self.setWordWrap(True)

        self.setFont(QFont(FONT, MESSAGE_FONT))

        self.setStyleSheet(f"""
            QLabel{{
                color:white;
                background-color:rgba(0,20,40,180);
                border:2px solid {PRIMARY};
                border-radius:18px;
                padding:15px;
            }}
        """)

        self.hide()

        # Typing Timer
        self.typing_timer = QTimer()
        self.typing_timer.timeout.connect(self.type_next)

        # Auto Hide Timer
        self.hide_timer = QTimer()
        self.hide_timer.setSingleShot(True)
        self.hide_timer.timeout.connect(self.hide)

    # -----------------------
    # Show Animated Text
    # -----------------------

    def show_message(self, text):

        self.full_text = text

        self.current_index = 0

        self.setText(f"{self.title}\n")

        self.show()

        self.typing_timer.start(25)

    # -----------------------
    # Typing Effect
    # -----------------------

    def type_next(self):

        if self.current_index < len(self.full_text):

            self.current_index += 1

            self.setText(
                f"{self.title}\n\n"
                f"{self.full_text[:self.current_index]}"
            )

        else:

            self.typing_timer.stop()

            # Hide after 5 seconds
            self.hide_timer.start(5000)