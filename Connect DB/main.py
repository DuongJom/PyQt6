from PyQt6.QtWidgets import QApplication
from login import LoginForm

if __name__ == "__main__":
    app = QApplication([])
    loginForm = LoginForm()
    loginForm.show()
    app.exec()