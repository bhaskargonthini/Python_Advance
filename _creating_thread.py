#creating a thread without using a class
from threading import*
# def display():
#     for i in range(1, 11):
#         print('child Thread')
# t = Thread(target = display) #creating thread object
# t.start()
# for i in range(1, 11):
#     print('main thread')
#creating a thread by extending class
# from threading import*
# class MyThread(Thread):
#     def run(self):
#         for i in range(10):
#             print('child thread-1')
# t = MyThread()
# t.start()
# for i in range(10):
#     print('main Thread-1')
from threading import*
class Test:
    def display(self):
        for i in range(10):
            print('child thread-2')
obj = Test()
t = Thread(target = obj.display)
t.start()
for i in range(10):
    print('main Thread-2')