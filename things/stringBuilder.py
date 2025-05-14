"""We need to create teh resize load factor, key counting and pretty printing then done """



class StringBuilder:
    def __init__(self):
        self._parts = []
    
    def append(self, value):
        self._parts.append(str(value))
    
    def insert(self, index, value):
        self._parts.insert(index,value)

    def to_string(self):
        return ''.join(self._parts)

sb = StringBuilder()
sb.append('Hello')
sb.append(' ')
sb.append('world')
sb.insert(1,"beautiful ")
print(sb.to_string())


# we hash our keys and place them at a index in a array and to prevent collisons we create a linked list with the key pointing to the next time in that index

class HashTable:
    def __init__(self, size=0):
        self.buckets = [[] for _ in range(size)]

    def get_index(self,key):
        hash = hash(key) % len(self.buckets)
        return hash
    
    def add(self, key, value):
        index = self.get_index(key)
        bucket = self.buckets[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        
        bucket.append((key,value))

    
    def get(self,key):
        index = self.get_index(key)
        bucket = self.buckets[index]

        for k, v in bucket:
            if k == key:
                return v
        return None
    
    def remove(self, key):
        index = self.get_index(key)
        bucket = self.buckets[index]

        for i, (k, v) in enumerate(bucket): # bucket is a list of (key, value) tuples
            if k == key:
                removed = bucket.pop(i)
                return removed[1]
        return None




         

