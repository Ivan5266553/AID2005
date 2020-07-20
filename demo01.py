from socket import *
import time

f = open("my.log", 'a')

sockfd = socket()
sockfd.bind(("0.0.0.0", 8888))
sockfd.listen(5)


sockfd.settimeout(3)

while True:
    print("Waiting fot connect")
    try:
        connfd, addr = sockfd.accept()
        print("Connect from", addr)
    except:
        msg = "%s : %s" % (time.ctime(), e)
        f.write(msg)
        time.sleep(2)
    else:
        data =connfd.recv(1024)
        print(data.decode())