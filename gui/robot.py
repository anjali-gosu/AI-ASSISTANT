# gui/robot.py

from PySide6.QtWidgets import QLabel
from PySide6.QtCore import QTimer, Qt
from PySide6.QtGui import QPixmap

from gui.theme import ROBOT_SIZE


class RobotWidget(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Load Robot Image
        self.pixmap = QPixmap("assets/robot.png")

        if not self.pixmap.isNull():
            self.setPixmap(
                self.pixmap.scaled(
                    ROBOT_SIZE,
                    ROBOT_SIZE,
                    Qt.KeepAspectRatio,
                    Qt.SmoothTransformation
                )
            )

        self.setStyleSheet("background: transparent;")

        # Walking variables
        self.direction = 1
        self.speed = 3
        self.walking = True

        # Animation timer (60 FPS)
        self.timer = QTimer()
        self.timer.timeout.connect(self.walk)
        self.timer.start(16)

    # -------------------------
    # Walking Animation
    # -------------------------
    def walk(self):

        if not self.walking:
            return

        x = self.x() + self.direction * self.speed

        parent = self.parentWidget()

        if parent:

            # Bounce from left/right edges
            if x < 20:
                self.direction = 1

            elif x + self.width() > parent.width() - 20:
                self.direction = -1

            self.move(x, self.y())

    # -------------------------
    # Robot States
    # -------------------------

    def start_walk(self):
        self.walking = True

    def stop_walk(self):
        self.walking = False

    def listening(self):
        self.stop_walk()

    def thinking(self):
        self.stop_walk()

    def speaking(self):
        self.stop_walk()

    def idle(self):
        self.start_walk()