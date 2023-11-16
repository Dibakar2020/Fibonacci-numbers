# frist ten Fibonacci number

def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence)<n:
        next_fib_number=fib_sequence[-1]+fib_sequence[-2]
        fib_sequence.append(next_fib_number)
    return fib_sequence
#for printing 1st ten fibonacci number
first_ten_fib_number=fibonacci(10)
print("frist ten Fibonacci number",first_ten_fib_number)
