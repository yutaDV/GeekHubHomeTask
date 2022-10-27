#створити репозитарый на GitHub
def my_range(start: int, stop: int, step=1):

    if step == 0:
        raise Exception('arg 3 must not be zero')
    result = ()
    while start <= stop:
        result += tuple(start)
        start += step
    yield result


for i in my_range(1, 10, 2):
    print(i)
