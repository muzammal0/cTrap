import pandas as pd
import datetime as dt
import pytz
import csv
import os

device_to_select = 'n1'
user = os.getlogin()
# read the file in csv
K = pd.read_csv("/home/"+user+"/events.csv")
UTCtime = K['timestamp']
s_type = K['type']
devices = K['devices']
state = K['state']
header = ['Date_A', 'Devices', 'State']

with open('/home/' + user + '/refine_data_'+device_to_select+'.csv', 'a+', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)

    for i in reversed(range(len(UTCtime) - 1)):
        if s_type[i] == 'DEVICE_STATE':
            if devices[i] == device_to_select:
                df = UTCtime[i].replace('Z', '')
                df2 = UTCtime[i + 1].replace('Z', '')
                datetimeObj = dt.datetime.strptime(df, '%Y-%m-%dT%H:%M:%S.%f')
                datetimeObj2 = dt.datetime.strptime(df2, '%Y-%m-%dT%H:%M:%S.%f')
                local_tz = pytz.timezone('Asia/Karachi')
                local_dt_a = datetimeObj.replace(tzinfo=pytz.utc).astimezone(local_tz)
                local_dt_b = datetimeObj2.replace(tzinfo=pytz.utc).astimezone(local_tz)
                # print(datetimeObj)
                # print(datetimeObj2)
                # diff = datetimeObj - datetimeObj2
                # print(local_tz.normalize(local_dt).__format__('%Y-%m-%d'))
                # print(local_tz.normalize(local_dt).__format__('%H:%M:%S'))
                data = [local_dt_a, devices[i], state[i]]
                writer.writerow(data)
