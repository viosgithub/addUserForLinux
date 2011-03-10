#coding:utf-8
import os

r = open("userlist","r")
GIDS = "4,20,21,24,25,26,29,30,44,46,104"
users = []
for line in r:
    users.append(line[:line.index(":")])
for user in users:
    os.system("useradd " + user)
    os.system("usermod -G " + GIDS+" "+user)
    os.system("mkdir /home/" + user)
    os.system("chown -R :" + user + " /home/" + user)
    os.system("chown -R " + user + " /home/" + user)
    os.system("chmod 700 /home/" + user)

os.system("chpasswd < userlist")



