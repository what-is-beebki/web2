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
        self.now = datetime.datetime.now()
    
    def set_deadline(self):
        deadline = datetime.datetime(self.now.year, self.now.month, self.now.day, 23, 59, 59)
        expire_time = (deadline - self.now).seconds
        return expire_time
    
    def get(self):
        
        if self.radish.exists('visits'):
            self.radish.incr('visits')
            if self.radish.ttl('visits') == -1:
                self.radish.delete('visits')
            
        if not self.radish.exists('visits'):
            self.radish.set('visits', 0)
            self.radish.expire('visits', self.set_deadline())
        try:
            self.write("That's {} visit!".format(self.radish.get('visits')))
        except:
            self.set_status(404)

async def main():
    app = tornado.web.Application([(r"/count_visits", CountVisitsHandler)]) 
    app.listen(8888)
    await asyncio.Event().wait()

if __name__ == '__main__':
    asyncio.run(main())
