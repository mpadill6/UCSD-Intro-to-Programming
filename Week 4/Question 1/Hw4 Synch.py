#Question 1 Multiprocess Synchronized
import multiprocessing #import multiprocessing libraries
import time
start= time.perf_counter() #used to measure processing time
  

#Define Functions and add 1 sec sleep
def add(x, y):
    time.sleep(1)
    return x + y
def subtract(x, y):
    time.sleep(1)
    return x-y
def multiply(x, y):
    time.sleep(1)
    return x * y
def divide(x, y):
    time.sleep(1)
    if y==0:
        raise ValueError('Cannot divide by zero!')
    return x / y
def modulus(x, y):
    time.sleep(1)
    return x % y
if __name__=='__main__': 
    process1=multiprocessing.Process(name='add',target=add,args=(10,5,))
    process2=multiprocessing.Process(name='subtract',target=subtract,args=(10,5,))
    process3=multiprocessing.Process(name='multiply',target=multiply,args=(10,5,))
    process4=multiprocessing.Process(name='divide',target=divide,args=(10,5,))
    process5=multiprocessing.Process(name='modulus',target=modulus,args=(10,5,))

#Start Functions
    process1.start()
    process2.start()
    process3.start()
    process4.start()
    process5.start()
#Join Functions
    process1.join()
    process2.join()
    process3.join()
    process4.join()
    process5.join()

finish=time.perf_counter()

print("Finished in", round(finish-start,2), "second(s)")



    
