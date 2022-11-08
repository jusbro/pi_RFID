#IMPORTS
import RPi.GPIO as GPIO
import time
from mfrc522 import SimpleMFRC522

#OBJECTS
reader = SimpleMFRC522()

#VARIABLES AND CONSTANTS
boysPass1 = 584186405527
boysPass2 = 11

girlsPass1 = 584189224911
girlsPass2 = 11

printer1 = 11
printer2 = 11
printer3 = 11 
printer4 = 11

locker1 = 11
locker2 = 11 
locker3 = 11
locker4 = 11

counter = 0

#Main Loop
print("Started")
try:
    print("Starting try method")
    while True:
        print("Looking for Data")
        id, text = reader.read()
        print("Got Data")
        print(counter)
        counter = counter +1
        print(id,"\n")
        time.sleep(5)
finally:
    GPIO.cleanup()
