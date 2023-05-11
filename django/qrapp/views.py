from django.shortcuts import render
import qrcode
import pyrebase

# Create your views here.
config = {
    "apiKey": "AIzaSyAy3NaQbZuKf-Wz3u7vqva9Vq8bjd1zS2I",
    "authDomain": "qrapp-4f12c.firebaseapp.com",
    "databaseURL": "https://qrapp-4f12c-default-rtdb.firebaseio.com/",
    "projectId": "qrapp-4f12c",
    "storageBucket": "qrapp-4f12c.appspot.com",
    "messagingSenderId": "1060269819608",
    "appId": "1:1060269819608:web:17cccc8ac098b6486379ad"
}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
database = firebase.database()

otp = 0
em = ''
pd = ''
UID = ''

def openLoginPage(request):
    return render(request, "register.html")


def validateuser(request):
    email = request.POST.get("t1")
    password = request.POST.get("t2")
    useremail = str(database.child('Data').child("users").child(UID).child("details").child('email').get().val())
    pswd = str(database.child('Data').child("users").child(UID).child("details").child('password').get().val())
    global em, pd
    em = useremail
    pd = pswd

    if email == useremail and password == pswd:

        im = qrcode.make(UID)
        im.save(r"qrapp/static/qrimages/naveen.jpg")
        return render(request, "qrcode_page.html")


    else:
        return render(request, "login.html", {"message": "Invalid User"})


def validateOTP(request):

    rno = database.child('Data').child("users").child(UID).child("details").child('user_otp').get().val()
    global otp
    otp = rno
    user_otp = request.POST.get("otp")
    if user_otp == str(otp):
        return render(request, "welcome.html")

    else:
        return render(request, "login.html", {"message": "Invalid OTP"})


def registeruser(request):
    email = request.POST.get("t1")
    username = request.POST.get("t2")
    password = request.POST.get("t3")
    try:
        user = auth.create_user_with_email_and_password(email, password)

        uid = user['localId']
        global UID
        UID = uid
        data = {"username": username, "password": password, "email": email}
        database.child("Data").child("users").child(uid).child("details").set(data)
    except:
        message ="problem"

        return render(request,"register.html", {"messg":message})


    return render(request,"login.html")


def login_view(request):
    return render(request, 'login.html')