import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget,
    QLabel, QFrame, QTextEdit, QScrollArea
)
from PyQt5.QtGui import QFont, QColor
from PyQt5.QtCore import Qt
from subprocess import Popen
from utils.logger import log_event

class VisionToolkit(QMainWindow):
    """
    Main GUI class for the Computer Vision Toolkit
    """
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Computer Vision Toolkit - PyQt5")
        self.setGeometry(400, 100, 600, 700)

        self.init_ui()

    def init_ui(self):
        """
        Initialize the UI Layout with Sections
        """
        # Main layout
        layout = QVBoxLayout()

        title = QLabel("📷 Computer Vision Toolkit")
        title.setFont(QFont("Arial", 18, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        # Color Detection Section
        layout.addWidget(self.create_section_label("🎨 Color Detection"))
        layout.addWidget(self.create_button("🔴 Red Detection", "color_detection/red_detection.py"))
        layout.addWidget(self.create_button("🔵 Blue Detection", "color_detection/blue_detection.py"))

        # Haar Cascade Detection Section
        layout.addWidget(self.create_section_label("👁️ Haar Cascade Detection"))
        layout.addWidget(self.create_button("😀 Face Detection", "haar_detection/face_detection.py"))
        layout.addWidget(self.create_button("👀 Eye Detection", "haar_detection/eye_detection.py"))
        layout.addWidget(self.create_button("😊 Smile Detection", "haar_detection/smile_detection.py"))
        layout.addWidget(self.create_button("🚗 Vehicle Detection", "haar_detection/vehicle_detection.py"))
        layout.addWidget(self.create_button("👜 Mobile Detection", "haar_detection/mobile_detection.py"))

        # Logging Area
        layout.addWidget(self.create_section_label("📜 Logs"))
        self.log_area = QTextEdit()
        self.log_area.setReadOnly(True)
        self.log_area.setFixedHeight(150)
        layout.addWidget(self.log_area)

        # Central widget setup
        widget = QWidget()
        widget.setLayout(layout)

        # Scroll Area if needed
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setWidget(widget)

        self.setCentralWidget(scroll)

    def create_section_label(self, text):
        """
        Creates a styled section label
        """
        label = QLabel(text)
        label.setFont(QFont("Arial", 14, QFont.Bold))
        label.setStyleSheet("color: #2E86C1; margin-top: 15px;")
        return label

    def create_button(self, label, script):
        """
        Creates a styled button that runs a script
        """
        button = QPushButton(label)
        button.setStyleSheet("""
            QPushButton {
                background-color: #3498DB;
                color: white;
                padding: 10px;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: #2980B9;
            }
        """)
        button.clicked.connect(lambda: self.run_script(script))
        return button

    def run_script(self, script):
        """
        Launch the selected script and log the action
        """
        try:
            log_msg = f"Launching {script}"
            log_event(log_msg)
            self.log_area.append(f"[LOG]: {log_msg}")
            Popen(["python", script])
        except Exception as e:
            error_msg = f"Error launching {script}: {str(e)}"
            self.log_area.append(f"[ERROR]: {error_msg}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = VisionToolkit()
    window.show()
    sys.exit(app.exec_())
