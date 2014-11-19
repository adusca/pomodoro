import time
import pynotify

def sendmessage(title, message, minutes):
    time.sleep(minutes*60)
    pynotify.init("Teste")
    notice = pynotify.Notification(title, message)
    notice.show()
    return

minutes = int(raw_input("How many minutes should a pomodoro last? "))
count = 1

while True:
    sendmessage("You did " + str(count) + " pomodoro(s)!", 
                "Take a 5 minutes break", minutes)
    sendmessage("The break is over!","Time to got back to work", 5)
    count += 1
