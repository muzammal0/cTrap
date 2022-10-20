#!/usr/bin/env python3
import pyfirmata
import time
if __name__ == '__main__':
    # Initiate communication with Arduino
    board = pyfirmata.Arduino('/dev/ttyUSB0')
    print("Communication Successfully started")
    while True:
        board.digital[2].write(1)
        time.sleep(1)
        board.digital[2].write(0)
        time.sleep(1)

	board.digital[3].write(1)
        time.sleep(1)
        board.digital[3].write(0)
        time.sleep(1)

  	board.digital[4].write(1)
        time.sleep(1)
        board.digital[4].write(0)
        time.sleep(1)
