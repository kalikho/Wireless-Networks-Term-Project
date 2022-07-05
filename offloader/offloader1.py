import configparser
import os
import datetime
config = configparser.ConfigParser()
config.read('../configuration.ini')
# config['hosts']['ip1']
print(datetime.datetime.now())
print("Task Offloading Started for Device 1")
os.system('sshpass -p "$iang_2021" scp -vr tasks/workload.csv anurag@172.16.117.201:/home/anurag/tasks')
print(datetime.datetime.now())
print("Task Offloading Done for Device 1")