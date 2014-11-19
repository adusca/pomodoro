import time
import pynotify

def sendmessage(title, message, minutes):
    time.sleep(minutes*60)
    pynotify.init("Test")
    notice = pynotify.Notification(title, message)
    notice.show()
    return

minutes = int(raw_input("How many minutes should a pomodoro last? "))

while True:
    sendmessage("Time is up!", "Take a 5 minutes break", minutes)
    sendmessage("The break is over!","Time to got back to work", 5)
