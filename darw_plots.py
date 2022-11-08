import pandas as pd
import datetime as dt
from _csv import writer
from datetime import timedelta
from datetimerange import DateTimeRange

import os
import csv

device_to_select = 'n1'
user = os.getlogin()
K = pd.read_csv('/home/' + user + '/refine_data_' + device_to_select + '.csv')
start_date = K['Date_A']
state = K['State']
header = ['Date_A', 'Date_B', 'Duration', 'State']
header2 = ['Date_A', 'Min', 'State']
active = {"Date": [], "Duration": []}
inactive = {"Date": [], "Duration": []}
with open('/home/' + user + '/plot_data_' + device_to_select + '.csv', 'w+', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    # calculate time difference
    for i in range(len(start_date) - 1):
        df = start_date[i].split('.')[0]
        df2 = start_date[i + 1].split('.')[0]
        datetimeObj = dt.datetime.strptime(df, '%Y-%m-%d %H:%M:%S')
        datetimeObj2 = dt.datetime.strptime(df2, '%Y-%m-%d %H:%M:%S')
        diff = datetimeObj2 - datetimeObj
        # print(diff)
        data = [datetimeObj, datetimeObj2, diff, state[i]]
        writer.writerow(data)
    f.close()

# make active-inactive list
data2 = pd.read_csv('/home/' + user + '/plot_data_' + device_to_select + '.csv')
s_date = data2.Date_A[0].split(' ')[0]
s_date += ' 00:00'
s_date_dt = dt.datetime.strptime(s_date, '%Y-%m-%d %H:%M')

e_date = data2.Date_B[len(data2.Date_B) - 1].split(' ')[0]
e_date += ' 23:59'
e_date_dt = dt.datetime.strptime(e_date, '%Y-%m-%d %H:%M')

print(s_date_dt, 'Start date')
print(e_date_dt, 'End date')
match_index = []
datarow = ''
# match date and get time range index
dataff = {}
dfff = pd.DataFrame(dataff)

while s_date_dt <= e_date_dt:
    for j in range(len(data2)):
        df = data2.Date_A[j]
        df2 = data2.Date_B[j]
        dateA = dt.datetime.strptime(df, '%Y-%m-%d %H:%M:%S')
        dateB = dt.datetime.strptime(df2, '%Y-%m-%d %H:%M:%S')
        # print(s_date_dt , 'start date')
        # print(dateA , 'range A')
        # print(dateB ,' range B')
        timerange1 = DateTimeRange(dateA.__format__('%Y-%m-%d'), dateB.__format__('%Y-%m-%d'))
        if s_date_dt.__format__('%Y-%m-%d') in timerange1:
            match_index.append(j)

    print(match_index)

    # timerange = DateTimeRange(data2.Date_A[match_index[0]], data2.Date_B[match_index[len(match_index) - 1]])

    for m in range(720):
        check_date = s_date_dt + timedelta(minutes=m * 2)
        for n in (match_index[0], match_index[len(match_index) - 1]):
            timerange = DateTimeRange(data2.Date_A[n], data2.Date_B[n])
            if check_date in timerange:
                # data = [check_date.__format__('%Y-%m-%d'), m,data2.State[n]]
                    dfff[str(check_date.__format__('%Y-%m-%d'))] = [m]



    match_index.clear()
    s_date_dt += timedelta(days=1)
    print(s_date_dt)

dfff.to_csv('/home/n6/out.csv')