import queue
q = queue.Queue(10)
try:
    q.put('zhang')
    q.put(5)
    q.put(['wang','li'])
    print(q.get())
    print(q.get())
    print(q.get())
    queue.size()
    q.get_nowait()
except AttributeError:
    print("属性错误！")
except NameError:
    print("未定义成员！")