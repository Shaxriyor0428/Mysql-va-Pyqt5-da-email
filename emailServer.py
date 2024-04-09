import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class EmailService:
    sendSucces = False
    def __init__(self,sender_email,sender_password,receiver_email,subject,message):
        self.sender_email = sender_email
        self.sender_password = sender_password
        self.receiver_email=receiver_email
        self.subject = subject
        self.message = message

        textOfMessage = self.__createMessage()
        self.__sendMessage(textOfMessage)

    def __createMessage(self) -> MIMEMultipart:
        message = MIMEMultipart()
        message["From"] = self.sender_email
        message["To"] = self.receiver_email
        message["Subject"] = self.subject
        message.attach(MIMEText(self.message,"plain"))
        return message

    def __sendMessage(self,message:MIMEMultipart):
        try :
            server = smtplib.SMTP("smtp.gmail.com",587)
            server.starttls()
            server.login(self.sender_email,self.sender_password)
            text = message.as_string()
            server.sendmail(self.sender_email,self.receiver_email,text)
            self.sendSucces = True
            
        except Exception as er:
            self.sendSucces = False
            print(f"error at the open {er}")
        finally:
            server.quit()



