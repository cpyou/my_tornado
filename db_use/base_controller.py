import tornado.web


class BaseController(tornado.web.RequestHandler):

    def data_received(self, chunk):
        pass

    @property
    def db(self):
        return self.application.db
