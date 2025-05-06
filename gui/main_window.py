# gui/main_window.py

from PySide6.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem
from db.db_manager import fetch_tools

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AMR Tool House")
        self.resize(800, 600)

        layout = QVBoxLayout()
        self.table = QTableWidget()
        layout.addWidget(self.table)

        self.setLayout(layout)
        self.load_data()

    def load_data(self):
        tools = fetch_tools()
        self.table.setRowCount(len(tools))
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["ID", "Name", "Description"])

        for row, tool in enumerate(tools):
            for col, value in enumerate(tool):
                self.table.setItem(row, col, QTableWidgetItem(str(value)))


# gui/main_window.py

from PySide6.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AMR Tool House")
        self.resize(600, 400)

        layout = QVBoxLayout()
        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["ID", "Name", "Description"])
        layout.addWidget(self.table)

        self.setLayout(layout)

        # Example static data
        self.table.insertRow(0)
        self.table.setItem(0, 0, QTableWidgetItem("1"))
        self.table.setItem(0, 1, QTableWidgetItem("Tool A"))
        self.table.setItem(0, 2, QTableWidgetItem("Antibiotic Resistance Checker"))

