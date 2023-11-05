from PyQt6 import QtGui, uic
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtSql import QSqlQuery
from database import Database as db

class RegisterForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.is_closed = False
        uic.loadUi("Register.ui", self)
        self.btnRegister.clicked.connect(self.register)

    def closeEvent(self, event):
        self.is_closed = True
    
    def register(self):
        if db.connectDB():
            query = QSqlQuery()
            query.prepare(
                """
                    SELECT 
                        username
                    FROM
                        users
                    WHERE
                        username = :username 
                """
            )
            query.bindValue(":username", self.txtUsername.text())
            query.exec()

            if query.first():
                print("Username already exists!")
            else:
                query.prepare(
                        """
                            INSERT INTO users (username, password)
                            VALUES (:username, :password)
                        """
                    )
                    
                query.bindValue(":username", self.txtUsername.text())
                query.bindValue(":password", self.txtPassword.text())
                if self.txtPassword.text() == self.txtConfirmPassword.text():
                    query.exec()
                    print("Register successfully!")
                    self.is_closed = True
                    self.close()
                else:
                    print("Failed to register! Please try again!")
        else:
            print("Cannot connect to database!")
        db.disconnectDB()
        