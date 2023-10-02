import asyncio
import tornado

# Запуск:
# http://localhost:8888/count_visits
# http://localhost:8888/get_meme?id=1     # 0-7; otherwise error
# http://localhost:8888/get_meme          # 0 by default
# http://localhost:8888/show_doc

visits = int(0)

class GetMemeHandler(tornado.web.RequestHandler):
    def get(self):
        x = self.get_query_argument("id", default="0")
        path = '../dz1/memes/meme'+x+'.jpg'
        #self.write(path)
        try:
            with open(path, 'rb') as f:
                data = f.read()
                self.set_header("Content-Type", "image/jpeg") # класс работает
                self.write(data)
            self.finish()
        except:
            self.set_status(404)

class CountVisitsHandler(tornado.web.RequestHandler):
    def get(self):
        global visits
        visits += 1
        try:
            self.write("That's {} visit!".format(visits))
        except:
            self.set_status(404)

#class ShowDocHandler(tornado.web.RequestHandler):
    #def get(self):
        #path = '../dz1/index.html'
        #try:
            #with open(path, 'rb') as f:
                #data = f.read()
                #self.write(data)
            #self.finish()
        #except:
            #self.set_status(404)

async def main():
    app = tornado.web.Application([(r"/get_meme", GetMemeHandler),
                                   (r"/count_visits", CountVisitsHandler),
                                   (r"/show_doc", tornado.web.StaticFileHandler, {"path": '../dz1/index.html'})]) # оаоа не работает(((((((
                                   #(r"/show_doc", ShowDocHandler)])
    app.listen(8888)
    await asyncio.Event().wait()

if __name__ == '__main__':
    asyncio.run(main())
