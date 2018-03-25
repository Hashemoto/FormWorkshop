import time

class members():
    def __init__(self, name,age):
        self.name = name
        self.age = age

class post():
    def __init__(self,creator,title,body):
        self.creator = creator
        self.title = title
        self.body  = body
        self.time = time.ctime()
