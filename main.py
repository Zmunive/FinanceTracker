from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout
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

        # Contenido (vacío por ahora)
        self.content = QWidget()

        # Agregar al layout
        layout.addWidget(self.sidebar)
        layout.addWidget(self.content)


if __name__ == "__main__":
    app = QApplication([])

    window = MainWindow()
    window.show()

    app.exec()
