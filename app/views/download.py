from tornado.web import RequestHandler, asynchronous
from tornado.httpclient import HTTPClient, HTTPResponse, AsyncHTTPClient


class DownloadHandler(RequestHandler):
    def get(self, *args, **kwargs):
        url = self.get_query_argument('url')
        filename = self.get_query_argument('filename', 'index.html')
        client = HTTPClient()
        resp: HTTPResponse = client.fetch(url, validate_cert=False)
        # print(resp.body)
        from app import BASE_DIR, os
        dir = os.path.join(BASE_DIR, 'static/downloads')
        with open(os.path.join(dir, filename), 'wb') as f:
            f.write(resp.body)
        self.write('下载成功')


class AsyncDownHandler(RequestHandler):

    def save(self, response: HTTPResponse):
        filename = self.get_query_argument('filename', 'index.html')
        from app import BASE_DIR, os
        dir = os.path.join(BASE_DIR, 'static/downloads')
        with open(os.path.join(dir, filename), 'wb') as f:
            f.write(response.body)
        self.write('下载并保存成功')
        self.finish()

    @asynchronous
    def get(self, *args, **kwargs):
        url = self.get_query_argument('url')
        client = AsyncHTTPClient()
        resp: HTTPResponse = client.fetch(url, self.save, validate_cert=False)
        # print(resp.body)
        self.write('开始下载')
