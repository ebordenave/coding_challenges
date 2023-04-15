import time


def fibonacci(n: int) -> int:
    # BASE CASE
    if n == 0:
        return 0
    if n == 1:
        return 1

    fib_table = [0] * (n + 1)
    fib_table[1] = 1

    for idx in range(2, n+1):
        fib_table[idx] = fib_table[idx - 1] + fib_table[idx - 2]

    return fib_table


def elapsed_time(func: callable, *args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    elapsed_time = end_time - start_time
    return elapsed_time, result


print(elapsed_time(fibonacci, 8))
