import random
import asyncio
import httpx
from api.models import GourmetFood,Appointment,Family,Child
import datetime
import queue
import threading

q = queue.Queue()
sem = asyncio.Semaphore(30)
proxyList = ['http://120.24.76.81:8123', 'http://117.114.149.66:55443', 'http://61.216.156.222:60808', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://61.216.156.222:60808', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://61.216.185.88:60808', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://121.13.252.58:41564', 'http://120.24.76.81:8123', 'http://121.13.252.61:41564', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://222.74.73.202:42055', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://183.236.232.160:8080', 'http://121.13.252.58:41564', 'http://222.74.73.202:42055', 'http://120.24.76.81:8123', 'http://183.236.232.160:8080', 'http://210.5.10.87:53281', 'http://120.24.76.81:8123', 'http://27.42.168.46:55481', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://183.236.232.160:8080', 'http://120.24.76.81:8123', 'http://27.42.168.46:55481', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://27.42.168.46:55481', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://121.13.252.60:41564', 'http://121.13.252.58:41564', 'http://120.24.76.81:8123', 'http://121.13.252.58:41564', 'http://61.216.185.88:60808', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://117.114.149.66:55443', 'http://210.5.10.87:53281', 'http://120.24.76.81:8123', 'http://121.13.252.61:41564', 'http://120.24.76.81:8123', 'http://121.13.252.62:41564', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://182.34.17.104:9999', 'http://120.24.76.81:8123', 'http://182.34.17.104:9999', 'http://120.24.76.81:8123', 'http://121.13.252.62:41564', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://27.42.168.46:55481', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://183.236.232.160:8080', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://121.13.252.60:41564', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://183.236.232.160:8080', 'http://121.13.252.60:41564', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://121.13.252.62:41564', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://183.236.232.160:8080', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://61.216.156.222:60808', 'http://117.114.149.66:55443', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://222.74.73.202:42055', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://182.34.17.104:9999', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://120.24.76.81:8123', 'http://112.14.47.6:52024']

imageList = []
async def spendRequest(p):
    headers = {
        'referer': 'https://www.pexels.com/zh-cn/search/%E8%82%89/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.46',
        'secret-key': 'H2jk9uKnhRmL6WPwh89zBezWvr',
        'sentry-trace': '087c21f6745b4142bad8140bbcbc5691-9e04c830633c790f-0'
    }
    ip = random.choice(proxyList)
    proxies = {
        'http://': ip
    }
    # 美食230
    url1 = f'https://www.pexels.com/zh-cn/api/v3/search/photos?page={p}&per_page=24&query=%E7%BE%8E%E9%A3%9F&orientation=all&size=all&color=all&seo_tags=true'
    # 食物 240
    url2 = f'https://www.pexels.com/zh-cn/api/v3/search/photos?page={p}&per_page=24&query=%E9%A3%9F%E7%89%A9&orientation=all&size=all&color=all&seo_tags=true'
    # 肉 150
    url3 = f'https://www.pexels.com/zh-cn/api/v3/search/photos?page={p}&per_page=24&query=%E8%82%89&orientation=all&size=all&color=all&seo_tags=true'

    # 女人
    url4 = f'https://www.pexels.com/zh-cn/api/v3/search/photos?page={p}&per_page=24&query=%E5%A5%B3%E4%BA%BA&orientation=all&size=all&color=all&seo_tags=true'

    # 约会(相约) 230
    url5 = f'https://www.pexels.com/zh-cn/api/v3/search/photos?page={p}&per_page=24&query=%E7%BA%A6%E4%BC%9A&orientation=all&size=all&color=all&seo_tags=true'
    # 家庭 240
    url6 = f'https://www.pexels.com/zh-cn/api/v3/search/photos?page={p}&per_page=24&query=%E5%AE%B6%E5%BA%AD&orientation=all&size=all&color=all&seo_tags=true'
    # 孩子240
    url7 = f'https://www.pexels.com/zh-cn/api/v3/search/photos?page={p}&per_page=24&query=%E5%AD%A9%E5%AD%90&orientation=all&size=all&color=all&seo_tags=true'
    async with sem:
        async with httpx.AsyncClient(headers=headers,proxies=proxies) as client:
            resp = await client.get(url7)
            data = resp.json()
            for i in data['data']:
                attributes = i['attributes']
                image = attributes['image']
                mediumImage = image['medium']
                largeImage = image['large']
                result = {'minimage': mediumImage, 'maximage': largeImage}
                q.put(result)
                print(result)

async def tasks():
    return await asyncio.gather(*[spendRequest(p) for p in range(1, 241)])

def run():
    asyncio.run(tasks())

import time
def jia():
    while True:
        print('添加')
        data = q.get()
        try:
            addtime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            Child(maximage=data['maximage'],addtime=addtime,minimage=data['minimage']).save()
            print('添加成功')
        except:
            print('添加数据库失败循环下一次')
            continue
        if q.empty():
            time.sleep(2)
            if q.empty():
                print('完成')
                return
def main():
    getT = threading.Thread(target=run)
    jiaT = threading.Thread(target=jia)
    getT.start()
    jiaT.start()

from rest_framework.views import APIView,Response
class Add(APIView):
    def get(self,request):
        main()
        return Response({'成功':'11234'})















# import asyncio
# sem = asyncio.Semaphore(1)
# async def fetch(url):
#     proxies = {
#         "http://": 'http://121.8.215.106:9797',
#     }
#     async with sem:
#         async with httpx.AsyncClient(proxies=proxies) as client:
#             response = await client.get(url)
#             status = response.status_code
#             if status == 429:
#                 print(response.status_code)
#             imageHTML = response.text
#             imageRule = re.compile(r'id="wallpaper" src="(.*?)"',re.S)
#             image = imageRule.findall(imageHTML)
#             if len(image)> 0 and image[0]:
#                 print(image[0])
#                 imageList.append(image[0])
#
#
# async def main(urls):
#     return await asyncio.gather(*[fetch(url) for url in urls])
#     # return await asyncio.create_task(*[fetch(url) for url in urls])
# # loop = asyncio.new_event_loop()
# # asyncio.set_event_loop(loop=loop)
# # results = loop.run_until_complete(main(rehref))
# g = time.time()
#
# results = asyncio.run(main(rehref))
# print(time.time()-g)
# print(len(imageList),imageList)




# async def fetch(client, url):
#     response = await client.get(url)
#     print(response.status)
#     text = await response.text
#     return len(text)
#
#
# # urls是包含多个url的列表
# async def fetch_all(urls):
#     async with httpx.AsyncClient(proxies=proxies) as client:
#         return await asyncio.gather(*[fetch(client, url) for url in urls])