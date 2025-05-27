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

