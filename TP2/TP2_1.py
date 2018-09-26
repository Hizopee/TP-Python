#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Excercice 1 : Les sockets
"""
#fichier: TP2_1.py
#auteur: Panthier Sharon
#date: septembre 2018

# --------------- imports --------------------------------
import sys, socket, subprocess
# -------------- Programme Principal --------------------

host = "192.168.33.126"
port = 21

user="ftp"
password="ftp" 


try:
    s=socket.socket()
    #s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # connexion UDP
    s.connect((host,port))

    """iotype = subprocess.PIPE
    cmd = ['MKD TEST', 'STOR TEST', 'CWD TEST']
    proc = subprocess.Popen(cmd, stdout=iotype).wait()
    stdout,stderr = proc.communicate()
    conn.send(stdout)"""
    
    data=s.recv(1024)
    print(data)
    
    s.send("USER ftp\r\n")
    
    s.send("PASS ftp\r\n")
  
    
    s.sendall('Hello, world')
    data = s.recv(1024)
    print(data)
    
    s.send("QUIT\r\n")
    s.close()
except Exception as e:
    print('FTP error', e) 

"""
---- Résultats de l'exécution
"""
