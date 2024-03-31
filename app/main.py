import socket
import threading

from .redis.server import threaded_redis_server

def main() -> None:
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)

    while True:
        (connection, address) = server_socket.accept()
        thread = threading.Thread(target=threaded_redis_server, args=(connection, ))
        thread.start()


if __name__ == "__main__":
    main()
