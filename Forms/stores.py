class MembersStore():

    all_members=[]
    lastid=1

    def get_all(self):# get all members
        if len(MembersStore.all_members) ==0:
            return "No Members registered yet!"
        return MembersStore.all_members

    def add(self,member):#print member
        if self.entity_exists(member):
            return "Member is already exists."
        else:
            MembersStore.all_members.append([member.name,member.age,MembersStore.lastid])
            MembersStore.lastid +=1
            #member.id = MembersStore.lastid
            return "New member created."

    def get_by_id(self, id): # search for member by id
        if len(MembersStore.all_members) == 0:
            return False #"No Members registered yet!"
        for p in MembersStore.all_members:
            if id == p[2]:
                return p #"Member {} was found".format(p[0])
        return False #"No member with such ID"

    def entity_exists(self,member): # checks if an entity exists in a store
        value=0
        for x in MembersStore.all_members:
            if member.name in x:
                print member.name
                value=1
                print "Member Name {} was found with ID #{}.".format(x[0],x[2])
        if value ==1:
            return True
        else:
            return False # "Member does not exists."

#    def update(self, member):
         # update member data

    def delete(self, id): # delete member by id
        if self.get_by_id(id):
            MembersStore.all_members.remove(self.get_by_id(id))
            return "Member with ID # {} was Deleted".format(id)
        return "No member with such ID"
