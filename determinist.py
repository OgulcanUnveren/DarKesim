#!/usr/bin/python
import psutil
import time
import os
import sqlite3
from sqlite3 import Error
from playsound import playsound
import socket
import re
from functools import partial
from multiprocessing.pool import Pool
import subprocess
def get_chromeasd(get_zport):
    listOfProcessIds = findProcessIdByName("wexond")
    if len(listOfProcessIds) > 0:

        for elem in listOfProcessIds:
                    processID = elem['pid']
                    processName = elem['name']
                    processCreationTime =  time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(elem['create_time']))
#                    print(str(elem['cmdline'][-1]))
                    single_stander = psutil.Process(processID)
                    single_stander.terminate()
 #                   print("Process:"+processName+" terminated")
                    if single_stander.connections() != "":
                            #playsound("alert.mp3")
                        for cons in single_stander.connections():
#                            radarcan = socket.gethostbyaddr(cons.raddr)
                            #print(re.findall('"([^']*)"', str(cons.raddr)))
                            stem = str(cons.raddr)
                            pattern = "addr(ip='"
                            fist_part = stem.split(pattern,maxsplit=1)
                            ipvepirt = list(fist_part)[-1]
                            outp = str(ipvepirt)
                            get_ip = outp.partition("'")[0]
                            #get_port = outp.partition("port=")[-1][:-1]
                            get_port = get_zport
                            print(get_ip+":"+get_port)
                            print(subprocess.Popen("lsof -i :"+get_port  , shell=True))
                            subprocess.Popen("bash fuser -k -n tcp "+get_port, shell=True)
                            subprocess.Popen("bash fuser -k -n tcp "+get_port, shell=True)

#                            radarcan = socket.getaddrinfo(get_ip, get_port)
def get_chrome(get_port):
  #   print(subprocess.Popen("lsof -i :"+get_port  , shell=True))
    # subprocess.Popen("fuser -k -n tcp "+get_port, shell=True)
     #subprocess.Popen("fuser -k -n udp "+get_port, shell=True) 
     subprocess.Popen("lsof -i tcp:"+get_port+" | awk 'NR!=1 {print $2}' | xargs kill"  , shell=True)
     subprocess.Popen("lsof -i udp:"+get_port+" | awk 'NR!=1 {print $2}' | xargs kill"  , shell=True)
     subprocess.Popen("fuser -k -n tcp "+get_port, shell=True)
     subprocess.Popen("fuser -k -n udp "+get_port, shell=True)
#lsof -i tcp:${val} | awk 'NR!=1 {print $2}' | xargs kill
"copiedfuncs"

