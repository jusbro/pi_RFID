#RFID Tkinter Test
__author__="Justin Brown"
__version__="0.3.0"
__revision_date__="12/1/22"
__status__="Production"

"""
This program is an attempt to practice the connection between python backend and Tkinter Frontend
At its heart, this program tracks use of student hallway time with RFID hall passes.
Students can sign out and sign back in. A file is kept on the Pi of all pass use
The program can be further expanded with data analytics
"""

#IMPORTS
import RPi.GPIO as GPIO
import time
from mfrc522 import SimpleMFRC522
from datetime import datetime
from tkinter import *
import time

#OBJECTS
reader = SimpleMFRC522()
window = Tk()

#Create the window, for some reason this cannot currently be done in a method. Will totally 'figure' this out later
window.title("Pass System V 0.3")
window.geometry('1920x1080')
window.update_idletasks()
window.update
homeTitleLabel = Label(window, text="Scan a Pass", font=("Arial Bold", 150))
nameEntry = Entry(window, bd="4", relief = SUNKEN, font=("Arial Bold", 100))
nameSubmitButton = Button(window)
homeTitleLabel.pack()
nameEntry.pack()
nameEntry.pack_forget()


#VARIABLES AND CONSTANTS
versionNumber = 0.3
signOutName = ""

boysPass1 = 584186286068
boysPass1Stat = "in"
boysPass1Name = ""
boysPass2 = 584183328681
boysPass2Stat = "in"
boysPass2Name = ""

girlsPass1 = 584189224911
girlsPass1Stat = "in"
girlsPass1Name = ""
girlsPass2 = 584194599187
girlsPass2Stat = "in"
girlsPass1Name = ""

printer1 = 584183531207
printer1Stat = "in"
printer1Name = ""
printer2 = 584188180704
printer2Stat = "in"
printer2Name = ""
printer3 = 584191527234
printer3Stat = "in"
printer3Name = ""
printer4 = 11
printer4Stat = "in"
printer4Name = ""

locker1 = 584192701728
locker1Stat = "in"
locker1Name = ""
locker2 = 584194080866
locker2Stat = "in"
locker2Name = ""
locker3 = 584184701107
locker3Stat = "in"
locker3Name = ""
locker4 = 584189885919
locker4Stat = "in"
locker4Name = ""

adminWhiteCard = 837979804343
adminWhiteCardStat = "out"
dailyCounter = 1

#buzzerPin = -1
#blinkLED = -1

#METHODS
def screenUpdate():
    #issues the command to load the specified widgets in the method that called this one. This allows the program to continue running
    window.update_idletasks()
    window.update

def createWindow():
    #does not currently work, had to be called earlier.
    window.title("Pass System V"+ versionNumber)
    window.geometry('1920x1080')
    screenUpdate()
"""
def bootUpScreen():
    #A bootup screen that displays when the program first launches
    print("Bootup Screen")
    titleLabel = Label(window, text="Browntown Pass Scan System", font=("Arial Bold", 100))
    titleLabel.grid(column=0, row=0)
    titleLabel.place(relx=0.5, anchor=N)

    secLabel = Label(window, text="System Initializing Please Standby", font=("Arial Bold", 100))
    secLabel.grid(column=0, row=0)
    secLabel.place(relx=0.5, rely=0.5, anchor=CENTER)

    titleLabel.pack()
    secLabel.pack()

    screenUpdate()

    time.sleep(5)
    #This will 'hide' the labels
    titleLabel.forget()
    secLabel.forget()
"""
def storeName():
    print("Storing Name")
    signOutName = nameEntry.get()
    print(signOutName)
    nameSubmitButton.pack_forget()
    nameEntry.pack_forget()
    try:
        strCurrentTime = getTimeStamp()
    except:
        print("Error signing out in the StoreName Method")
    screenUpdate()
    homeScreen()

def signOut():
    print("Signing Out")
    homeTitleLabel.config(text="Signing Out")
    homeTitleLabel.pack()
    nameEntry.pack()
    print("1")
    #nameSubmitButton.config(command=storeName())
    nameSubmitButton.config(text = "Sign Out", bd='5',font=("Arial Bold", 75), command=storeName)
    print("1.5")
    nameSubmitButton.pack()
    print("2")
    window.mainloop()
    time.sleep(0.5)
    #nameSubmitButton.pack_forget()

def signIn():
    print("Signing In")

def homeScreen():
    print("Home Screen")
    
    homeTitleLabel.config(text="Scan a Pass")
    #homeTitleLabel.grid(column=0, row=0)
    #homeTitleLabel.place(relx=0.5, anchor=N)
    homeTitleLabel.pack()
    screenUpdate()
    time.sleep(0.5)
    RFIDScan()

def RFIDScan():
    #work in progress.
    #This is the 'main' section of code that will read from the RFID sensor
    print("RFID Scan")
    try:
        while True:
            print("In Loop")
            time.sleep(0.2)
            print("Looking for Data")
            id, text = reader.read()
            print("Got Data")
            signOut()
    except:
        print("Error Reading RFID, Fell out of RFID Scan Method")

def createFileLog():
    #work in progress
    #Creates the log (currently a txt) if the current file is nonexistant, otherwise it reopens the exisiting log file (in the event the Pi shuts off)
    #Files will be named by date (requiring a call to the getDate() method)
    try:
        log = open("signoutSheet.txt", "w")
        log.write("Sign Out Sheet\n")
        log.close()
        print("Created File Log Successfully")
    except:
        print("Failed to create File Log")

def getTimeStamp():
    #Gets the current time using the time library. Returns time in the form of hours minutes seconds
    now = datetime.now()
    currentTime = now.strftime("%H:%M:%S")
    return currentTime

def getDate():
    #work in progress
    #Gets the current date using the time library.
    now = datetime.now()
    date = now.strftime("somthing")
    return date

def displayLogSheet():
    #work in progress
    #Accessed with the admin card, this method should print the day's signout file to terminal for quick review
    print("Print Log Sheet")



#Main Loop
#bootUpScreen()
createFileLog()
homeScreen()
