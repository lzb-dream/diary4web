import requests
from bs4 import BeautifulSoup
import httpx
import threading
import time
import queue
from concurrent.futures import ThreadPoolExecutor


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.62',
    'Referer': 'https://www.kuaidaili.com/free/inha/2/'
}
turn = True
q = queue.Queue()
def request(urls):
    global turn
    for url in urls:
        resp = requests.get(url,headers=headers)
        time.sleep(0.9)
        html = resp.text
        beau = BeautifulSoup(html,"html.parser")
        ipList = beau.select('tbody>tr>td:first-child')
        portList = beau.select('tbody>tr>td:nth-child(2)')
        httpList = beau.select('tbody>tr>td:nth-child(4)')
        for i in range(len(ipList)):
            ip = ipList[i].find_all (text= True)[0]
            http = httpList[i].find_all(text=True)[0].lower()
            port = portList[i].find_all(text=True)[0]
            IP = http+'://'+ip+':'+port
            q.put(IP)
    turn = False

proxyList = ['http://120.24.76.81:8123', 'http://117.114.149.66:55443', 'http://61.216.156.222:60808', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://61.216.156.222:60808', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://61.216.185.88:60808', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://121.13.252.58:41564', 'http://120.24.76.81:8123', 'http://121.13.252.61:41564', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://222.74.73.202:42055', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://183.236.232.160:8080', 'http://121.13.252.58:41564', 'http://222.74.73.202:42055', 'http://120.24.76.81:8123', 'http://183.236.232.160:8080', 'http://210.5.10.87:53281', 'http://120.24.76.81:8123', 'http://27.42.168.46:55481', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://183.236.232.160:8080', 'http://120.24.76.81:8123', 'http://27.42.168.46:55481', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://27.42.168.46:55481', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://121.13.252.60:41564', 'http://121.13.252.58:41564', 'http://120.24.76.81:8123', 'http://121.13.252.58:41564', 'http://61.216.185.88:60808', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://117.114.149.66:55443', 'http://210.5.10.87:53281', 'http://120.24.76.81:8123', 'http://121.13.252.61:41564', 'http://120.24.76.81:8123', 'http://121.13.252.62:41564', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://182.34.17.104:9999', 'http://120.24.76.81:8123', 'http://182.34.17.104:9999', 'http://120.24.76.81:8123', 'http://121.13.252.62:41564', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://27.42.168.46:55481', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://183.236.232.160:8080', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://121.13.252.60:41564', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://183.236.232.160:8080', 'http://121.13.252.60:41564', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://121.13.252.62:41564', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://183.236.232.160:8080', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://61.216.156.222:60808', 'http://117.114.149.66:55443', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://222.74.73.202:42055', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://182.34.17.104:9999', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://112.14.47.6:52024']
def test():
    while True:
        if not turn:
            return
        pro = q.get()
        url = 'https://www.baidu.com/'
        proxies = {
            "http://": f"{pro}",
        }
        status = httpx.get(url=url,proxies=proxies).status_code
        if status == 200:
            proxyList.append(pro)
rt1 = threading.Thread(target=request,args=([f'https://www.kuaidaili.com/free/inha/{p}/' for p in range(1,20)],))
rt1.start()
with ThreadPoolExecutor(max_workers=10) as pool:
    for i in range(10):
        futures = pool.submit(test)
        re = futures.result()
    print(proxyList)


# async def fetch(url):
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.62'
#     }
#     async with httpx.AsyncClient(headers=headers) as client:
#         resp = await  client.get(url)
#         status = resp.status_code
#         text = resp.text
#         if status==200:
#             print(text)
#
#
#
# async def main(urls):
#     tasks = []
#     for url in urls:
#         task = asyncio.create_task(fetch(url))
#         tasks.append(task)
#     await asyncio.wait(tasks)
# loop = asyncio.new_event_loop()
# asyncio.set_event_loop(loop=loop)
# loop.run_until_complete(main([f'https://www.kuaidaili.com/free/inha/{p}/' for p in range(1,10)]))
