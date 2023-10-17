import asyncio
import tornado
import datetime
import redis

# Запуск:
# http://localhost:8888/count_visits

radish = redis.Redis(host='localhost', port=6379, decode_responses=True)
today = datetime.date.today()
#today = datetime.date(2002, 3, 11) # чтобы не ждать 0:00
radish.set('visits', 0)

class CountVisitsHandler(tornado.web.RequestHandler):
    def prepare(self):
        global radish
        self.radish = radish
        self.now = datetime.date.today()
    
    def NowIsToday(self):
        global today
        if self.now.isoformat()  == today.isoformat():
            return True
        else:
            today = datetime.date.today()
            return False
    
    def get(self):
        
        if not self.NowIsToday():
            #print('reset counter')
            self.radish.set('visits', 0)
        visits = self.radish.incr('visits')
        try:
            self.write("That's {} visit!".format(visits))
        except:
            self.set_status(404)

async def main():
    app = tornado.web.Application([(r"/count_visits", CountVisitsHandler)]) 
    app.listen(8888)
    await asyncio.Event().wait()

if __name__ == '__main__':
    asyncio.run(main())
