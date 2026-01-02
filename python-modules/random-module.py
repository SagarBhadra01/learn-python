import random

random.seed(10)

# Generator state
state = random.getstate()

# Basic random
print(random.random())
print(random.uniform(1, 5))
print(random.randint(1, 10))
print(random.randrange(1, 20, 3))

# Sequence operations
data = [1, 2, 3, 4, 5]
print(random.choice(data))
print(random.choices(data, k=3))
print(random.sample(data, 3))
random.shuffle(data)
print(data)

# Distributions
print(random.gauss(0, 1))
print(random.normalvariate(0, 1))
print(random.expovariate(1.5))
print(random.betavariate(0.5, 0.5))
print(random.lognormvariate(0, 1))
print(random.triangular(1, 10, 5))
print(random.paretovariate(1.5))
print(random.weibullvariate(1, 2))

# Bits
print(random.getrandbits(8))

# Restore state
random.setstate(state)

# System-level randomness
sys_rand = random.SystemRandom()
print(sys_rand.randint(1, 100))
