import configparser
import os
import datetime
config = configparser.ConfigParser()
config.read('../configuration.ini')
# config['hosts']['ip2']
print(datetime.datetime.now())
print("Task Offloading Started for Device 2")
os.system('sshpass -p "dancepeacock" scp -vr tasks/workload.csv dipraj@172.16.117.15:/home/dipraj/tasks')
print(datetime.datetime.now())
print("Task Offloading Done for Device 2")