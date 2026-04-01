from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QFrame
from PySide6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("FinanceTracker")
        self.resize(1200, 800)

        # Widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Layout principal horizontal
        main_layout = QHBoxLayout()
        central_widget.setLayout(main_layout)

        # Sidebar
        self.sidebar = QFrame()
        self.sidebar.setFixedWidth(250)
        self.sidebar.setObjectName("sidebar")

        # Contenido
        self.content = QFrame()
        self.content.setObjectName("content")

        # Agregar al layout
        main_layout.addWidget(self.sidebar)
        main_layout.addWidget(self.content)


if __name__ == "__main__":
    app = QApplication([])

    window = MainWindow()
    window.show()

    app.exec()