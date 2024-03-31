def redis_database(mode, key, value)-> str:
    redis_dictionary={}

    if mode=='s':
        redis_dictionary[key]=value
        return "okay"
    else:
        if key in redis_dictionary.keys():
            return redis_dictionary[key]
        else:
            return "error, key not found" 
