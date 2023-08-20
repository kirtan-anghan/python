import socket
import datetime


def server_program():
    # get the hostname
    host = socket.gethostname()
    port = 5000  # initiate port number above 1024

    server_socket = socket.socket()  # get instance
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(15)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        if data == "time":
            data = datetime.datetime.now().strftime("%H:%M:%S")
        elif data == "date":
            data = datetime.date.today().strftime("%d/%m/%Y")
        print("from connected user: " + str(data))
        conn.send(data.encode())  # send data to the client

        if data == "bye":
            break

    conn.close()  # close the connection


if __name__ == '__main__':
    server_program()