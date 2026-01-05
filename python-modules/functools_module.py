from functools import (
    reduce,
    partial,
    lru_cache,
    wraps,
    total_ordering,
    singledispatch,
    singledispatchmethod,
    cmp_to_key,
    cached_property
)

# reduce – cumulative operation
nums = [1, 2, 3, 4]
result = reduce(lambda a, b: a + b, nums)
print(result)

# partial – fix some arguments
def power(base, exp):
    return base ** exp

square = partial(power, exp=2)
cube = partial(power, exp=3)

print(square(5))
print(cube(3))

# lru_cache – memoization
@lru_cache(maxsize=128)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(10))
print(fib.cache_info())
fib.cache_clear()

# wraps – preserve metadata in decorators
def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Before function")
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def greet(name):
    """Greet user"""
    print("Hello", name)

greet("Sagar")
print(greet.__name__)
print(greet.__doc__)

# total_ordering – auto-generate comparisons
@total_ordering
class Student:
    def __init__(self, marks):
        self.marks = marks

    def __eq__(self, other):
        return self.marks == other.marks

    def __lt__(self, other):
        return self.marks < other.marks

s1 = Student(90)
s2 = Student(95)

print(s1 < s2)
print(s1 >= s2)

# singledispatch – function overloading
@singledispatch
def show(value):
    print("Default:", value)

@show.register(int)
def _(value):
    print("Integer:", value)

@show.register(list)
def _(value):
    print("List:", value)

show(10)
show([1, 2, 3])
show("hello")

# singledispatchmethod – method overloading
class Printer:
    @singledispatchmethod
    def print_data(self, value):
        print("Default:", value)

    @print_data.register(int)
    def _(self, value):
        print("Integer:", value)

    @print_data.register(str)
    def _(self, value):
        print("String:", value)

p = Printer()
p.print_data(5)
p.print_data("Hi")

# cmp_to_key – custom sorting
def compare(a, b):
    return b - a   # descending

nums = [5, 1, 3, 2]
nums.sort(key=cmp_to_key(compare))
print(nums)

# cached_property – cache class property
class Data:
    def __init__(self, x):
        self.x = x

    @cached_property
    def square(self):
        print("Calculating...")
        return self.x * self.x

d = Data(4)
print(d.square)
print(d.square)  # cached
