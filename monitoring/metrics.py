import time

class Metrics:
    
    def __init__(self):
        self.start = None
    
    def begin(self):
        self.start = time.time()
    
    def finish(self):
        return time.time() - self.start