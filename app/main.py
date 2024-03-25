import socket
import threading


def resp_parser(request_message) -> str:
    request_message.replace("\r\n","")
    index=request_message.index("$")
    length_request_message=int(request_message[index+1])
    echo_message=request_message[index+2:]
    return echo_message


def threaded_redis_server(connection) -> None:
    while True:
        redis_pong_response="+PONG\r\n"
        data=connection.recv(1024).decode(encoding="utf-8")
        if data=="*1\r\n$4\r\nping\r\n":
            connection.send(redis_pong_response.encode())
        else:
            echo_message=resp_parser(data)
            connection.send(echo_message.encode())


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
