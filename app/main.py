import socket


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    (connection, address) = server_socket.accept()
 
    while True:
        try : 
            redis_server_respone="+PONG\r\n"
            data=connection.recv(1024).decode(encoding="utf-8")
            connection.send(redis_server_respone.encode())
        except BrokenPipeError:
            break



if __name__ == "__main__":
    main()
