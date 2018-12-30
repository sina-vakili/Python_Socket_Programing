import socket
import sys 




#create a Socket (my connection)
def create_socket():
    try :
        global host
        global port 
        global s

        host = ''
        port = 9999
        s = socket.socket()

    except socket.error as mag:
        print ('Socket conection error : ' , str(mag) )

#Build conection with listening and connection
def bind_socket():
    try:
        global host
        global port
        global s

        print('binding the port: ' , str(port))

        s.bind((host,port))
        s.listen(5)


    except socket.error as mag :
        print('socket blinding ' , str(mag) , '\n' , 'retrying ...')
        bind_socket()

 #Establish connection with a client
def socket_accept():
    connection,address = s.accept()
    print('connection has been estabiled ' , 'IP' , address[0] , ' port ' , str(address[1]))
    send_command(connection)
    connection.close()

def send_command(connection):
    while True :
        cmd = input()
        if cmd == 'quit' :
            connection.close()
            s.close()
            sys.exit()
        
        if len(str.encode(cmd)) > 0 :
            connection.send(str.encode(cmd))
            client_response = str(connection.recv(1024),'utf-8')
            print(client_response)

def main() :
    create_socket()
    bind_socket()
    socket_accept()

main()

