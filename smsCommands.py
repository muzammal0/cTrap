import gammu
import time
import os




class SmsClass:

    def __init__(self):
        self.start = True
        self.state_machine = gammu.StateMachine()
        self.state_machine.ReadConfig()
        self.state_machine.Init()
        self.status = self.state_machine.GetSMSStatus()
        self.remain = self.status["SIMUsed"] + self.status["PhoneUsed"] + self.status["TemplatesUsed"]

        self.user = os.path.expanduser('~')
        print(self.user)
        self.command = "none"
        self.dir_path = self.user+'/camera_trap/data_root/events'



    def run(self):


        try:
            while self.remain > 0:
                if self.start:
                    sms = self.state_machine.GetNextSMS(Start=True, Folder=0)
                    self.start = False
                else:
                    sms = self.state_machine.GetNextSMS(Location=sms[0]["Location"], Folder=0)
                self.remain = self.remain - len(sms)

                for m in sms:
                    print()
                    print("{:<15}: {}".format("Number", m["Number"]))
                    print("{:<15}: {}".format("Date", str(m["DateTime"])))
                    print("{:<15}: {}".format("State", m["State"]))
                    #print("\n{}".format(m["Text"]))  // dont print text it some time cause issues
                    self.command = (m["Text"])

                if self.command.lower() == "reboot cvgl":
                    print("reboot command received deleting sms")
                    self.sentreply("rebooting now")
                    self.state_machine.DeleteSMS(Location=sms[0]["Location"], Folder=0)
                    time.sleep(10)
                    os.system('sudo reboot')

                if self.command.lower() == "2g on cvgl":
                    print("2g On Command")
                    self.sentreply("Turning on 2g")
                    self.state_machine.DeleteSMS(Location=sms[0]["Location"], Folder=0)
                    time.sleep(5)
                    os.system('sudo python' + self.user +'/ctrap/2gon.py 1800')

                if self.command.lower() == "stats cvgl":
                        self.state_machine.DeleteSMS(Location=sms[0]["Location"], Folder=0)
                        entries = os.listdir(self.dir_path)
                        self.sentreply("pending events " + str(len(entries)))

                else:
                    self.state_machine.DeleteSMS(Location=sms[0]["Location"], Folder=0)



        except gammu.ERR_EMPTY:
            # This error is raised when we've reached last entry
            # It can happen when reported status does not match real counts
            print("Failed to read all messages!")



    def sentreply(self, msg):

        message = {
            'Text': msg,
            'SMSC': {'Location': 1},
            'Number': '03227044026',
        }

        self.state_machine.SendSMS(message)
        print("SMS reply sent")


if __name__ == "__main__":
    SmsClass = SmsClass()
    SmsClass.run()

