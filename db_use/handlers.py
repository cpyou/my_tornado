# -*- coding:utf8 -*-
from controllers.article import IndexHandler, DbHandler


# 自动映射已导入的controller
handlers = [(v.url, v) for k, v in locals().items() if not k.startswith('_')]
# print handlers
