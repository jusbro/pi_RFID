import tkinter as tk
from mfrc522 import SimpleMFRC522
import threading
import RPi.GPIO as GPIO
import time
import datetime
import serial
uart = serial.Serial("/dev/serial0", baudrate=19200, timeout=3000)
import adafruit_thermal_printer



root = tk.Tk()
root.geometry("1280x1024")
root.resizable(0,0)

reader = SimpleMFRC522()

ThermalPrinter = adafruit_thermal_printer.get_printer_class(2.69)

printer = ThermalPrinter(uart)

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
printer4Num = 584186195029
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

loggoutName = "test"
loggoutDestination = "test"

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
    
def print_pass(name, destination):
    current_time = time.strftime('%I:%M:%S %p')
    current_Date = time.strftime('%a %b %d %Y')
    print("Printing Pass")
    printer.bold = True
    printer.feed(1)
    printer.size = adafruit_thermal_printer.SIZE_LARGE
    printer.print("Hallway Pass")
    printer.feed(2)
    printer.bold = False
    printer.size = adafruit_thermal_printer.SIZE_SMALL
    printer.print("Student: "+name)
    printer.feed(1)
    printer.print("Origin: Mr. Brown")
    printer.feed(1)
    printer.print("Destination: "+destination)
    printer.feed(1)
    printer.print("Departure Time: " + str(current_time))
    printer.print("Departure Date: " + str(current_Date))
    printer.feed(1)
    printer.bold = True 
    printer.print("_____________________________")
    printer.feed(2)
    printer.print("Returning Teacher Signature:")
    printer.feed(1)
    printer.print("_____________________________")
    printer.feed(1)

    printer.print("Time: ___________________")
    printer.feed(1)

    printer.print("PASS AUTHORIZED BY MR. BROWN")
    printer.print("call 2133 with any questions.")
    printer.feed(3)

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
        now = datetime.datetime.now()
        date_string = now.strftime("%Y-%m-%d")
        file_name = getFileName()
        log = open(file_name, "x")
        log.write("Sign Out Sheet "+date_string+"\n")
        log.close()
        print(f"File {file_name} created")
    except:
        print("File already exists")               

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
    time.sleep(0.1)
    GPIO.output(ReadLED, GPIO.LOW)
    GPIO.output(Buzzer, GPIO.LOW)

def signIn(passName, id):
    id = str(id)
    print(passName + " Pass Name")
    print("Signing In " + str(passName))
    now = datetime.datetime.now()
    strCurrentTime = now.strftime("%H:%M:%S")
    message = " RETURNED:" + strCurrentTime
    file_name = getFileName()
    correct_line = None
    try:
        log = open(file_name, "a")
        writeString = "Returned " + passName + " pass " + id + " at " + strCurrentTime + "\n"
        log.write(writeString)
        log.close()
    except FileNotFoundError as e:
        print(f"file not found {e}")
    new_window = tk.Toplevel(root)
    new_window.geometry("1280x1024")
    new_window.title("RFID Scanned")
    new_window.configure(bg="lightblue")
    label = tk.Label(new_window, text="Welcome Back from", font=("Arial", 60), bg="lightblue")
    label.pack()
    labelDestination = tk.Label(new_window, text=str(passName), font=("Arial", 60), bg="lightblue")
    labelDestination.pack()
    label2 = tk.Label(new_window, text="Please Return Your Pass ", font=("Arial", 75), bg="lightblue")
    label2.pack()
    label3 = tk.Label(new_window, text="This window will close after 6 seconds", font=("Arial", 50), bg="lightblue")
    label3.pack()
    new_window.after(6000, lambda: new_window.destroy())



def signOut(destination_name, id):
    id = str(id)

    def submitName(user_name, destination_name):
        global loggoutName
        global loggoutDestination
        loggoutName = user_name
        loggoutDestination = destination_name
        print_pass(user_name, destination_name)
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
    new_window.geometry("1280x1024")
    new_window.title("RFID Scanned")
    new_window.configure(bg="lightblue")
    label = tk.Label(new_window, text="RFID tag scanned with ID: " + str(id))
    label.pack()
    
    label2 = tk.Label(new_window, text="Enter your name", font=("Helvetica", 70), bg="lightblue")
    label2.pack()

    userName = tk.StringVar()
    entry = tk.Entry(new_window, textvariable=userName, width=60, font=("Helvetica", 60))
    entry.pack()
    entry.bind("<Return>", lambda x: submitName(entry.get(), destination_name))

    label2Spacer = tk.Label(root, text=" ", font=("Helvetica", 50))
    label2Spacer.pack()

    submitButton = tk.Button(new_window, text="Submit", font=("Helvetica", 70), command=lambda: submitName(entry.get(), destination_name))
    submitButton.pack()

    cancelButton = tk.Button(new_window, text="Cancel", font=("Helvetica", 70), command=new_window.destroy)
    cancelButton.pack()

    time.sleep(1)


    

    #signOutScript = name+" Destination: " + str(destinationName) + " Time Out: " + now.strftime("%H:%M:%S") + " Time In: "

def read_rfid():
    while True:
        try:
            id, text = reader.read()
            readLED()
            for Pass in passes:
                if id == Pass.id:
                    time.sleep(1)
                    if Pass.status == "in":
                        signOut(Pass.name, id)
                        Pass.setStatus("out")
                    elif Pass.status == "out":
                        signIn(Pass.name, id)
                        Pass.setStatus("in")
        except:
            pass

label0Spacer = tk.Label(root, text=" ", font=("Helvetica", 50))
label0Spacer.pack()
label = tk.Label(root, text="Scan a Pass", font=("Helvetica", 145))
label.pack()
labelSpacer = tk.Label(root, text=" ", font=("Helvetica", 100))
labelSpacer.pack()
label2 = tk.Label(root, text="You may also sign out with agenda", font=("Helvetica", 50))
label2.pack()
label2Spacer = tk.Label(root, text=" ", font=("Helvetica", 100))
label2Spacer.pack()
label3 = tk.Label(root, text="Alpha Version 0.13         Alpha Version 0.13          Alpha Version 0.13         Alpha Version 0.13         Alpha Version 0.13", font=("Helvetica", 20))  
label3.pack()
reprintButton = tk.Button(root, text="Reprint Last Pass", bg = "#f2946f", font=("Helvetica", 50), command=lambda:print_pass(loggoutName, loggoutDestination))
reprintButton.pack()

thread = threading.Thread(target=read_rfid)
setupBoard()
createFile()
createPasses()
thread.start()
root.mainloop()
