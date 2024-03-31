from app.redis.database import redis_dict

def redis_set(request_message)-> None:
    list=request_message.split("\r\n")

    key=list[4]
    value=list[6]

    redis_dict[key]=value
    #_=redis_database(mode, key,value)


def redis_get(request_message) -> str:
    list=request_message.split("\r\n")

    key=list[4]

    #value=redis_database(mode, key,"")

    return redis_dict[key]
