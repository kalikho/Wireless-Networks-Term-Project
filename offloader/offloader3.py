import configparser
import os
import datetime

config = configparser.ConfigParser()
config.read('../configuration.ini')
# config['hosts']['ip1']
print(datetime.datetime.now())
print("Task Offloading Started for Device 3")
os.system('sshpass -p "senorita" scp -vr tasks/workload.csv roshan@172.16.117.8:/home/roshan/tasks')
print(datetime.datetime.now())
print("Task Offloading Done for Device 3")
