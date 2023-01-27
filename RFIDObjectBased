import tkinter as tk
from mfrc522 import SimpleMFRC522
import threading
import RPi.GPIO as GPIO
import time
import datetime

root = tk.Tk()
root.geometry("1920x1080")
root.resizable(0,0)

reader = SimpleMFRC522()

#GPIO PIN VARIABLES
PowerLED = 37
ReadLED = 33
Buzzer = 31

boysPass1Num = 584186286068
boysPass1Stat = "in"
boysPass1Name = "Boy's Bathroom"
boysPass2Num = 584183328681
boysPass2Stat = "in"
boysPass2Name = "Boy's Bathroom"

girlsPass1Num = 584189224911
girlsPass1Stat = "in"
girlsPass1Name = "Girl's Bathroom"
girlsPass2Num = 584194599187
girlsPass2Stat = "in"
girlsPass2Name = "Girl's Bathroom"

printer1Num = 584183531207
printer1Stat = "in"
printer1Name = "Printer"
printer2Num = 584188180704
printer2Stat = "in"
printer2Name = "Printer"
printer3Num = 584191527234
printer3Stat = "in"
printer3Name = "Printer"
printer4Num = 11
printer4Stat = "in"
printer4Name = "Printer"

locker1Num = 584192701728
locker1Stat = "in"
locker1Name = "Locker"
locker2Num = 584194080866
locker2Stat = "in"
locker2Name = "Locker"
locker3Num = 584184701107
locker3Stat = "in"
locker3Name = "Locker"
locker4Num = 584189885919
locker4Stat = "in"
locker4Name = "Locker"

adminWhiteCardNum = 837979804343
adminWhiteCardStat = "out"
adminWhiteCardName = "Admin"


#SETUP GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PowerLED, GPIO.OUT)
GPIO.setup(ReadLED, GPIO.OUT)
GPIO.setup(Buzzer, GPIO.OUT)

passes = []

class Pass:
    def __init__(self, name, id, status):
        self.name = name
        self.id = id
        self.status = status
    def getStatus(self):
        return self.status
    def setStatus(self, status):
        self.status = status
    def getName(self):
        return self.name

def createPasses():
    boysPass1 = Pass(boysPass1Name, boysPass1Num, boysPass1Stat)
    boysPass2 = Pass(boysPass2Name, boysPass2Num, boysPass2Stat)
    girlsPass1 = Pass(girlsPass1Name, girlsPass1Num, girlsPass1Stat)
    girlsPass2 = Pass(girlsPass2Name, girlsPass2Num, girlsPass2Stat)
    printer1 = Pass(printer1Name, printer1Num, printer1Stat)
    printer2 = Pass(printer2Name, printer2Num, printer2Stat)
    printer3 = Pass(printer3Name, printer3Num, printer3Stat)
    printer4 = Pass(printer4Name, printer4Num, printer4Stat)
    locker1 = Pass(locker1Name, locker1Num, locker1Stat)
    locker2 = Pass(locker2Name, locker2Num, locker2Stat)
    locker3 = Pass(locker3Name, locker3Num, locker3Stat)
    locker4 = Pass(locker4Name, locker4Num, locker4Stat)
    adminWhiteCard = Pass(adminWhiteCardName, adminWhiteCardNum, adminWhiteCardStat)

    passes.append(boysPass1)
    passes.append(boysPass2)
    passes.append(girlsPass1)
    passes.append(girlsPass2)
    passes.append(printer1)
    passes.append(printer2)
    passes.append(printer3)
    passes.append(printer4)
    passes.append(locker1)
    passes.append(locker2)
    passes.append(locker3)
    passes.append(locker4)
    passes.append(adminWhiteCard)


def getFileName():
    now = datetime.datetime.now()
    date_string = now.strftime("%Y-%m-%d")
    file_name = date_string + "_Mr.BrownSignOut.txt"
    return file_name

def createFile():
    try:
        file_name = getFileName()
        log = open(file_name, "w")
        log.write("Sign Out Sheet\n")
        log.close()
        print(f"File {file_name} created")
    except:
        print("Failed to create File Log")
               

