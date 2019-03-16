import serial
import time

arduinoData = serial.Serial('/dev/ttyACM0', 38400)

arduinoData.write("4")
    
# while(1):
#     val = raw_input("Enter values between 1 and 4: ")
#     arduinoData.write(val)
