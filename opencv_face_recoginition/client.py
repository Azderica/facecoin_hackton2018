#client program
import socket
import threading
import os

HOST = "192.168.1.102"
PORT = 8091

is_Sending = False
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

def sendingMsg():
	while True:
		data = input(">> ")
		print('send')
		#data = bytes(data, "utf-8")
		s.send(data.encode())
	s.close()


def gettingMsg():
	while True:
		print('get')
		data = s.recv(1024)
		data = data.decode("utf-8","ignore")
		#data = str(data).split("b'", 1)[1].rsplit("'",1)[0]
		if 'image' in data:
			getImageFile()

			os.system("./play.sh")
			fp = open("id", "r")
			data = fp.readline()
			s.send(data.encode())
			fp.close()

		#else:
		#	print('>> ' + data)
	s.close()

def getImageFile():
	data_transferred = 0
	data = s.recv(10)
	data = str(data).split("b'", 1)[1].rsplit("'",1)[0]
	#data = data.decode("utf-8","ignore")
	bodysize=int(data)
	print(bodysize)
	readsize=0
	data = s.recv(1024)
	if not data:
		print('File[%s]: not file in server or error' %filename)
		return

	with open('test.jpg','wb') as f:
		try:
			while readsize < bodysize-1024:
				f.write(data)
				data_transferred += len(data)
				readsize+=1024
				data = s.recv(1024)

			print('File[test.jpg] complete. amount [%d]' %(data_transferred))
		except Exception as e:
			print(e)


#threading._start_new_thread(sendingMsg,())
threading._start_new_thread(gettingMsg,())

while True:
	pass
