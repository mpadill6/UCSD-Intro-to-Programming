#Question 1 Concurrent
import concurrent.futures
import time

start=time.perf_counter()

#define functions
def add(x, y):
    print("This worked")
    return x + y
    print("This worked")
def subtract(x, y):
    return x-y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y==0:
        raise ValueError('Cannot divide by zero!')
    return x / y
def modulus(x, y):
    return x % y

if __name__=='__main__':
    with concurrent.futures.ProcessPoolExecutor() as exec:
        proc1=exec.submit(add,10,5)
        proc2=exec.submit(subtract,10,5)
        proc3=exec.submit(multiply,10,5)
        proc4=exec.submit(divide,10,5)
        proc5=exec.submit(modulus,10,5)

        print(proc1.result())
        print(proc2.result())
        print(proc3.result())
        print(proc4.result())
        print(proc5.result())
    finish=time.perf_counter()
    print("Finished in", round(finish-start,2), "second(s)")
    
        
