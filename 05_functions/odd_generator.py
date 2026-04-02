def odd_generator(limit):
    for i in range(3, limit + 1, 2):
        yield i

for num in odd_generator(10):
    print(num)