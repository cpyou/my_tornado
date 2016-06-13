# -*- coding: utf-8 -*-
import tornado.ioloop
import tornado.web
import tornado.options
from tornado.options import options, define
import logging
from tornado.httpserver import HTTPServer
from tornado import gen

import openerplib

HOST = '192.168.3.7'
PORT = 8069
DB = 'pzfresh_produce_db'
USER = 'admin'
PASS = ''

conn = openerplib.get_connection(hostname=HOST, port=PORT, protocol="jsonrpc", database=DB, login=USER, password=PASS)
model = conn.get_model('stock.move')
model_ids = model.search([])


@gen.coroutine
def get_odoo_rpc_data(total_num):

    model_res = model.read(model_ids[:total_num], [])

    return model_res


class MainHandler(tornado.web.RequestHandler):

    def get(self, *args, **kwargs):
        self.write("Hello World")

    @gen.coroutine
    def post(self, *args, **kwargs):
        total_num = self.get_argument('total_num', 1)
        model_res = yield get_odoo_rpc_data(int(total_num))
        # model_res = get_odoo_rpc_data(int(total_num))
        self.write({'model_res': model_res})
handlers = [
    ('/', MainHandler)
]


class Application(tornado.web.Application):

    def __init__(self):

        settings = dict(
            debug=False,
        )
        tornado.web.Application.__init__(self, handlers, **settings)


def main():
    define("port", default=33806, help="run on the given port", type=int)
    tornado.options.parse_command_line()
    server = HTTPServer(Application(), xheaders=True)
    # server.listen(options.port, address='127.0.0.1')
    server.bind(int(options.port))
    server.start(0)
    logging.info("running on 127.0.0.1:%s", options.port)
    tornado.ioloop.IOLoop.current().start()

if __name__ == '__main__':
    main()
