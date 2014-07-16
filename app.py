import tornado.ioloop
import tornado.web
import json
import time

class MainHandler(tornado.web.RequestHandler):

    @tornado.web.asynchronous
    def get(self):

        sender = self.get_argument('sender')
        receiver = self.get_argument('receiver')
        
        b = { 'sender': sender,
              'receiver': receiver,
              'message': 'hello' }
        
        self.write(json.dumps(b))
        self.finish()

    @tornado.web.asynchronous
    def post(self):

        sender = self.get_argument('sender')
        receiver = self.get_argument('receiver')

        print sender
        print receiver
        
        b = { 'sender': 'kykim',
              'receiver': 'cw',
              'message': 'hello' }
        
        self.write(json.dumps(b))
        self.finish()
        
application = tornado.web.Application([
        (r'/', MainHandler),
        ])

if __name__ == '__main__':
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
