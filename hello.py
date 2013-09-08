import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("You requested the main page")

class StoryHandler(tornado.web.RequestHandler):
    def get(self, story_id):
        self.write("You requested the story %s" % story_id )

class MyFormHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('<html><body><form action="/myform" method="post">'
                   '<input type="text" name="message">'
                   '<input type="submit" value="submit">'
                   '</form></bory></html>')

    def post(self):
        self.set_header("Content-Type", "text/plain")
#        self.write("You worte " + self.get_argument("message"))
        self.redirect('/some-canonical-page', permanent=Ture)

#application = tornado.wsgi.WSGIApplication([
#    (r"/([a-z]*)", ContentHandler),
#    (r"/static/tornado-0.2.tar.gz", tornado.web.RedirectHandler,
#    dict(url="https://github/downloads/facsbook/tornado/tornado-0.2.tar.gz")),], **settings)

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/story/([0-9]+)", StoryHandler),
    (r"/myform", MyFormHandler)
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
