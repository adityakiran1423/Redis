from app.redis.database import redis_dict, expiry_dict, set_time_dict

from datetime import datetime
import time


def redis_set(request_message):
    list = request_message.split("\r\n")

    key = list[4]
    value = list[6]

    redis_dict[key] = value


def redis_get(request_message, get_time) -> str:
    list = request_message.split("\r\n")

    key = list[4]

    if key in expiry_dict:
        status = expiry_checker(set_time_dict[key], get_time, expiry_dict[key])
        if status:
            return "$-1\r\n"
        else:
            if key in redis_dict:
                print("returning from main else")
                return f"${len(redis_dict[key])}\r\n{redis_dict[key]}\r\n"
            else:
                return "$-1\r\n"

    elif key in redis_dict:
        print("returning from main else")
        return f"${len(redis_dict[key])}\r\n{redis_dict[key]}\r\n"

    else:
        return "$-1\r\n"


def redis_set_with_expiry(request_message):
    list = request_message.split("\r\n")

    key = list[4]
    value = list[6]
    expiry = list[10]

    redis_dict[key] = value
    expiry_dict[key] = expiry
    set_time = datetime.now()
    set_time.strftime("%H:%M:%S.%f%z")
    set_time_dict[key] = set_time


def expiry_checker(set_time, get_time, expiry_time) -> bool:
    time_delta = get_time - set_time

    time_delta = int(time_delta.total_seconds() * 1000)

    expiry_time = int(expiry_time)

    print(type(time_delta))
    print(type(expiry_time))

    if time_delta > expiry_time:
        return True
    else:
        return False
