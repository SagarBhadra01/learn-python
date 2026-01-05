from collections import (
    Counter,
    defaultdict,
    deque,
    OrderedDict,
    ChainMap,
    namedtuple,
    UserDict,
    UserList,
    UserString
)


# 1. Counter — Frequency counting, multisets


data = "programming"

c = Counter(data)
print("Counter:", c)

print("Count of 'g':", c['g'])
print("Most common 2:", c.most_common(2))

c.update("python")          # Add more data
c.subtract("gm")            # Remove counts
print("After update/subtract:", c)

print("Expanded elements:", list(c.elements()))

# Use-case: comparing collections
c1 = Counter("abc")
c2 = Counter("bcd")
print("Union:", c1 | c2)    # max counts
print("Intersection:", c1 & c2)


# 2. defaultdict — Avoid KeyError, auto initialization


# Grouping values
groups = defaultdict(list)
pairs = [('a', 1), ('b', 2), ('a', 3)]

for k, v in pairs:
    groups[k].append(v)

print("Grouped values:", groups)

# Counting
count = defaultdict(int)
for ch in "banana":
    count[ch] += 1

print("Default count:", count)

# Unique values
unique = defaultdict(set)
unique['x'].add(10)
unique['x'].add(10)
print("Unique values:", unique)


# 3. deque — Fast queue / stack / sliding window


dq = deque([1, 2, 3])

dq.append(4)          # push right
dq.appendleft(0)      # push left
print("Deque:", dq)

dq.pop()              # remove right
dq.popleft()          # remove left
print("After pops:", dq)

dq.rotate(1)          # rotate right
dq.rotate(-1)         # rotate left
print("After rotate:", dq)

# Sliding window
window = deque(maxlen=3)
for i in range(6):
    window.append(i)
    print("Window:", window)


# 4. OrderedDict — Order-sensitive dictionary


od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
print("OrderedDict:", od)

od.move_to_end('a')           # reorder keys
print("After move:", od)

od.popitem(last=False)        # FIFO removal
print("After pop:", od)

# Order-sensitive comparison
od1 = OrderedDict([('a', 1), ('b', 2)])
od2 = OrderedDict([('b', 2), ('a', 1)])
print("Order equality:", od1 == od2)  # False


# 5. ChainMap — Multiple dicts, scope resolution


defaults = {'theme': 'dark', 'lang': 'en'}
user = {'lang': 'fr'}

settings = ChainMap(user, defaults)
print("Language:", settings['lang'])
print("Theme:", settings['theme'])

# New scope (like local variables)
child = settings.new_child({'debug': True})
print("Child map:", child)


# 6. namedtuple — Lightweight immutable objects


Student = namedtuple("Student", ["id", "name", "marks"])
s = Student(1, "Sagar", 95)

print("Student:", s)
print("Name:", s.name)
print("As dict:", s._asdict())
print("Fields:", s._fields)


# 7. UserDict — Custom dictionary behavior


class SafeDict(UserDict):
    def __getitem__(self, key):
        return self.data.get(key, "KEY NOT FOUND")

sd = SafeDict()
sd['a'] = 10
print("SafeDict:", sd['a'])
print("Missing key:", sd['x'])


# 8. UserList — Custom list behavior


class LoggedList(UserList):
    def append(self, item):
        print("Adding:", item)
        super().append(item)

ll = LoggedList()
ll.append(10)
ll.append(20)
print("LoggedList:", ll)

# 9. UserString — Custom string behavior

class UpperString(UserString):
    def append(self, value):
        self.data += value.upper()

us = UpperString("hello")
us.append(" world")
print("UserString:", us)
