from threading import*
#without multithreading
import time
def doubles(numbers):
    for n in numbers:
        time.sleep(1)
        print('double:', 2*n)
def squares(numbers):
    for n in numbers:
        time.sleep(1)
        print('square:',n*n)
numbers = [1,2,3,4,5,6]
begintime = time.time()
doubles(numbers)
squares(numbers)
print('the total time taken:',time.time()-begintime)
