import threading
import src.config as config

from time import sleep
from datetime import datetime, timedelta


class WorkerThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.tasks = []
        self.ids = [0]  # ids[0] = Generador de misiones

        self._running = True
        self.start()
        
    def run(self):
        while self._running:
            sleep(1)
            try:
                while len(self.tasks) and self.tasks[0]['time'] <= datetime.now():
                    task, args, kwargs = self.tasks[0]['func']
                    self.ids[self.tasks[0]['id']] = False
                    self.tasks = self.tasks[1:]
                    
                    try:
                        task(*args, **kwargs)
                    except Exception as e:
                        config.logging_error('No se ha ejecutado una tarea: ', e)
                
            except Exception as e:
                pass

    def put(self, time_of_execute, task, *args, **kwargs):
        '''
        :param time_of_execute: datetime
        '''
        
        def key(element):
            return element['time']
        
        _id = len(self.tasks) + 1
        now = datetime.now()
        execute_in = time_of_execute + now
        
        missions = []
        start = task.__name__ not in missions
       
        band = True 
        for i, value in enumerate(self.ids[start:]): 
            if not value:
                self.ids[i] = True
                _id = i
                band = False
                break
        
        if band: 
            self.ids.append(True)
        
        self.tasks.append({
            'id': _id,
            'time': execute_in,
            'func': [task, args, kwargs]
        })
        
        self.tasks.sort(key=key)
        return _id

    def pop(self, _id): 
        for i, t in enumerate(self.tasks): 
            if t['id'] == _id:
                self.ids[self.tasks['id']] = False
                self.tasks.pop(i)
                break

    def stop(self):
        self._running = False