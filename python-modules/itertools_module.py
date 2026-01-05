import itertools
import operator

# count – infinite counter
for i in itertools.count(1):
    print(i)
    if i == 5:
        break

# cycle – repeat elements infinitely
colors = ['red', 'green']
c = itertools.cycle(colors)
for _ in range(4):
    print(next(c))

# repeat – repeat same value
for x in itertools.repeat(10, 3):
    print(x)

# accumulate – running total
nums = [1, 2, 3, 4]
print(list(itertools.accumulate(nums)))            # sum
print(list(itertools.accumulate(nums, max)))       # max
print(list(itertools.accumulate(nums, operator.mul)))  # product

# chain – combine iterables
a = [1, 2]
b = [3, 4]
print(list(itertools.chain(a, b)))

# chain.from_iterable – flatten
nested = [[1, 2], [3, 4], [5]]
print(list(itertools.chain.from_iterable(nested)))

# compress – filter by selectors
data = ['A', 'B', 'C', 'D']
selectors = [1, 0, 1, 0]
print(list(itertools.compress(data, selectors)))

# dropwhile – drop until condition false
nums = [1, 2, 3, 4, 1]
print(list(itertools.dropwhile(lambda x: x < 3, nums)))

# takewhile – take until condition false
print(list(itertools.takewhile(lambda x: x < 4, nums)))

# filterfalse – opposite of filter
print(list(itertools.filterfalse(lambda x: x % 2 == 0, nums)))

# groupby – group consecutive elements
data = [('a', 1), ('a', 2), ('b', 3), ('b', 4)]
for key, group in itertools.groupby(data, key=lambda x: x[0]):
    print(key, list(group))

# islice – slice iterator
nums = range(10)
print(list(itertools.islice(nums, 2, 8, 2)))

# tee – duplicate iterator
it = iter([1, 2, 3])
a, b = itertools.tee(it, 2)
print(list(a))
print(list(b))

# zip_longest – zip uneven iterables
x = [1, 2]
y = ['a', 'b', 'c']
print(list(itertools.zip_longest(x, y, fillvalue=None)))

# product – cartesian product
print(list(itertools.product([1, 2], ['a', 'b'])))
print(list(itertools.product([0, 1], repeat=3)))

# permutations – ordered arrangements
print(list(itertools.permutations([1, 2, 3], 2)))

# combinations – unordered selection
print(list(itertools.combinations([1, 2, 3], 2)))

# combinations_with_replacement – allow repeat
print(list(itertools.combinations_with_replacement([1, 2, 3], 2)))

# starmap – map with unpacking
pairs = [(2, 3), (4, 5)]
print(list(itertools.starmap(operator.mul, pairs)))

# pairwise – consecutive pairs (Python 3.10+)
nums = [1, 2, 3, 4]
print(list(itertools.pairwise(nums)))

# batched – fixed size batches (Python 3.12+)
data = range(10)
print(list(itertools.batched(data, 3)))

# infinite iterator controlled by islice
counter = itertools.count(100)
print(list(itertools.islice(counter, 5)))
