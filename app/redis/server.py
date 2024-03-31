from app.parser import resp_parser

def threaded_redis_server(connection) -> None:
    while True:
        redis_pong_response="+PONG\r\n"
        # echo_regex="\*2+\r\n\$\d+\r\necho\r\n\$\d+\r\n[a-zA-Z0-9]+\r\n"

        data=connection.recv(1024).decode(encoding="utf-8")

        if data=="*1\r\n$4\r\nping\r\n":
            connection.send(redis_pong_response.encode())

        elif data.startswith("*2\r\n$4\r\necho\r\n"):
            echo_message=resp_parser(data)
            connection.send(echo_message.encode())

        elif data.startswith("*3\r\n$3\r\nset\r\n"):
            echo_message=resp_parser(data)
            print("This is from server.py in set elif block")
            connection.send(echo_message.encode())

        elif data.startswith("*2\r\n$3\r\nset\r\n"):
            echo_message=resp_parser(data)
            print(echo_message)
            connection.send(echo_message.encode())