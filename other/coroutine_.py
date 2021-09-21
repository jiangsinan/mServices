import requests
import asyncio

@asyncio.coroutine
def download(url):
    resp = requests.get(url)
    print('正在下载')
    return resp.content,resp.status_code

@asyncio.coroutine
def save(url,filename):
    content,code = yield from download(url)
    print(url,code)
    yield from write_file(filename,content)
    print('保存成功')


async def write_file(filename,content):
    with open(filename,'wb') as f:
        f.write(content)

if __name__ == '__main__':
    ioloop = asyncio.get_event_loop()
    ioloop.run_until_complete(asyncio.wait([
        save('https://www.baidu.com','baidu.html'),
        save('https://jd.com','jd.html'),
        save('https://mail.qq.com','qq_mail.html'),
    ]))
