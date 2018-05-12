import time, threading

# 新线程执行的代码:
def loop(number):
    print('thread %s is running...'% threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s %s>>> %s' % (threading.current_thread().name, number, n))
        time.sleep(1)
    print('thread %s ended.'% threading.current_thread().name )

print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop,args=(2,), name='LoopThread')
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)