def setupBoard():
    GPIO.output(PowerLED, GPIO.HIGH)
    GPIO.output(ReadLED, GPIO.HIGH)
    GPIO.output(Buzzer, GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(PowerLED, GPIO.LOW)
    GPIO.output(ReadLED, GPIO.LOW)
    GPIO.output(Buzzer, GPIO.LOW)
    time.sleep(1)
    GPIO.output(PowerLED, GPIO.HIGH)

def readLED():
    GPIO.output(ReadLED, GPIO.HIGH)
    GPIO.output(Buzzer, GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(ReadLED, GPIO.LOW)
    GPIO.output(Buzzer, GPIO.LOW)

def signIn(passName, id):
    id = str(id)
    print(passName + " Pass Name")
    print("Signing In" + str(passName))
    now = datetime.datetime.now()
    strCurrentTime = now.strftime("%H:%M:%S")
    message = " RETURNED:" + strCurrentTime
    file_name = getFileName()
    with open(file_name, 'r+') as f:
        lines = f.readlines()
        for i, line in enumerate(reversed(lines)):
            if line.find(id) !=-1:
                print("found  id")
                lines[len(lines) - 1 - i] = lines[len(lines) - 1 - i].strip() + message + "\n"
            break
        f.seek(0)
        for line in lines:
            f.write(line)
    new_window = tk.Toplevel(root)
    new_window.geometry("1920x1080")
    new_window.title("RFID Scanned")
    new_window.configure(bg="lightblue")
    label = tk.Label(new_window, text="Welcome Back!", font=("Arial", 90), bg="lightblue")
    label.pack()
    label2 = tk.Label(new_window, text="Please Return Your Pass " + str(id), font=("Arial", 90), bg="lightblue")
    label2.pack()
    label3 = tk.Label(new_window, text="This Window Will close after 4 seconds", font=("Arial", 75), bg="lightblue")
    label3.pack()
    new_window.after(4000, lambda: new_window.destroy())


def signOut(destination_name, id):
    id = str(id)
    def submitName(user_name, destination_name):
        now = datetime.datetime.now()
        time_string = now.strftime("%H:%M:%S")
        print("Submit button pressed")
        file_name = getFileName()
        log = open(file_name, "a")
        writeString = user_name+" signed out at "+time_string+" to "+destination_name+ " with pass " + id+"\n"
        log.write(writeString)
        log.close()
        new_window.destroy()

    new_window = tk.Toplevel(root)
    new_window.geometry("1920x1080")
    new_window.title("RFID Scanned")
    new_window.configure(bg="lightblue")
    label = tk.Label(new_window, text="RFID tag scanned with ID: " + str(id))
    label.pack()
    
    label2 = tk.Label(new_window, text="Enter your name", font=("Helvetica", 90), bg="lightblue")
    label2.pack()

    submitButton = tk.Button(new_window, text="Submit", font=("Helvetica", 90), command=lambda: submitName(entry.get(), destination_name))
    submitButton.pack()

    cancelButton = tk.Button(new_window, text="Cancel", font=("Helvetica", 90), command=new_window.destroy)
    cancelButton.pack()

    userName = tk.StringVar()
    entry = tk.Entry(new_window, textvariable=userName, width=80, font=("Helvetica", 80))
    entry.pack()
    

    #signOutScript = name+" Destination: " + str(destinationName) + " Time Out: " + now.strftime("%H:%M:%S") + " Time In: "

def read_rfid():
    while True:
        try:
            id, text = reader.read()
            readLED()
            for Pass in passes:
                if id == Pass.id:
                    if Pass.status == "in":
                        signOut(Pass.name, id)
                        Pass.setStatus("out")
                    elif Pass.status == "out":
                        signIn(Pass.name, id)
                        Pass.setStatus("in")
        except:
            pass

label = tk.Label(root, text="Scan a Pass", font=("Helvetica", 180))
label.pack()

thread = threading.Thread(target=read_rfid)
setupBoard()
createFile()
createPasses()
thread.start()
root.mainloop()
