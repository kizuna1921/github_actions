def sample(i):
    return i*2

print(sample(10))


def sample(func):
    return func(10)

print(sample(lambda i : i*2))

l = []
for x in range(10):
    l.append(x**2)
print(l)

l = list(map(lambda x: x**2, range(10)))
print(l)