redis_dictionary={}

def redis_set(request_message)-> None:
    request_message.replace("\r\n","")

    index1=request_message.index("$")
    index2=request_message.rfind("$")
    for i in range(index1+1,index2):
        if request_message[i]=="$":
            key=request_message[i:index2]
            break
    value=request_message[index2:]
    redis_dictionary[key]=value


def redis_get(request_message) -> str:
    request_message.replace("\r\n","")
    index2=request_message.rfind("$")
    key=request_message[index2:]
    
    if key in redis_dictionary:
        return redis_dictionary[key]
    else:
        return "$-1\r\n" 