"""
List all the ports opened by processes on the local machine
to run it with sudo: sudo python port_processes.py
"""


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn
def create_task(conn, task):
    """
    Create a new task
    :param conn:
    :param task:
    :return:
    """

    sql = ''' INSERT INTO logs(pid,ProcessName,Time,Connections)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()

    return cur.lastrowid

def checkIfProcessRunning(processName):
    '''
    Check if there is any running process that contains the given name processName.
    '''
    #Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;
def findProcessIdByName(processName):
    '''
    Get a list of all the PIDs of a all the running process whose name contains
    the given string processName
    '''
    listOfProcessObjects = []
    #Iterate over the all the running process
    for proc in psutil.process_iter():
       try:
           pinfo = proc.as_dict(attrs=['pid', 'name','cmdline', 'create_time'])
           # Check if process name contains the given name string.
           if processName.lower() in pinfo['name'].lower() :
               listOfProcessObjects.append(pinfo)
       except (psutil.NoSuchProcess, psutil.AccessDenied , psutil.ZombieProcess) :
           pass
    return listOfProcessObjects;

def sokaktadilen():

    wholetube = psutil.net_connections()
    lugochinese = []
    for pid in wholetube:
        lugochinese.append(pid.pid)
    mylist = list(dict.fromkeys(lugochinese))
    
    list_to_stand = ['m.spotify.music', '.android.chrome', 'gle.android.gms', 'mdnsd', '.gms.persistent', 'python', 'su', 'android.youtube', 'android.vending', 'system_server', 'earchbox:search','droid.sshserver']
    ovidoc = []
    listOfProcessIds = findProcessIdByName("wexond")

    for listos in mylist:


                  
        single_stander = psutil.Process(listos)
        ovidoc.append(single_stander.name())
    mylist = list(dict.fromkeys(ovidoc))
    
    
    for last_tpo_stand in mylist:
        if last_tpo_stand == "python3":
                listOfProcessIds = findProcessIdByName("python3")
            
                if len(listOfProcessIds) > 0:

                    for elem in listOfProcessIds:
                        processID = elem['pid']
                        processName = elem['name']
                        processCreationTime =  time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(elem['create_time']))
                        if str(elem['cmdline'][-1]) == "/data/data/com.termux/dar_kesim/determinist.py":
                            pass
                        elif str(elem['cmdline'][-1]) == "/data/data/com.termux/dar_kesim/deterics.py":
                            pass
                        elif str(elem['cmdline'][-1]) == "run":
                            pass
                        elif str(elem['cmdline'][-1]) == "/data/data/com.termux/dar_kesim/detergoogle.py":
                            pass
                        elif str(elem['cmdline'][-1]) == "/data/data/com.termux/dar_kesim/deterist.py":
                            pass
                        elif str(elem['cmdline'][-1]) == "/data/data/com.termux/dar_kesim/deterics.py":
                            pass

                        else:
                            print(str(elem['cmdline'][-1]))
#                            print('Tek olası revshell canum')
                            print((processID ,processName,processCreationTime ))
                            single_stander = psutil.Process(processID)
                            if single_stander.connections() != "":
                                #playsound("alert.mp3")
                                for cons in single_stander.connections():
                                    database = r"/data/data/com.termux/dar_kesim/webapp/asskicker.db"
  
    
                                    conn = create_connection(database)
                                    with conn:
                                        task_2 = (str(processID), str(processName), str(processCreationTime), str(cons))

        # create tasks
                                        create_task(conn, task_2)
                                        watereye = open("/data/data/com.termux/dar_kesim/webapp/olupbiten.txt","a")
                                        #os.system("lsof -i : "+)
                                        watereye.write("Process:"+str(processID)+ " ProcessName:" + str(processName) + "Time:"+ str(processCreationTime))
                                        watereye.close()
                                        stem = str(cons.laddr)
                                        pattern = "addr(ip='"
                                        fist_part = stem.split(pattern,maxsplit=1)
                                        ipvepirt = list(fist_part)[-1]
                                        outp = str(ipvepirt)
                                        get_ip = outp.partition("'")[0]
                                        get_port = outp.partition("port=")[-1][:-1]
                                        single_stander.terminate()
                                        get_chrome(get_port)
#                                        print(subprocess.Popen("lsof -i :"+get_port  , shell=True))
#                                        subprocess.Popen("bash fuser -k -n tcp "+get_port, shell=True)
#                                        subprocess.Popen("bash fuser -k -n tcp "+get_port, shell=True)
                                        print("port has been loved")
                                        #playsound("alert.mp3")
#                                print("Process:"+processName+" terminated")

                        #database = r"C:\sqlite\db\pythonsqlite.db"

    
                        #conn = create_connection(database)
                        #with conn:



         #                   task_2 = ('Confirm with user about the top requirements', 1, 1, project_id, '2015-01-03', '2015-01-05')

        
        #                    create_task(conn, task_1)
                            
#                        single_stander = psutil.Process(processID)
 #                       single_stander.terminate()
  #                      print("Process:"+processName+" terminated")


        elif last_tpo_stand not in list_to_stand:
            listOfProcessIds = findProcessIdByName(last_tpo_stand)
            if len(listOfProcessIds) > 0:
                print('Process Exists | PID and other details are')
                for elem in listOfProcessIds:
                    processID = elem['pid']
                    processName = elem['name']
                    processCreationTime =  time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(elem['create_time']))
                    print((processID ,processName,processCreationTime ))
                    
                    if processName not in list_to_stand:
                        
                        single_stander = psutil.Process(processID)
#                        single_stander.terminate()
                        #print("Process:"+processName+" terminated")
                        if single_stander.connections() != "":
                            #playsound("alert.mp3")
                            for cons in single_stander.connections():
                                database = r"/data/data/com.termux/dar_kesim/webapp/asskicker.db"

    
                                conn = create_connection(database)
                                with conn:
                                    task_2 = (str(processID), str(processName), str(processCreationTime), str(cons))

        # create tasks
                                    create_task(conn, task_2)
                                    watereye = open("/data/data/com.termux/dar_kesim/webapp/olupbiten.txt","a")
     
                                    watereye.write("Process:"+str(processID)+ " ProcessName:" + str(processName) + "Time:"+ str(processCreationTime) + "Connections:" + str(cons) + "\n")
                                    watereye.close()
                                    stem = str(cons.laddr)
                                    pattern = "addr(ip='"
                                    fist_part = stem.split(pattern,maxsplit=1)
                                    ipvepirt = list(fist_part)[-1]
                                    outp = str(ipvepirt)
                                    get_ip = outp.partition("'")[0]
                                    get_port = outp.partition("port=")[-1][:-1]
                                    #get_chrome(get_port)

                                    single_stander.terminate()
                                    get_chrome(get_port)
                                    #print(subprocess.Popen("lsof -i :"+get_port  , shell=True))
                                    #subprocess.Popen("bash fuser -k -n tcp "+get_port, shell=True)
                                    #subprocess.Popen("bash fuser -k -n tcp "+get_port, shell=True)
                                    print("port and process has been loved")

            else:
                print('No Running Process found with given text')
            print('** Find running process by name using List comprehension **')


def whitelist():
    try:
        f=open("whitelist.domains","r") #Open external file to see what sites can pass our gateway
        filterlist=f.read()
        for line in filterlist.split():
            if(";" in line):
                print("Ignore comment")
            else:
                try:
                    os.system("bash whiter.sh "+line)        
                except:
                                print ("Can't load filter list")
#            socket.inet_aton(line)
       #             print("I'm an ipv4! ",line)
                                                        #if i'm here cuz line is an ipv4 address
      #              os.popen("iptables -I FORWARD -p ALL -m string --string  "+line+" --algo kmp "+timeout+" -j ACCEPT")
     #               os.popen("iptables -I FORWARD -p ALL -m string --string  "+line+" --algo kmp -j LOG --log-prefix 'WHITELIST-SDS'")
    #            except: # if i'm there cuz its not an ipv4 so a normal string
   #                 os.popen("iptables -I FORWARD -p tcp --match multiport --dports 80,443 -m string --string "+line+" --algo kmp "+timeout+" -j ACCEPT")
  #                  os.popen("iptables -I FORWARD -p udp --dport 53 -m string --string "+line+" --algo kmp "+timeout+" -j ACCEPT")
 #                   os.popen("iptables -I FORWARD -p ALL -m string --string  "+line+" --algo kmp -j LOG --log-prefix 'WHITELIST-SDS'")
#                    print ("added whitelist rule: ",line)
        while True:
            sokaktadilen()
    except:
                                print ("Can't load filter list")




if __name__ == "__main__":
#    whitelist()
    while True:
        sokaktadilen()
