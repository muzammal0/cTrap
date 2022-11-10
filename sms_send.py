import serial
import time

number = "+923227044026"
sms = 0
while (True):

    ser = serial.Serial("/dev/ttyTHS1", baudrate=115200, timeout=5)
    msg = "sending box " + str(sms)
    ser.write(str.encode('AT\r'))
    print(ser.read(128))


    ser.write(str.encode('AT+CMGF=1\r'))
    time.sleep(5)
    print(ser.read(128))

    ser.write(str.encode('AT+CMGDA="DEL ALL"\r'))
    time.sleep(5)
    print(ser.read(128))

    ser.write(str.encode('AT+CMGS="' + number + '"\r'))
    time.sleep(5)
    ser.write(str.encode(msg + chr(26)))
    time.sleep(5)
    sms = sms + 1
    ser.close()
    print("in wait")
    time.sleep(10)