from uuid import uuid4

from dbConnection import OtpInterface

class OtpRepository:
    def __init__(self, dbCon, dbCur):
        self.dbCon = dbCon
        self.dbCur = dbCur
        
    def create(self, email, pasw, expireAt):
        token = str(uuid4())
        query = "INSERT INTO otp(email, pasw, token, expireAt) VALUES (%s, %s, %s, %s)"
        self.dbCur.execute(query, (email, pasw, token, expireAt))
        self.dbCon.commit()
        
        return token

    def getByTokenEmail(self, token,email):
        query = "SELECT * FROM otp WHERE token = %s and email = %s"
        self.dbCur.execute(query, (token,email,))
        data = self.dbCur.fetchall()
        if len(data):
            return OtpInterface(data[0])
        else:
            return None

