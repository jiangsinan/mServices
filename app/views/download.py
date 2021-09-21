from tornado.web import RequestHandler
from tornado.httpclient import HTTPClient,HTTPResponse

class DownloadHandler(RequestHandler):
    def get(self, *args, **kwargs):
        url = self.get_query_argument('url')
        filename = self.get_query_argument('filename','index.html')
        client = HTTPClient()
        resp : HTTPResponse = client.fetch(url,validate_cert = False)
        # print(resp.body)
        from app import BASE_DIR,os
        dir = os.path.join(BASE_DIR,'static/downloads')
        with open(os.path.join(dir,filename) , 'wb') as f:
            f.write(resp.body)
        self.write('下载成功')