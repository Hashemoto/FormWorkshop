import models
import time
import stores


#memeber_testing.append(memebr1.name)

member1 = models.members('Hashem',28)
member2 = models.members('M',29)
member3 = models.members('B',29)
member4 = models.members('M',30)
member5 = models.members('riq',29)
member6 = models.members('iq',29)
post1 = models.post(member1.name,"The First Usefull post", "Some text in the body of this post\nWill be for sure USEFULL")
post2= models.post(member2.name,"The 2nd Usefull post","Another text in the body of this post\nWill be for sure USEFUL")
post3 = models.post(member2.name,"The 3rd Usefull post", "Third post with some text in the body of this post\nWill be for sure USEFUL")

member_store1 = stores.MembersStore()

#print member1.id
member_store1.add(member1)
member_store1.add(member2)
member_store1.add(member3)
member_store1.add(member4)
#member_store1.add(member5)
#member_store1.add(member6)
print member_store1.entity_exists(member1)
#print member_store1.get_by_id(4)
#print member_store1.delete(1)
#print member_store1.delete(1)
#print member_store1.get_by_id(1)
#print member_store1.get_all()
