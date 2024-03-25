import socket
import threading
import sys


def threaded_redis_server(connection, reddis_pong_response):
    while True:
        data=connection.recv(1024).decode(encoding="utf-8")
        connection.send(reddis_pong_response.encode())


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)

    while True:
        try : 
            redis_pong_response="+PONG\r\n"
            (connection, address) = server_socket.accept()
            thread = threading.Thread(target=threaded_redis_server, args=(connection, redis_pong_response,))
            thread.start()
        except BrokenPipeError:
            sys.exit()


if __name__ == "__main__":
    main()
