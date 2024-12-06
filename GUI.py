import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

class TextCollectorApp(QWidget):
    def __init__(self):
        super().__init__()

        # this is to intitialize the UI
        self.init_ui()

    def init_ui(self):
        # Setting the window properties
        self.setWindowTitle('Text Collector with PyQt5')
        self.setGeometry(300, 300, 400, 200)

        # Creating the layout
        layout = QVBoxLayout()

        # Creating a label to prompt user for input
        self.prompt_label = QLabel('Enter text:', self)
        layout.addWidget(self.prompt_label)

        # Creating a text input field (QLineEdit)
        self.text_input = QLineEdit(self)
        layout.addWidget(self.text_input)

        # Creating a button that will trigger the display of the entered text
        self.submit_button = QPushButton('Submit', self)
        self.submit_button.clicked.connect(self.display_text)
        layout.addWidget(self.submit_button)

        # Creating a label that will display the entered text
        self.result_label = QLabel('Your text will appear here.', self)
        layout.addWidget(self.result_label)

        # Setting the layout for the window
        self.setLayout(layout)

    def display_text(self):
        # Getting the user's text from the input field
        user_text = self.text_input.text()

        # Updating the result label with the user's entered text
        self.result_label.setText(f'Your text: {user_text}')

# Creating the application object
app = QApplication(sys.argv)

# Creating the main window (instance of the TextCollectorApp class)
window = TextCollectorApp()

# Show the window to the user
window.show()

# Run the application's event loop
sys.exit(app.exec_())
