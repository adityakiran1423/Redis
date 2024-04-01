from .redis.command_executor import redis_set, redis_get, redis_set_with_expiry

from datetime import datetime

def resp_parser(request_message) -> str:
    if request_message.startswith("*2\r\n$4\r\necho\r\n"):
        request_message.replace("\r\n","")
        index=request_message.rfind("$")
        response_message=request_message[index:]

    elif request_message.startswith("*3\r\n$3\r\nset\r\n"):
        response_message="+OK\r\n"
        redis_set(request_message)

    elif request_message.startswith("*5\r\n$3\r\nset\r\n"):
        response_message="+OK\r\n"
        redis_set_with_expiry(request_message)

    elif request_message.startswith("*2\r\n$3\r\nget\r\n"):
        get_time=datetime.now()
        get_time.strftime('%H:%M:%S.%f%z')
        response_message=redis_get(request_message, get_time)
        # print(response_message)
    
    return response_message