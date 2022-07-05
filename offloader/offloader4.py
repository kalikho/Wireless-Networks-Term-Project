import configparser
import os
import datetime

config = configparser.ConfigParser()
config.read('../configuration.ini')
# config['hosts']['ip1']
print(datetime.datetime.now())
print("Task Offloading Started for Device 4")
os.system('sshpass -p "ani01" scp -vr tasks/workload.csv anindita@172.16.117.158:/home/anindita/tasks')
print(datetime.datetime.now())
print("Task Offloading Done for Device 4")