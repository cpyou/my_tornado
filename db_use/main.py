import tornado.ioloop
import tornado.web
import tornado.options
import os
from tornado.options import options, define
from sqlalchemy.orm import scoped_session, sessionmaker
from core.db import engine, init_db
import logging
from handlers import handlers


class Application(tornado.web.Application):

    def __init__(self):

        settings = dict(
            debug=True,
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            template_path=os.path.join(os.path.dirname(__file__), "templates")
        )
        tornado.web.Application.__init__(self, handlers, **settings)
        self.db = scoped_session(sessionmaker(bind=engine,
                                              autocommit=False, autoflush=True,
                                              expire_on_commit=False))


def main():
    define("port", default=8000, help="run on the given port", type=int)
    tornado.options.parse_command_line()
    init_db()
    Application().listen(options.port, address='127.0.0.1')
    logging.info("running on 127.0.0.1:%s", options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    main()
