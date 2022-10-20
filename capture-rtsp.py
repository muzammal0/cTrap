import logging
import os
import time
from datetime import datetime
from uuid import uuid4
from hikvisionapi import Client
from utils import  current_milli_time, Constants, ImageOperations


class Capture(Constants):
    event_id = None
    table = 'capture_logs'


    def __init__(self):
        super().__init__()
        logging.info('Script Started')
        self.read_params()
        self.user = os.getlogin()
        self.cam = Client('http://192.168.0.2', 'admin', 'lums12345')

        self.image_dest = '/home/' + str(self.user) + '/camera_trap/camera_trap/data_root/events/'

        if not os.path.exists(self.image_dest):
            os.makedirs(self.image_dest)

        with self.db:
            self.db.create_tables()

        logging.info(f'Checked Tables')

        self.put_log([f'"{datetime.now().strftime("%Y-%m-%dT%H:%M:%S")}"', '"SCRIPT_STARTED"', '1', f'"Capture Started"'])


    def run(self):
        while True:
            try:
                response = self.cam.Event.notification.alertStream(method='get', type='Stream')
                status = (response[0]["EventNotificationAlert"]["eventState"])
                print("Motion " + status)
                gen_uuid = True
                while status == "active":
                    if gen_uuid:
                        uuid = str(uuid4().hex)
                        gen_uuid = False
                    print("Start Capturing")
                    image_response = self.cam.Streaming.channels[102].picture(method='get', type='opaque_data')
                    if not os.path.exists(self.image_dest + uuid):
                        os.makedirs(self.image_dest + uuid)
                    # timestamp = self.get_timestamp(1)
                    with open(self.image_dest + uuid + '/' + str(current_milli_time()) + '.jpg', 'wb') as f:
                        for chunk in image_response.iter_content(chunk_size=1024):
                            if chunk:
                                f.write(chunk)
                    print(image_response)
                    response = self.cam.Event.notification.alertStream(method='get', type='Stream')
                    status = (response[0]["EventNotificationAlert"]["eventState"])

            except Exception as e:
                print(e)

    def current_milli_time(self):
        return round(time.time() * 1000)



if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s - capture:%(levelname)s - %(message)s', level=logging.DEBUG)
    capture = Capture()
    capture.run()


