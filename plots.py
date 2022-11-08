import pandas as pd
from datetime import datetime
import pytz

# read the file in csv
K = pd.read_csv("/home/n6/events.csv")
UTCtime = K['timestamp']
for i in range(len(UTCtime)):
    df = UTCtime[i].replace('Z', '')
    datetimeObj = datetime.strptime(df, '%Y-%m-%dT%H:%M:%S.%f')
    local_tz = pytz.timezone('Asia/Karachi')
    local_dt = datetimeObj.replace(tzinfo=pytz.utc).astimezone(local_tz)
    print(datetimeObj)
    print(local_tz.normalize(local_dt).__format__('%Y-%m-%d'))
    print(local_tz.normalize(local_dt).__format__('%H:%M:%S'))

