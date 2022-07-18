
import os
import time

def myping(host):
        response = os.system("ping -c 1 " + host)
        if response == 0:
                print ('ping sucessful')
                return True
        else:
                print ('ping failed')
                return False


check = myping("www.google.com")


if check == False:
        print ('first ping failed waiting for 2nd ping')
        time.sleep(600)
        check2 = myping("www.google.com")
        if check2 == False:
                print ('rebooting system')
                time.sleep(5)
                os.system('reboot now')
        else:
                print ('exiting')

