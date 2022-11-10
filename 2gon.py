import time
import os
import sys

sleep = sys.argv[1]
os.system('sudo pon')
time.sleep(int(sleep))
os.system('sudo poff')
time.sleep(5)
os.system('sudo reboot')
