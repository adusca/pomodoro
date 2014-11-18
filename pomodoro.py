import time
import pynotify

def sendmessage(title, message, minutes):
    time.sleep(minutes*60)
    pynotify.init("Test")
    notice = pynotify.Notification(title, message)
    notice.show()
    return

minutes = int(raw_input("How long? (in minutes) "))
sendmessage("Time is up!", "Take a 5 minutes break", minutes)
