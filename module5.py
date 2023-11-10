from module4 import fibonacci  # here we import a function fibonacci from another file named "module4.py"
import timeit
# the first 100 Fibonacci numbers
first_100_fib_number=fibonacci(100)
print("frist Hundred Fibonacci number",first_100_fib_number)
# Measure the time it takes to generate 100 Fibonacci numbers using timeit
time_taken = timeit.timeit(lambda: fibonacci(100), number=1000)
time_taken=time_taken/1000  # Average time over 1000 runs
print(f"Time taken to generate 100 Fibonacci numbers: {time_taken:.5} seconds")
