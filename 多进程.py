import multiprocessing
import time
import os

def sing(active):
    print('主进程:', os.getppid())
    print('子进程',os.getpid())
    for i in range(3):
        print(active)
        time.sleep(1)

def dance(active):
    print('主进程:', os.getppid())
    print('子进程',os.getpid())
    for i in range(3):
        print(active)
        time.sleep(1)

if __name__ == '__main__':
    print('主进程:',os.getpid())
    # 多进程任务名不能加括号
    # 参数可以以args元组或者kwargs字典的形式传入
    singPro = multiprocessing.Process(target=sing,args=('唱歌',))
    dancePro = multiprocessing.Process(target=dance,kwargs={'active':'跳舞'})
    # 进程任务.daemon=True是子进程守护主进程，主进程一结束，在当前主进程下的所有子进程都会销毁
    singPro.daemon=True
    dancePro.daemon = True
    singPro.start()
    dancePro.start()
    time.sleep(1)


#     多线程。jion是阻塞主线程的不会阻塞子线程是说等子进程结束后主线程才继续向下走


