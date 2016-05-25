# from tornado.httpclient import HTTPRequest, AsyncHTTPClient
from mod.databases.tables import Article
from base_controller import BaseController
# import tornado.gen
# import urllib


class DbHandler(BaseController):

    def get(self):
        data = self.db.query(Article).all()
        for item in data:
            print item.content


class ArticleContorller(BaseController):

    def get(self):
        data = self.db.query(Article).all()
        for item in data:
            print item.content
