import serial
import socket

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
latitude = ''
longitude = ''
def readgps(latitude,longitude):
    """Read the GPG LINE using the NMEA standard"""
    while True:
        line = ser.readline()
        if "GPGGA" in line:
            latitude = line[18:26] #Yes it is positional info for lattitude
            longitude = line[31:39] #do it again
            return(latitude,longitude)
    print('Finished')

readgps(latitude,longitude)
