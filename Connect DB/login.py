from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtSql import QSqlQuery
from database import Database as db
from register import RegisterForm

class LoginForm(QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi("Login.ui", self)
        self.btnLogin.clicked.connect(self.login)
        self.btnRegister.clicked.connect(self.register)
        self.registerForm = None

    def login(self):
        if not db.connectDB():
            print("Cannot connect to database!")
        else:
            query = QSqlQuery()
            query.prepare(
                """
                    SELECT 
                        username
                       ,password
                    FROM 
                        users
                    WHERE 
                        username = :username
                """
            )

            query.bindValue(":username", self.txtUsername.text())
            query.exec()
            
            if query.first():
                print("Login successful!")
            else:
                print("Login failed!")
        db.disconnectDB()

    def register(self):
        registerForm = RegisterForm()
        self.registerForm = registerForm
        registerForm.show()
        if registerForm.is_closed:
            self.show()
    


