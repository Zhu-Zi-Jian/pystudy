import socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
for xx in ['aBch','fd','h7Tq','2019144104','.']:
     s.sendto(xx.encode('utf-8'),('127.0.0.1',8088))
     str1 = s.recv(1024)
     str2 = str(str1,encoding = 'utf-8')
     print('The original string is: ',xx,'\tthe processed string is: ',str2)
s.close()

