# ==========================================
# Jarvis AI v3
# gui/interface.py
# Part 1
# ==========================================

from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QGraphicsDropShadowEffect
)

from PySide6.QtGui import (
    QColor,
    QPainter,
    QLinearGradient,
    QBrush,
    QPen,
    QFont
)

from PySide6.QtCore import (
    Qt,
    QTimer,
    Signal
)

from gui.theme import *
from gui.robot import RobotWidget
from gui.speech import SpeechBubble


class JarvisGUI(QWidget):

    # Thread Safe Signals
    statusSignal = Signal(str)
    commandSignal = Signal(str)
    responseSignal = Signal(str)

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Jarvis AI v3")

        self.resize(WINDOW_WIDTH, WINDOW_HEIGHT)

        self.setMinimumSize(1200, 700)

        self.setStyleSheet(
            f"""
            QWidget{{
                background:{BACKGROUND};
            }}
            """
        )

        # Connect Signals
        self.statusSignal.connect(self.update_status)
        self.commandSignal.connect(self.update_command)
        self.responseSignal.connect(self.update_response)

        self.build_ui()

        self.start_background_animation()

    # ====================================
    # BUILD UI
    # ====================================

    def build_ui(self):

        self.mainLayout = QVBoxLayout(self)

        self.mainLayout.setContentsMargins(40,40,40,40)

        self.mainLayout.setSpacing(25)

        ###################################
        # STATUS
        ###################################

        self.status = QLabel("STATUS : IDLE")

        self.status.setAlignment(Qt.AlignCenter)

        self.status.setFont(
            QFont(FONT,22,QFont.Bold)
        )

        self.status.setStyleSheet(f"""
        QLabel{{
            color:{PRIMARY};
            background:transparent;
        }}
        """)

        glow = QGraphicsDropShadowEffect()

        glow.setBlurRadius(40)

        glow.setColor(QColor(0,220,255))

        glow.setOffset(0)

        self.status.setGraphicsEffect(glow)

        self.mainLayout.addWidget(self.status)

        ###################################
        # ROBOT AREA
        ###################################

        self.robotContainer = QWidget()

        self.robotLayout = QVBoxLayout(self.robotContainer)

        self.robotLayout.setAlignment(Qt.AlignCenter)

        self.robot = RobotWidget(self)

        self.robotLayout.addWidget(
            self.robot,
            alignment=Qt.AlignCenter
        )

        self.mainLayout.addWidget(
            self.robotContainer,
            stretch=1
        )

        ###################################
        # USER BUBBLE
        ###################################

        self.userBubble = SpeechBubble("👤 YOU")

        self.userBubble.setFixedWidth(600)

        self.mainLayout.addWidget(
            self.userBubble,
            alignment=Qt.AlignCenter
        )

        ###################################
        # AI BUBBLE
        ###################################

        self.aiBubble = SpeechBubble("🤖 JARVIS")

        self.aiBubble.setFixedWidth(600)

        self.mainLayout.addWidget(
            self.aiBubble,
            alignment=Qt.AlignCenter
        )

        self.mainLayout.addStretch()

    # ====================================
    # BACKGROUND ANIMATION
    # ====================================

    def start_background_animation(self):

        self.gridOffset = 0

        self.timer = QTimer()

        self.timer.timeout.connect(self.animate_background)

        self.timer.start(30)

    def animate_background(self):

        self.gridOffset += 2

        if self.gridOffset >= 50:

            self.gridOffset = 0

        self.update()

    # ====================================
    # PAINT EVENT
    # ====================================

    def paintEvent(self,event):

        painter = QPainter(self)

        painter.setRenderHint(QPainter.Antialiasing)

        ###################################
        # Gradient Background
        ###################################

        gradient = QLinearGradient(
            0,
            0,
            0,
            self.height()
        )

        gradient.setColorAt(
            0,
            QColor(5,10,25)
        )

        gradient.setColorAt(
            1,
            QColor(0,0,0)
        )

        painter.fillRect(
            self.rect(),
            QBrush(gradient)
        )

        ###################################
        # Grid
        ###################################

        pen = QPen(
            QColor(0,170,255,40)
        )

        painter.setPen(pen)

        spacing = 50

        offset = self.gridOffset

        x = offset

        while x < self.width():

            painter.drawLine(
                x,
                0,
                x,
                self.height()
            )

            x += spacing

        y = offset

        while y < self.height():

            painter.drawLine(
                0,
                y,
                self.width(),
                y
            )

            y += spacing

    # ====================================
    # GUI UPDATE METHODS
    # ====================================

    def update_status(self,text):

        self.status.setText(
            f"STATUS : {text.upper()}"
        )

    def update_command(self,text):

        self.userBubble.show_message(text)

    def update_response(self,text):

        self.aiBubble.show_message(text)