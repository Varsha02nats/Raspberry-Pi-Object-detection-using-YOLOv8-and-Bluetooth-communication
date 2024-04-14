import serial
import time

bluetooth=serial.Serial("/dev/rfcomm4",38400)

while True:
    a=input("enter:-")
    string='X{0}'.format(a)
    bluetooth.write(string.encode("utf-8"))