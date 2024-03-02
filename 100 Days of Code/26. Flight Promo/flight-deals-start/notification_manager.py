import smtplib



class NotificationManager:
    def __init__(self, email, password) :
        self.EMAIL = email
        self.PASS = password

    def convertmsg(self, anotherlist):
        self.msg = "Low Price Alert!\n"
        for lowp in anotherlist:
            self.msg += f"Only{lowp[3]}$ to fly from Jakarta to {lowp[0]}, at {lowp[1]}\n"
        self.sendmessage(self.msg)
    
    def sendmessage(self, message):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=self.EMAIL,password=self.PASS)
            connection.sendmail(from_addr=self.EMAIL, to_addrs=self.EMAIL,
                                msg=message)
        