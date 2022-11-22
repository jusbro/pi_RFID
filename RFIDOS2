#IMPORTS
import RPi.GPIO as GPIO
import time
from mfrc522 import SimpleMFRC522
from datetime import datetime

#OBJECTS
reader = SimpleMFRC522()

#VARIABLES AND CONSTANTS
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

#SETUP BOARD
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
#GPIO.setup(blinkLED, GPIO.OUT)
#GPIO.setup(buzzerPin, GPIO.OUT)

#METHODS
def getTimeStamp():
    now = datetime.now()
    currentTime = now.strftime("%H:%M:%S")
    strCurrentTime = str(currentTime)
    print(currentTime)
    return currentTime

#FILE CREATION
log = open("signoutSheet.txt", "w")
log.write("Sign Out Sheet\n")
log.close()
print("Daily Log Created")

#Main Loop
print("Started")
try:
    print("Starting try method")
    while True:
        print("Looking for Data")
        id, text = reader.read()
        print("Got Data")
        if id == boysPass1:
            print("Boys Pass 1")
            if boysPass1Stat == "in":
                print("Sign Out")
                print("Please Type Your First Name")
                firstName = input("->")
                print("Please Type Your Last Name")
                lastName = input("->")
                print("Signing out "+firstName+" "+lastName)
                boysPass1Name=firstName+" "+ lastName
                log = open("signoutSheet.txt", "a")
                try:
                    strCurrentTime = getTimeStamp()
                    boysPass1SignoutTime = strCurrentTime
                except:
                    print("failed to get timestamp from method")
                message = str(dailyCounter) +" "+ boysPass1Name+ " Boy's Bathroom DEPARTED: " + strCurrentTime
                log.writelines(message+"\n")
                log.close()
                dailyCounter = dailyCounter + 1
                boysPass1Stat = "out"
            elif boysPass1Stat == "out":
                print("Welcome Back "+ boysPass1Name)
                strCurrentTime = getTimeStamp()
                message = " RETURNED:" + strCurrentTime
                with open('signoutSheet.txt', 'r+') as f:
                    lines = f.readlines()
                    for i, line in enumerate(lines):
                        if line.find(boysPass1SignoutTime) !=-1:
                            lines[i] = lines[i].strip()+ message +"\n"
                    f.seek(0)
                    for line in lines:
                        f.write(line)
                boysPass1Stat = "in"

        elif id == boysPass2:
            print("Boys Pass 2")
            if boysPass2Stat == "in":
                print("Sign Out")
                print("Please Type Your First Name")
                firstName = input("->")
                print("Please Type Your Last Name")
                lastName = input("->")
                print("Signing out "+firstName+" "+lastName)
                boysPass2Name=firstName+" "+ lastName
                log = open("signoutSheet.txt", "a")
                try:
                    strCurrentTime = getTimeStamp()
                    boysPass2SignoutTime = strCurrentTime
                except:
                    print("failed to get timestamp from method")
                message = str(dailyCounter) +" "+ boysPass2Name+ " Boy's Bathroom DEPARTED: " + strCurrentTime
                log.writelines(message+"\n")
                log.close()
                dailyCounter = dailyCounter + 1
                boysPass2Stat = "out"
            elif boysPass2Stat == "out":
                print("Welcome Back "+ boysPass2Name)
                strCurrentTime = getTimeStamp()
                message = " RETURNED:" + strCurrentTime
                with open('signoutSheet.txt', 'r+') as f:
                    lines = f.readlines()
                    for i, line in enumerate(lines):
                        if line.find(boysPass2SignoutTime) !=-1:
                            lines[i] = lines[i].strip()+ message +"\n"
                    f.seek(0)
                    for line in lines:
                        f.write(line)
                boysPass2Stat = "in"

        elif id == girlsPass1:
            print("Girls Pass 1")
            if girlsPass1Stat == "in":
                print("Sign Out")
                print("Please Type Your First Name")
                firstName = input("->")
                print("Please Type Your Last Name")
                lastName = input("->")
                print("Signing out "+firstName+" "+lastName)
                girlsPass1Name=firstName+" "+ lastName
                log = open("signoutSheet.txt", "a")
                try:
                    strCurrentTime = getTimeStamp()
                    girlsPass1SignoutTime = strCurrentTime
                except:
                    print("failed to get timestamp from method")
                message = str(dailyCounter) +" "+ girlsPass1Name+ " Girls's Bathroom DEPARTED: " + strCurrentTime
                log.writelines(message+"\n")
                log.close()
                dailyCounter = dailyCounter + 1
                girlsPass1Stat = "out"
            elif girlsPass1Stat == "out":
                print("Welcome Back "+ girlsPass1Name)
                strCurrentTime = getTimeStamp()
                message = " RETURNED:" + strCurrentTime
                with open('signoutSheet.txt', 'r+') as f:
                    lines = f.readlines()
                    for i, line in enumerate(lines):
                        if line.find(girlsPass1SignoutTime) !=-1:
                            lines[i] = lines[i].strip()+ message +"\n"
                    f.seek(0)
                    for line in lines:
                        f.write(line)
                girlsPass1Stat = "in"

        elif id == girlsPass2:
            print("Girls Pass 2")
            if girlsPass2Stat == "in":
                print("Sign Out")
                print("Please Type Your First Name")
                firstName = input("->")
                print("Please Type Your Last Name")
                lastName = input("->")
                print("Signing out "+firstName+" "+lastName)
                girlsPass2Name=firstName+" "+ lastName
                log = open("signoutSheet.txt", "a")
                try:
                    strCurrentTime = getTimeStamp()
                    girlsPass2SignoutTime = strCurrentTime
                except:
                    print("failed to get timestamp from method")
                message = str(dailyCounter) +" "+ girlsPass2Name+ " Girls's Bathroom DEPARTED: " + strCurrentTime
                log.writelines(message+"\n")
                log.close()
                dailyCounter = dailyCounter + 1
                girlsPass2Stat = "out"
            elif girlsPass2Stat == "out":
                print("Welcome Back "+ girlsPass2Name)
                strCurrentTime = getTimeStamp()
                message = " RETURNED:" + strCurrentTime
                with open('signoutSheet.txt', 'r+') as f:
                    lines = f.readlines()
                    for i, line in enumerate(lines):
                        if line.find(girlsPass2SignoutTime) !=-1:
                            lines[i] = lines[i].strip()+ message +"\n"
                    f.seek(0)
                    for line in lines:
                        f.write(line)
                girlsPass2Stat = "in"

        elif id == printer1:
            print("Printer 1")
            if printer1Stat == "in":
                print("Sign Out")
                print("Please Type Your First Name")
                firstName = input("->")
                print("Please Type Your Last Name")
                lastName = input("->")
                print("Signing out "+firstName+" "+lastName)
                printer1Name=firstName+" "+ lastName
                log = open("signoutSheet.txt", "a")
                try:
                    strCurrentTime = getTimeStamp()
                    printer1SignoutTime = strCurrentTime
                except:
                    print("failed to get timestamp from method")
                message = str(dailyCounter) +" "+ printer1Name+ " Printer DEPARTED: " + strCurrentTime
                log.writelines(message+"\n")
                log.close()
                dailyCounter = dailyCounter + 1
                printer1Stat = "out"
            elif printer1Stat == "out":
                print("Welcome Back "+ printer1Name)
                strCurrentTime = getTimeStamp()
                message = " RETURNED:" + strCurrentTime
                with open('signoutSheet.txt', 'r+') as f:
                    lines = f.readlines()
                    for i, line in enumerate(lines):
                        if line.find(printer1SignoutTime) !=-1:
                            lines[i] = lines[i].strip()+ message +"\n"
                    f.seek(0)
                    for line in lines:
                        f.write(line)
                printer1Stat = "in"
        elif id == printer2:
            print("Printer 2")
            if printer2Stat == "in":
                print("Sign Out")
                print("Please Type Your First Name")
                firstName = input("->")
                print("Please Type Your Last Name")
                lastName = input("->")
                print("Signing out "+firstName+" "+lastName)
                printer2Name=firstName+" "+ lastName
                log = open("signoutSheet.txt", "a")
                try:
                    strCurrentTime = getTimeStamp()
                    printer2SignoutTime = strCurrentTime
                except:
                    print("failed to get timestamp from method")
                message = str(dailyCounter) +" "+ printer2Name+ " Printer DEPARTED: " + strCurrentTime
                log.writelines(message+"\n")
                log.close()
                dailyCounter = dailyCounter + 1
                printer2Stat = "out"
            elif printer2Stat == "out":
                print("Welcome Back "+ printer2Name)
                strCurrentTime = getTimeStamp()
                message = " RETURNED:" + strCurrentTime
                with open('signoutSheet.txt', 'r+') as f:
                    lines = f.readlines()
                    for i, line in enumerate(lines):
                        if line.find(printer2SignoutTime) !=-1:
                            lines[i] = lines[i].strip()+ message +"\n"
                    f.seek(0)
                    for line in lines:
                        f.write(line)
                printer2Stat = "in"

        elif id == printer3:
            print("Printer 3")
            if printer3Stat == "in":
                print("Sign Out")
                print("Please Type Your First Name")
                firstName = input("->")
                print("Please Type Your Last Name")
                lastName = input("->")
                print("Signing out "+firstName+" "+lastName)
                printer3Name=firstName+" "+ lastName
                log = open("signoutSheet.txt", "a")
                try:
                    strCurrentTime = getTimeStamp()
                    printer3SignoutTime = strCurrentTime
                except:
                    print("failed to get timestamp from method")
                message = str(dailyCounter) +" "+ printer3Name+ " Printer DEPARTED: " + strCurrentTime
                log.writelines(message+"\n")
                log.close()
                dailyCounter = dailyCounter + 1
                printer3Stat = "out"
            elif printer3Stat == "out":
                print("Welcome Back "+ printer3Name)
                strCurrentTime = getTimeStamp()
                message = " RETURNED:" + strCurrentTime
                with open('signoutSheet.txt', 'r+') as f:
                    lines = f.readlines()
                    for i, line in enumerate(lines):
                        if line.find(printer3SignoutTime) !=-1:
                            lines[i] = lines[i].strip()+ message +"\n"
                    f.seek(0)
                    for line in lines:
                        f.write(line)
                printer3Stat = "in"
                
        elif id == printer4:
            print("Printer 4")

        elif id == locker1:
            print("Locker 1")
            if locker1Stat == "in":
                print("Sign Out")
                print("Please Type Your First Name")
                firstName = input("->")
                print("Please Type Your Last Name")
                lastName = input("->")
                print("Signing out "+firstName+" "+lastName)
                locker1Name=firstName+" "+ lastName
                log = open("signoutSheet.txt", "a")
                try:
                    strCurrentTime = getTimeStamp()
                    locker1SignoutTime = strCurrentTime
                except:
                    print("failed to get timestamp from method")
                message = str(dailyCounter) +" "+ locker1Name+ " Locker DEPARTED: " + strCurrentTime
                log.writelines(message+"\n")
                log.close()
                dailyCounter = dailyCounter + 1
                locker1Stat = "out"
            elif locker1Stat == "out":
                print("Welcome Back "+ locker1Name)
                strCurrentTime = getTimeStamp()
                message = " RETURNED:" + strCurrentTime
                with open('signoutSheet.txt', 'r+') as f:
                    lines = f.readlines()
                    for i, line in enumerate(lines):
                        if line.find(locker1SignoutTime) !=-1:
                            lines[i] = lines[i].strip()+ message +"\n"
                    f.seek(0)
                    for line in lines:
                        f.write(line)
                locker1Stat = "in"

        elif id == locker2:
            print("Locker 2")
            if locker2Stat == "in":
                print("Sign Out")
                print("Please Type Your First Name")
                firstName = input("->")
                print("Please Type Your Last Name")
                lastName = input("->")
                print("Signing out "+firstName+" "+lastName)
                locker2Name=firstName+" "+ lastName
                log = open("signoutSheet.txt", "a")
                try:
                    strCurrentTime = getTimeStamp()
                    locker2SignoutTime = strCurrentTime
                except:
                    print("failed to get timestamp from method")
                message = str(dailyCounter) +" "+ locker2Name+ " Locker DEPARTED: " + strCurrentTime
                log.writelines(message+"\n")
                log.close()
                dailyCounter = dailyCounter + 1
                locker2Stat = "out"
            elif locker2Stat == "out":
                print("Welcome Back "+ locker2Name)
                strCurrentTime = getTimeStamp()
                message = " RETURNED:" + strCurrentTime
                with open('signoutSheet.txt', 'r+') as f:
                    lines = f.readlines()
                    for i, line in enumerate(lines):
                        if line.find(locker2SignoutTime) !=-1:
                            lines[i] = lines[i].strip()+ message +"\n"
                    f.seek(0)
                    for line in lines:
                        f.write(line)
                locker2Stat = "in"      

        elif id == locker3:
            print("Locker 3")
            if locker3Stat == "in":
                print("Sign Out")
                print("Please Type Your First Name")
                firstName = input("->")
                print("Please Type Your Last Name")
                lastName = input("->")
                print("Signing out "+firstName+" "+lastName)
                locker3Name=firstName+" "+ lastName
                log = open("signoutSheet.txt", "a")
                try:
                    strCurrentTime = getTimeStamp()
                    locker3SignoutTime = strCurrentTime
                except:
                    print("failed to get timestamp from method")
                message = str(dailyCounter) +" "+ locker3Name+ " Locker DEPARTED: " + strCurrentTime
                log.writelines(message+"\n")
                log.close()
                dailyCounter = dailyCounter + 1
                locker3Stat = "out"
            elif locker3Stat == "out":
                print("Welcome Back "+ locker3Name)
                strCurrentTime = getTimeStamp()
                message = " RETURNED:" + strCurrentTime
                with open('signoutSheet.txt', 'r+') as f:
                    lines = f.readlines()
                    for i, line in enumerate(lines):
                        if line.find(locker3SignoutTime) !=-1:
                            lines[i] = lines[i].strip()+ message +"\n"
                    f.seek(0)
                    for line in lines:
                        f.write(line)
                locker3Stat = "in"

        elif id == locker4:
            print("Locker 4")
            if locker4Stat == "in":
                print("Sign Out")
                print("Please Type Your First Name")
                firstName = input("->")
                print("Please Type Your Last Name")
                lastName = input("->")
                print("Signing out "+firstName+" "+lastName)
                locker4Name=firstName+" "+ lastName
                log = open("signoutSheet.txt", "a")
                try:
                    strCurrentTime = getTimeStamp()
                    locker4SignoutTime = strCurrentTime
                except:
                    print("failed to get timestamp from method")
                message = str(dailyCounter) +" "+ locker4Name+ " Locker DEPARTED: " + strCurrentTime
                log.writelines(message+"\n")
                log.close()
                dailyCounter = dailyCounter + 1
                locker4Stat = "out"
            elif locker4Stat == "out":
                print("Welcome Back "+ locker4Name)
                strCurrentTime = getTimeStamp()
                message = " RETURNED:" + strCurrentTime
                with open('signoutSheet.txt', 'r+') as f:
                    lines = f.readlines()
                    for i, line in enumerate(lines):
                        if line.find(locker4SignoutTime) !=-1:
                            lines[i] = lines[i].strip()+ message +"\n"
                    f.seek(0)
                    for line in lines:
                        f.write(line)
                locker4Stat = "in"

        elif id == adminWhiteCard:
            print("Admin White Card")
        else:
            print("Invalid pass")
        time.sleep(1)
finally:
    GPIO.cleanup()
