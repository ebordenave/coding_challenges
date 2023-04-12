import time

def fibonacci(n: int) -> int:
    # BASE CASE
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    prev1, prev2 = 1,0
    output = 0
    
    for idx in range(2,n+1):
        output = prev1 + prev2
        prev2 = prev1
        prev1 = output
    
    # RECURSIVE CASE
    # return fibonacci(n-1) + fibonacci(n-2)
    
    #(O)n
    return output


def elapsed_time(func: callable, *args, **kwargs):
    start_time = time.time()
    result = func(*args,**kwargs)
    end_time = time.time()
    elapsed_time = end_time - start_time
    return elapsed_time, result

print(elapsed_time(fibonacci, 30))
