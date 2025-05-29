## Collections Module Essentials

### Counter
when counting frequencies of elements(strings, numbers etc)

```from collections import Counter
    Counter('banana') # returns {'b':1, 'a':3, 'n':2}
```

- Common use cases: Anagrams, permutations, majority elements, frequency sorting

### defaultdict

Use when avoidong key errors and setting default values on first use.
```
from collections import defaultdict
d = defaultdict(int)
d['a'] += 1 # d['a'] is now 1 without needing to initalise it
```
Needed for grouping data, dynamic frequency counting, graph adjency lists etc

### deque

Use when you need fast queue/stack behaviour with O(1) pops from both ends
```
from collection import deque
dq = deqye([1,2,3])
dq.append(4)         # [1,2,3,4]
dq.popleft()         # 1, deque is now [2,3,4]  
```
Used for sliding window problems, BFS

### namedtuple (rare)

Use for lightweight classes for fixed data structures
```
from collections import namedtuple
Point = namedtuple('Point',['x', 'y'])
p = Point(1,2)     # p.x == 1, p.y == 2 
```

##  Other important ones

- `enumerate()` created (index, value) pairs used for lopping with indexes cleanly
- `zip()` Combines iterables element wise adn works with merging lists, pairing data
- `sorted()` Sorts a list used for quick sorting custom keys
- `reversed()` Reverses iterables string and array reversal
- `set()` Removes duplicates for when you need unique elements in a list 
- `any()`checks any across iterables
- `all()` checks all across iterables

### Little hacks 

Counter + == 

enumerate + zip 

defailtdict(list) -> Grouping items by keys
```
d = defaultdict(list)
for k, v in pairs:
    d[k].append(v)

```