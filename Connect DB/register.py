from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtSql import QSqlQuery
from database import Database as db

class RegisterForm(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Register.ui", self)
        if db.connectDB():
            query = QSqlQuery()
            query.prepare(
                """
                    INSERT INTO users (username, password)
                    VALUES (:username, :password)
                """
            )
            query.bindValue(":username", "admin")
            query.bindValue(":password", 000)
            query.exec()
            print("Register successfully!")
        else:
            print("Cannot connect to database!")
        db.disconnectDB()