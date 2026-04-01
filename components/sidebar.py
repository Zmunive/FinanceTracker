from PySide6.QtWidgets import QFrame, QVBoxLayout, QPushButton, QLabel
from PySide6.QtCore import Qt
import qtawesome as qta


class Sidebar(QFrame):
    def __init__(self):
        super().__init__()

        self.setObjectName("sidebar")
        self.setFixedWidth(240)

        layout = QVBoxLayout()
        layout.setContentsMargins(10, 20, 10, 10)
        layout.setSpacing(15)
        self.setLayout(layout)

        # 🔹 Title
        self.title = QLabel("FinanceTracker")
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setObjectName("sidebarTitle")

        layout.addWidget(self.title)

        # 🔹 Buttons
        self.dashboard_btn = self.create_button("Dashboard", "fa5s.home")
        self.ingresos_btn = self.create_button("Ingresos", "fa5s.plus")
        self.expenses_btn = self.create_button("Gastos Fijos", "fa5s.wallet")
        self.g_variables_btn = self.create_button("Gastos Variables", "fa5s.wallet")
        self.tarjetas_btn = self.create_button("Tarjetas", "fa5s.credit-card")
        self.me_deben_btn = self.create_button("Me Deben", "fa5s.cog")
        self.debo_btn = self.create_button("Debo", "fa5s.cog")
        self.reportes_btn = self.create_button("Reportes", "fa5s.cog")
        self.proyecciones_btn = self.create_button("Proyecciones", "fa5s.cog")

        layout.addWidget(self.dashboard_btn)
        layout.addWidget(self.ingresos_btn)
        layout.addWidget(self.expenses_btn)
        layout.addWidget(self.g_variables_btn)
        layout.addWidget(self.tarjetas_btn)
        layout.addWidget(self.me_deben_btn)
        layout.addWidget(self.debo_btn)
        layout.addWidget(self.reportes_btn)
        layout.addWidget(self.proyecciones_btn)

        layout.addStretch()

    def create_button(self, text, icon):
        btn = QPushButton(f"  {text}")
        btn.setIcon(qta.icon(icon))
        btn.setObjectName("sidebarButton")
        btn.setCursor(Qt.PointingHandCursor)
        return btn
