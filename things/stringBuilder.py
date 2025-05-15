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
    def __init__(self, size=10):
        self.buckets = [[] for _ in range(size)]
        self.count = 0 

    def get_index(self,key):
        if len(self.buckets) == 0:
            raise ValueError('HashTbale is unitialosed - no buckets exist')
        return hash(key) % len(self.buckets)
        
    
    def add(self, key, value):
        index = self.get_index(key)
        bucket = self.buckets[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        
        bucket.append((key,value))
        # to track load factor
        self.count+=1 

        if self.count / len(self.buckets) > 0.75:
            self.resize()

    def resize(self):
        old_buckets = self.buckets
        new_size = len(old_buckets) * 2 # double the old array
        self.buckets = [[] for _ in range(new_size) ]
        self.count = 0

        for bucket in old_buckets:
            for key, value in bucket:
                self.add(key,value)


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
                self.count -= 1
                removed = bucket.pop(i)
                return removed[1]
        return None
    
    def total(self):
        return len(self.buckets)
    
    def load_factor(self):
        return self.count / len(self.buckets)



if __name__ == '__main__':
    ht = HashTable()

    for i in range(20):
        key = f"key{i}"
        value = f"value{i}"
        ht.add(key,value)
        print(f'Inserted ({key}, {value})')
        print(f'Load factor: {ht.load_factor():.2f}')
        print(f'Bucket Count: {len(ht.buckets)}')
        print('-------')
    
    print("\n Checking that inserted keys exist")
    all_good = True
    for i in range(20):
        key = f"key{i}"
        expected = f"value{i}"
        actual = ht.get(key)
        if actual != expected:
            print(f"mismatch for {key}: expected {expected} got {actual}")
            all_good = False
    
    if all_good:
        print("we good")

