import time
from serial import Serial
import socketserver

def Main():
    SER = Serial(
            port = '/dev/ttyS0', #Replace with the serial port that you are using to read information
            baudrate = 9600, #Replace with baudrate that is used by the thing writing to serial
            timeout = 1,
            )
    #UDP Server Setup#


    IP = "127.0.0.1" #Change to a usable IP for the network

    PORT 80 #This can be changed to any port, but the clients must also use the same port to connect

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    SERVER.bind((IP, PORT))
    while True
        data, addr = SERVER.recvfrom(1024) #This is the buffer, it is in bytes
        SER.write(data)
        time.sleep(1) #this is so the serial connection has time to send the information, but it ca be removed if neede

