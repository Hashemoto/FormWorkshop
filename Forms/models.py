import time

class members():
    def __init__(self, name,age):
        self.name = name
        self.age = age
        self.id = id =0

    def __str__(self):
        return self.name,self.age,self.id

class post():
    def __init__(self,creator,title,body):
        self.creator = creator
        self.title = title
        self.body  = body
        self.time = time.ctime()

    def __str__(self):
        return "This post was created by {} on {} \n {} \n Body:\n {}".format(self.creator,self.time,self.title,self.body)
