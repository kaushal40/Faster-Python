from time import perf_counter

def sum_using_for(n):
    sum = 0
    for i in range(n):
        sum += i
    return sum

def sum_suning_inbuilt(n):
    return sum(range(n))

if __name__ == '__main__':
    n = 1000000

    start = perf_counter()
    sum_using_for(n)
    duration = perf_counter() - start
    print("for loop time: ", duration)

    start = perf_counter()
    sum_suning_inbuilt(n)
    duration = perf_counter() - start
    print("inbuilt loop time: ", duration)


