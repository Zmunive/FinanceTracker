from pathlib import Path

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QFrame,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QVBoxLayout,
    QWidget,
)

from components.sidebar import Sidebar


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("FinanceTracker")
        self.resize(1200, 800)

        # Widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Layout principal
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        central_widget.setLayout(layout)

        # Sidebar
        self.sidebar = Sidebar()

        # Separador entre sidebar y contenido
        self.separator = QFrame()
        self.separator.setObjectName("mainSeparator")
        self.separator.setFrameShape(QFrame.VLine)

        # Contenido principal
        self.content = QFrame()
        self.content.setObjectName("content")

        content_layout = QVBoxLayout()
        content_layout.setContentsMargins(32, 32, 32, 32)
        content_layout.setSpacing(8)
        self.content.setLayout(content_layout)

        self.content_title = QLabel("Menu")
        self.content_title.setObjectName("contentTitle")

        self.content_hint = QLabel("Menu 2")
        self.content_hint.setObjectName("contentHint")
        self.content_hint.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        self.content_hint.setWordWrap(True)

        # Agregar al layout
        layout.addWidget(self.sidebar)
        layout.addWidget(self.separator)
        layout.addWidget(self.content)
        layout.setStretch(2, 1)

        content_layout.addWidget(self.content_title)
        content_layout.addWidget(self.content_hint)
        content_layout.addStretch()


if __name__ == "__main__":
    app = QApplication([])

    style_path = Path(__file__).resolve().parent / "styles" / "sidebar.qss"
    if style_path.exists():
        app.setStyleSheet(style_path.read_text(encoding="utf-8"))

    window = MainWindow()
    window.show()

    app.exec()
