"""
Description: Defines the TransitApp class to provide the graphical user interface for the transit system.
Author: Abhishek Gill
"""

import sys
from PySide6.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QPushButton, QMessageBox
from bus.bus import Bus

class TransitApp(QWidget):
    def __init__(self):
        """
        Initializes the QWindow.
        """
        super().__init__()
        self.__initialize_widgets()
        self.button.clicked.connect(self.__show_message)

    def __initialize_widgets(self):
        """
        Initializes all widgets on the QWindow.
        """
        self.setWindowTitle("Transit System")

        layout = QVBoxLayout()

        # Create the table
        self.table = QTableWidget()
        self.table.setRowCount(3)
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["Bus ID", "Capacity", "Model"])

        buses = [
            Bus("Bus101", 50, "Model X"),
            Bus("Bus102", 60, "Model Y"),
            Bus("Bus103", 40, "Model Z")
        ]

        for i, bus in enumerate(buses):
            self.table.setItem(i, 0, QTableWidgetItem(bus.bus_id))
            self.table.setItem(i, 1, QTableWidgetItem(str(bus.capacity)))
            self.table.setItem(i, 2, QTableWidgetItem(bus.model))

        layout.addWidget(self.table)

        # Resize columns to fit contents
        self.table.resizeColumnsToContents()

        # Create the button
        self.button = QPushButton("Show Message")
        layout.addWidget(self.button)

        self.setLayout(layout)

    def __show_message(self):
        """
        Displays an informational message when the button is clicked.
        """
        QMessageBox.information(self, "Coming Soon", "Coming Soon: Bus Schedules!")