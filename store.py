class Store:
    data = dict()
    
    @classmethod
    def set(s, key, val):
        s.data[key] = val
        return "OK"
        
    @classmethod
    def get(s, key):
        if key in s.data:
            return s.data[key]
        else:
            return "NULL"
            
    @classmethod
    def delete(s, key):
        if key in s.data:
            del s.data[key]
            return "OK"
            
    @classmethod
    def lpush(s, key, val):
        if key in s.data and isinstance(s.data[key], list):
            s.data[key].insert(0, val)
        else:
            s.data[key] = [val]
        return "OK"
            
    @classmethod
    def rpush(s, key, val):
        if key in s.data and isinstance(s.data[key], list):
            s.data[key].append(val)
        else:
            s.data[key] = [val]
        return "OK"
            
    @classmethod
    def lpop(s, key):
        if key in s.data and isinstance(s.data[key], list):
            return s.data[key].pop(0)
        else:
            return "NULL"
    
    @classmethod
    def rpop(s, key):
        if key in s.data and isinstance(s.data[key], list):
            return s.data[key].pop()
        else:
            return "NULL"
            
    @classmethod
    def llen(s, key):
        if key in s.data and isinstance(s.data[key], list):
            return str(len(s.data[key]))
        else:
            return "0"
            
