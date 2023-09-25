import asyncio
import tornado

# `http://localhost:8000/get_meme?id=1`

visits = int(0)

class GetMemeHandler(tornado.web.RequestHandler):
    def get(self):
        x = self.get_query_argument("id", default="0")
        path = '..\dz1\memes\meme'+x+'.jpg'
        try:
            stream = open(path, 'rb')
            mem_dna = stream.read()
            self.write(mem_dna)
            stream.close()
        except:
            self.set_status(404)

class CountVisitsHandler(tornado.web.RequestHandler):
    def get(self):
        visits += 1
        try:
            self.write("That's {visits} visit!")
        except:
            self.set_status(404)

async def main():
    app = tornado.web.Application([(r"/get_meme", GetMemeHandler),
                                   (r"/count_visits", CountVisitsHandler)])
    app.listen(8888)
    await asyncio.Event().wait()

if __name__ == '__main__':
    asyncio.run(main())