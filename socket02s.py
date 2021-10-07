import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('0.0.0.0',8088))
print('Bind UDP on 8088...')
while True:
    str1,addr=s.recvfrom(1024)
    str2=str(str1,encoding='utf-8')
    print('I received a string is: ',str2)
    str3=str2.upper()
    s.sendto(str3.encode('utf-8'),addr)
    if str2 == '.':
        break
s.close()
