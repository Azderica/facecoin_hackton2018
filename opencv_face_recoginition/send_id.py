import socket

HOST = '172.30.1.28'
PORT = 5050

def getFileFromServer(filename):
    data_transferred = 0

    with socket.socket() as sock:
        sock.connect((HOST,PORT))
        #sock.sendall(filename.encode())

        data = sock.recv(1024)
        if not data:
            print('File[%s]: not file in server or error' %filename)
            return

        with open('test.jpg','wb') as f:
            try:
                while  data:
                    f.write(data)
                    data_transferred += len(data)
                    data = sock.recv(1024)
            except Exception as e:
                print(e)

    print('File[%s] complete. amount [%d]' %(filename, data_transferred))

#filename = input('Download:')

filename = "test.png"
getFileFromServer(filename)
