from PyQt6.QtSql import QSqlDatabase, QSqlQuery

class Database:
    global con
    con = QSqlDatabase.addDatabase("QSQLITE")
    con.setDatabaseName("testdb.sqlite")
    
    def __init__(self):
        self.createUserTable()
        
    def connectDB():
        con.open()
        return con.isOpen()
    
    def disconnectDB():
        con.close()

    def createUserTable(self):
        if self.connectDB():
            query = QSqlQuery()
            query.prepare(
                """
                    CREATE TABLE IF NOT EXISTS users
                    (
                        username  TEXT NOT NULL
                        ,password TEXT NOT NULL
                    )
                """
            )
            query.exec()
            print("Create table 'user' successfully!")
        else:
            print("Can not connect to database!")