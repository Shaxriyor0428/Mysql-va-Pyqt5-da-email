from dbConnection import Connetion,OtpInterface
from otpRepository import OtpRepository


class Repository( Connetion ):
    def __init__(self):
        super().__init__()

    def otpRepository(self):
        obj = OtpRepository(self.dbConnection,self.databaseCursor)
        return obj
    


# obj = Repository()
# data = obj.otpRepository().getByTokenEmail(token="uybdupescd",email="shax@gmail.com")

# print(data.pasw)

