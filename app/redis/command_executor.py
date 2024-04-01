from app.redis.database import redis_dict

from datetime import datetime

def redis_set(request_message):
    list=request_message.split("\r\n")

    key=list[4]
    value=list[6]

    if request_message.startswith("*5\r\n$3\r\nset\r\n"):
        expire_time=list[10]
        set_time = datetime.now()
        set_time.strftime('%H:%M:%S.%f%z')
        redis_dict[key]=value
        # expiry_handler(expire_time,key)
        return set_time, expire_time
    else:
        redis_dict[key]=value


def redis_get(request_message) -> str:
    list=request_message.split("\r\n")

    key=list[4]

    if request_message.startswith("*5\r\n$3\r\nset\r\n"):
        set_time, expire_time=redis_set()
        print("in starts with 5 if")
        current_time = datetime.now()
        current_time.strftime('%H:%M:%S.%f%z')

        time_delta=current_time-set_time
        time_delta.total_seconds()
        time_delta=time_delta.total_seconds()*1000

        print(f"set_time is {set_time}")
        print(f"current_time is {current_time}")
        print(f"expiry is {expire_time}")
        print(f"time_delta is {time_delta}")

        status=expiry_handler(set_time, current_time, expire_time,key)
        print(status)
        if status:
            return "$-1\r\n"
        else:
            if key in redis_dict:
                print("printing from status false else")
                return f"${len(redis_dict[key])}\r\n{redis_dict[key]}\r\n"
            else:
                return "$-1\r\n"

    else:
        print("in else of starts with 5 if")
        if key in redis_dict:
            print("returning from main else")
            return f"${len(redis_dict[key])}\r\n{redis_dict[key]}\r\n"
        else:
            return "$-1\r\n"

def expiry_handler(set_time, current_time, expire_time,key)->bool:
    time_delta=current_time-set_time
    print(f"set_time is {set_time}")
    print(f"current_time is {current_time}")
    print(f"expiry is {expire_time}")
    print(f"time_delta is {time_delta}") 
    if time_delta>expire_time:
        del redis_dict[key]
        return True
    else:
        return False