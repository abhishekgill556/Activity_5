"""
Description: Implements the SportsApp class, providing the core functionality of the sports application.
Author: Abhishek Gill
"""

import sys
from PySide6.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QPushButton, QMessageBox
from player.player import Player

class SportsApp(QWidget):
    """
    Represents a simple application for managing and displaying sports players in a user-friendly interface.

    Attributes:
        table (QTableWidget): The table widget displaying player details.
        button (QPushButton): A button to show a welcome message.
    """
    def __init__(self):
        """
        Sets up the main window of the application.

        This method initializes the interface, sets up widgets, and connects actions to buttons.
        """
        super().__init__()
        self.__initialize_widgets()

        self.button.clicked.connect(self.__show_message)

    def __initialize_widgets(self):
        """
        Lays out the components of the application window.

        Creates a table to display player information and a button to show a welcome message.
        The layout is set to neatly organize these elements on the screen.
        """
        self.setWindowTitle("Sports League")

        layout = QVBoxLayout()

        # Create the table
        self.table = QTableWidget()
        self.table.setRowCount(3)
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["Name", "Age", "Position"])

        # Hard-coded data
        players = [
            Player("John Doe", 25, "Forward"),
            Player("Jane Smith", 28, "Midfielder"),
            Player("Jim Brown", 22, "Defender")
        ]

        for i, player in enumerate(players):
            self.table.setItem(i, 0, QTableWidgetItem(player.name))
            self.table.setItem(i, 1, QTableWidgetItem(str(player.age)))
            self.table.setItem(i, 2, QTableWidgetItem(player.position))

        self.table.resizeColumnsToContents()
        
        layout.addWidget(self.table)

        # Create the button
        self.button = QPushButton("Show Message")
        layout.addWidget(self.button)

        self.setLayout(layout)

    def __show_message(self):
        """
        Shows a welcome message when the button is clicked.

        Pops up a friendly message box to greet the user.
        """
        QMessageBox.information(self, "Welcome", "Welcome to the Team!")
