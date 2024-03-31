def redis_database(mode, key, value)-> str:
    redis_dictionary={}

    if mode=='s':
        redis_dictionary[key]=value
        return "okay"
    else:
        if key in redis_dictionary.keys():
            get_val=redis_dictionary[key]
            return f"${len(get_val)}\r\n\{get_val}\r\n"
        else:
            return "$-1\r\n" 
