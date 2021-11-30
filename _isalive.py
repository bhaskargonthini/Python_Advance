from threading import*
import time
def display():
    print(current_thread().getName(),'...started')
    time.sleep(3)
    print(current_thread().getName(),'....ended')
print('the number of active threads:',active_count())
t1 = Thread(target=display, name='child thread1')
t2 = Thread(target=display,name='child thread2')
# t3 = Thread(target=display, name='child thread3')
t1.start()
t2.start()
print(t1.name,'is Alive:',t1.isAlive())
print(t2.name,'is Alive:',t2.isAlive())
time.sleep(5)
print(t1.name,'is Alive:',t1.isAlive())
print(t2.name,'is Alive:',t2.isAlive())

