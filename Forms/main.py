import models



member1 = models.members('Hashem',28)
member2 = models.members('Tariq',29)
#    def __init__(self,creator,title,body,time):
post1 = models.post(member1.name,"test post", "test body")

post2= models.post(member2.name,"2nd post","another test post")

post3 = models.post(member2.name,"3rd post", " My other test post")
