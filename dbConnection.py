import mysql.connector
from datetime import datetime

import mysql.connector
class Connetion:
    def __init__(self):
        self.dbConnection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="shaxriyor",
            database="email"
        )
        self.databaseCursor = self.dbConnection.cursor()


class OtpInterface:
    email: str = None
    pasw: str = None
    token: str = None
    expireAt: datetime = None

    def __init__(self, data):
        self.email = data[0]
        self.pasw = data[1]
        self.token = data[2]
        self.expireAt = data[3]

# obj = Connetion()
# obj.databaseCursor.execute("select * from otp where token")
# print(obj.databaseCursor.fetchall())


