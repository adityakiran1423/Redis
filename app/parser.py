from .redis.command_executor import redis_set, redis_get

def resp_parser(request_message) -> str:
    if request_message.startswith("*2\r\n$4\r\necho\r\n"):
        request_message.replace("\r\n","")
        index=request_message.rfind("$")
        response_message=request_message[index:]

    elif request_message.startswith("*3\r\n$3\r\nset\r\n"):
        response_message="+OK\r\n"
        redis_set(request_message)

    elif request_message.startswith("*2\r\n$3\r\nget\r\n"):
        response_message=redis_get(request_message)
        print(response_message)
    
    return response_message