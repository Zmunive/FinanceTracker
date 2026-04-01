from PySide6.QtWidgets import QFrame, QVBoxLayout, QPushButton, QLabel
from PySide6.QtCore import Qt
import qtawesome as qta


class Sidebar(QFrame):
    def __init__(self):
        super().__init__()

        self.setObjectName("sidebar")
        self.setFixedWidth(240)

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(10, 20, 10, 10)
        main_layout.setSpacing(15)
        self.setLayout(main_layout)

        # 🔹 Title
        self.title = QLabel("FinanceTracker")
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setObjectName("sidebarTitle")

        main_layout.addWidget(self.title)

        # 🔹 Botones

        # Principal
        self.dashboard_btn = self.create_button("Dashboard", "fa5s.home")
        self.ingresos_btn = self.create_button("Ingresos", "fa5s.plus")

        # Gastos
        self.expenses_btn = self.create_button("Gastos Fijos", "fa5s.wallet")
        self.g_variables_btn = self.create_button("Gastos Variables", "fa6s.arrow-trend-up")

        # Crédito
        self.tarjetas_btn = self.create_button("Tarjetas", "fa5s.credit-card")

        # Préstamos
        self.me_deben_btn = self.create_button("Me Deben", "fa6s.circle-arrow-up")
        self.debo_btn = self.create_button("Debo", "fa6s.circle-arrow-down")

        # Análisis
        self.reportes_btn = self.create_button("Reportes", "fa5s.file-invoice-dollar")
        self.proyecciones_btn = self.create_button("Proyecciones", "fa5s.file-signature")

        # 🔹 Secciones
        main_layout.addLayout(self.create_section("Principal", [
            self.dashboard_btn,
            self.ingresos_btn
        ]))

        main_layout.addLayout(self.create_section("Gastos", [
            self.expenses_btn,
            self.g_variables_btn
        ]))

        main_layout.addLayout(self.create_section("Crédito", [
            self.tarjetas_btn
        ]))

        main_layout.addLayout(self.create_section("Préstamos", [
            self.me_deben_btn,
            self.debo_btn
        ]))

        main_layout.addLayout(self.create_section("Análisis", [
            self.reportes_btn,
            self.proyecciones_btn
        ]))

        main_layout.addStretch()

    # 🔹 Crear botón
    def create_button(self, text, icon_name):
        btn = QPushButton(f"  {text}")
        btn._icon = qta.icon(icon_name, color = "#ffffff")
        btn.setIcon(btn._icon)
        btn.setObjectName("sidebarButton")
        btn.setCursor(Qt.PointingHandCursor)
        return btn

    # 🔹 Crear sección
    def create_section(self, title_text, buttons):
        section_layout = QVBoxLayout()
        section_layout.setSpacing(5)

        label = QLabel(title_text)
        label.setObjectName("sectionLabel")

        section_layout.addWidget(label)

        for btn in buttons:
            section_layout.addWidget(btn)

        return section_layout