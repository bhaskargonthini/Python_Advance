import threading
# class X(threading.Thread):
#     def run(self):
#         for p in range(1,20):
#             print(p)
# class Y(threading.Thread):
#     def run(self):
#         for q in range(21, 30):
#             print(q)
# x = X()
# y = Y()
# x.start()
# y.start()
class X(threading.Thread):
    def run(self):
        myfunc()
class Y(threading.Thread):
    def run(self):
        myfunc()
def myfunc():
    for p in range(1, 21):
        print(p)
x = X()
y = Y()
x.start()
y.start()