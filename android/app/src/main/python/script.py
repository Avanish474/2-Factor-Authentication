import random
import smtplib
def main(otp):
        server=smtplib.SMTP('smtp.gmail.com',587)
        #adding TLS security
        server.starttls()
        #get your app password of gmail ----as directed in the video
        password='sjtofsdjcotgzjdo'
        server.login('avanishgupta606@gmail.com',password)
        #generate OTP using random.randint() function
#         otp=''.join([str(random.randint(0,9)) for i in range(4)])
        msg='Hello, Your OTP is '+str(otp)
        sender='avanishgupta606@gmail.com'  #write email id of sender
        receiver='avanishgupta607@gmail.com' #write email of receiver
        #sendi
        server.sendmail(sender,receiver,msg)
        server.quit()