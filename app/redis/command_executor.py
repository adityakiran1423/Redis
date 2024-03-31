from app.redis.database import redis_database 

def redis_set(request_message)-> None:
    request_message.replace("\r\n","")

    mode='s'

    index1=request_message.index("$")
    index2=request_message.rfind("$")
    for i in range(index1+1,index2):
        if request_message[i]=="$":
            key=request_message[i:index2]
            break
    value=request_message[index2:]
    _=redis_database(mode, key,value)
    # redis_dictionary[key]=value


def redis_get(request_message) -> str:
    request_message.replace("\r\n","")

    mode='g'

    index2=request_message.rfind("$")
    key=request_message[index2:]
    
    value=redis_database(mode, key,"")
    print(value)
    return value
