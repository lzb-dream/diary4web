
import queue
import threading
import time

q = queue.Queue()

# async def a():
#     async with sem:
#         print('a开始')
#         await asyncio.sleep(1)
#         print('a结束了')
#
#
# async def b():
#     print('b开始')
#     await asyncio.sleep(1)
#     print('b结束了')
#
# async def main():
#     tasks = []
#     task1 = asyncio.create_task(a())
#     task2 = asyncio.create_task(b())
#     task3 = asyncio.create_task(a())
#     tasks.append(task1)
#     tasks.append(task2)
#     tasks.append(task3)
#     await asyncio.wait(tasks)
#
# def gh():
#     asyncio.run(main())
#
# def l():
#     time.sleep(1)
#     print('正常函数')

# t1 = threading.Thread(target=gh)
# t2 = threading.Thread(target=l)
# t1.start()
# t2.start()

# 时间
import datetime,time
newTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(newTime)
# times = (datetime.datetime.now()+datetime.timedelta(days=1,seconds=2000)).strftime("%Y-%m-%d %H:%M:%S")
# print(times)
#
# time_stamp = time.mktime(time.strptime(times, '%Y-%m-%d %H:%M:%S'))
# print(time_stamp)
# print(time.time())








