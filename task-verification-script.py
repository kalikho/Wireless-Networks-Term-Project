from random import randrange
import os
import pandas as pd
import configparser
import shutil 
import datetime

print("BEGIN")

configparser = configparser.ConfigParser()
configparser.read("configuration.ini")

number_of_devices = 4
directory = 'outputs'

random_dict_task_1 = {"2":0,"3":0,"4":0}
random_dict_task_2 = {"1":0,"3":0,"4":0}
random_dict_task_3 = {"1":0,"2":0,"4":0}
random_dict_task_4 = {"2":0,"3":0,"1":0}

counter_cat_a = int(configparser['settings']['category_a_device'])
counter_cat_b = int(configparser['settings']['category_b_device'])
counter_cat_c = int(configparser['settings']['category_c_device'])
counter_cat_d = int(configparser['settings']['category_d_device'])


for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f):
        while(counter_cat_a):
            print("Running in counter_cat_a")
            print(counter_cat_a)
            if(f == "outputs/result_1.csv"):
                random = randrange(number_of_devices)
                print(random)
                if(counter_cat_a == 0):
                    break
                else:
                    if(counter_cat_a == int(configparser['settings']['category_a_device'])):
                        print(counter_cat_a)
                        shutil.copy2('outputs/workload1.csv', 'outputs/result_1_verification.csv')
                    if(random == 2 and random_dict_task_1["2"] == 0):
                        os.system('sshpass -p "password" scp -vr outputs/result_1_verification.csv username@ip:/home/username/tasks/')
                        counter_cat_a = counter_cat_a - 1
                        print("===")
                        print(datetime.datetime.now())
                        print(" Verification Task :: Allocated  Task 1 to Device 2 \n")
                        print("===")
                        random_dict_task_1["2"] = 1 
                    if(random == 3 and random_dict_task_1["3"] == 0):
                        os.system('sshpass -p "password" scp -vr outputs/result_1_verification.csv username@ip:/home/username/tasks/')
                        counter_cat_a = counter_cat_a - 1
                        print("===")
                        print(datetime.datetime.now())
                        print(" Verification Task :: Allocated  Task 1 to Device 3 \n")
                        print("===")                        
                        random_dict_task_1["3"] = 1 
                    if(random == 4 and random_dict_task_1["4"] == 0):
                        os.system('sshpass -p "password" scp -vr outputs/result_1_verification.csv username@ip:/home/username/tasks/')
                        counter_cat_a = counter_cat_a - 1
                        print("===")
                        print(datetime.datetime.now())
                        print(" Verification Task :: Allocated  Task 1 to Device 4 \n")
                        print("===")
                        random_dict_task_1["4"] = 1 


        while(counter_cat_b):
            if(f == "outputs/result_2.csv"):
                random = randrange(number_of_devices)
                if(counter_cat_b == 0):
                    break
                else:
                    if(counter_cat_b == int(configparser['settings']['category_b_device'])):
                        shutil.copy2('outputs/workload2.csv', 'outputs/result_2_verification.csv')
                    if(random == 1 and random_dict_task_2["1"] == 0 ):
                        os.system('sshpass -p "password" scp -vr outputs/result_2_verification.csv username@ip:/home/username/tasks/')
                        counter_cat_b = counter_cat_b - 1
                        print("===")
                        print(datetime.datetime.now())
                        print(" Verification Task :: Allocated Task 2 to Device 1")
                        print("===")
                        random_dict_task_2["1"] = 1 
                    if(random == 3 and random_dict_task_2["3"] == 0):
                        os.system('sshpass -p "password" scp -vr outputs/result_2_verification.csv username@ip:/home/username/tasks/')
                        counter_cat_b = counter_cat_b - 1
                        print("===")
                        print(datetime.datetime.now())
                        print("Verification Task :: Allocated Task 2 to Device 3")
                        print("===")
                        random_dict_task_2["3"] = 1 

                    if(random == 4 and random_dict_task_2["4"] == 0):
                        os.system('sshpass -p "password" scp -vr outputs/result_2_verification.csv username@ip:/home/username/tasks/')
                        counter_cat_b = counter_cat_b - 1
                        print("===")
                        print(datetime.datetime.now())
                        print("Verification Task :: Allocated Task 2 to Device 4")
                        print("===")
                        random_dict_task_2["4"] = 1 

        while(counter_cat_c):
            if(f == "outputs/result_3.csv"):
                random = randrange(number_of_devices)
                if(counter_cat_c == 0):
                    break
                else:
                    if(counter_cat_c == int(configparser['settings']['category_c_device'])):
                       shutil.copy2('outputs/workload3.csv', 'outputs/result_3_verification.csv')
                    if(random == 2 and random_dict_task_3["2"] == 0):
                        os.system('sshpass -p "password" scp -vr outputs/result_3_verification.csv username@ip:/home/dipraj/tasks/')
                        counter_cat_c = counter_cat_c - 1
                        print("===")
                        print(datetime.datetime.now())
                        print("Verification Task :: Allocated Task 3 to Device 2")
                        print("===")
                        random_dict_task_3["2"] = 1 
                    if(random == 1 and random_dict_task_3["1"] == 0):
                        os.system('sshpass -p "password" scp -vr outputs/result_3_verification.csv username@ip:/home/anurag/tasks/')
                        counter_cat_c = counter_cat_c - 1
                        print("===")
                        print(datetime.datetime.now())
                        print("Verification Task :: Allocated Task 3 to Device 1")
                        print("===")
                        random_dict_task_3["1"] = 1 
                    if(random == 4 and random_dict_task_3["4"] == 0):
                        os.system('sshpass -p "password" scp -vr outputs/result_3_verification.csv username@ip:/home/anindita/tasks/')
                        counter_cat_c = counter_cat_c - 1
                        print("===")
                        print(datetime.datetime.now())
                        print("Verification Task :: Allocated Task 3 to Device 1")
                        print("===")
                        random_dict_task_3["4"] = 1 
        while(counter_cat_d):
            if(f == "outputs/result_4.csv"):
                random = randrange(number_of_devices)
                if(counter_cat_d == 0):
                    break
                else:
                    if(counter_cat_d == int(configparser['settings']['category_d_device'])):
                       shutil.copy2('outputs/workload4.csv', 'outputs/result_4_verification.csv')
                    if(random == 1 and random_dict_task_4["1"]==0):
                        os.system('sshpass -p "password" scp -vr outputs/result_4_verification.csv username@ip:/home/username/tasks/')
                        counter_cat_d = counter_cat_d - 1
                        print("===")
                        print(datetime.datetime.now())
                        print("Verification Task :: Allocated Task 4 to Device 1")
                        print("===")
                        random_dict_task_4["1"] = 1 
                    if(random == 3 and random_dict_task_4["3"] == 0):
                        os.system('sshpass -p "password" scp -vr outputs/result_4_verification.csv username@ip:/home/username/tasks/')
                        counter_cat_d = counter_cat_d - 1
                        print("===")
                        print(datetime.datetime.now())
                        print("Verification Task :: Allocated Task 4 to Device 3")
                        print("===")
                        random_dict_task_4["3"] = 1 
                    if(random == 2 and random_dict_task_4["2"] == 0):
                        os.system('sshpass -p "password" scp -vr outputs/result_4_verification.csv username@ip:/home/username/tasks/')
                        counter_cat_d = counter_cat_d - 1
                        print("===")
                        print(datetime.datetime.now())
                        print("Verification Task :: Allocated Task 4 to Device 2")
                        print("===")
                        random_dict_task_4["2"] = 1 

print("=============================== END ============================ \n")
