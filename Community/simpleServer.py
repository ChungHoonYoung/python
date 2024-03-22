import socket

class simple_server:
    def __init__(self):
        self.bufsize = 1024
        self.counter = 0

    def run(self,ip,port):
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

        self.sock.bind((ip,port))

        self.sock.listen(5)

        while self.counter < 5:    
            clnt_sock,req_addr = self.sock.accept()

            req_message = clnt_sock.recv(self.bufsize)

            print("this is request message")
            print(req_message)

            res_message = '''HTTP/1.1 200 OK
Server:simple web server
Content-length:2048
Content-type:text/html

<html><head><title>simple web server</title></head>
<body>Doyeon! Please don't sleep at this time!</body>
</html>

'''.encode("utf-8")

            print("this is response message")
            print(res_message)

            clnt_sock.send(res_message)

            clnt_sock.close()
            self.counter += 1

        print('close sock')
        self.sock.close()

server = simple_server()
server.run("0.0.0.0",19245)