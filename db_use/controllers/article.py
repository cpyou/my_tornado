# -*-coding:utf-8 -*-
# from tornado.httpclient import HTTPRequest, AsyncHTTPClient
from mod.tables import Article
from core.base_controller import BaseController
# import tornado.gen
# import urllib


class IndexHandler(BaseController):
    url = '/'

    def get(self):
        self.render('index.html')


class DbHandler(BaseController):

    url = '/db/'

    def get(self):
        data = self.db.query(Article).all()
        items = []
        for item in data:
            items.append(item.user)
        self.render('article.html', items=items)

# DbHandler()


class ArticleContorller(BaseController):

    def get(self):
        data = self.db.query(Article).all()
        for item in data:
            print item.content
