class Friend:
    friends_dict = {}
    def __init__(self, name):
        Friend.friends_dict[name] = 'No party...'
        self.name = name

    # returns the string with the last invite that the person has received 
    # with the right place, day and time
    show_invite = lambda self: Friend.friends_dict[self.name]    

        
class Party:
    '''Sends the invites to all friends.
    Each friend an instance of class Friend.'''
    def __init__(self, place):
        self.place = place
        self.observers = []

    def add_friend(self, friend):
        '''adds friend 'name' to the list of the 'observers' 
        (people, which will get the invitations, when the new party is scheduled)'''
        self.observers.append(friend)

    def del_friend(self, friend):
        '''remove 'friend' from the 'observers' list'''
        self.observers.remove(friend)

    def send_invites(self, date):
        '''sends the invites with the right day and time to the each person on the list of 'observers''''
        for i in self.observers:
            Friend.friends_dict[i.name] = f'{self.place}: {date}'


# Examples


party = Party("Midnight Pub")
nick = Friend("Nick")
john = Friend("John")
lucy = Friend("Lucy")
chuck = Friend("Chuck")

party.add_friend(nick)
party.add_friend(john)
party.add_friend(lucy)
party.send_invites("Friday, 9:00 PM")
party.del_friend(nick)
party.send_invites("Saturday, 10:00 AM")
party.add_friend(chuck)

john.show_invite() == "Midnight Pub: Saturday, 10:00 AM"
lucy.show_invite() == "Midnight Pub: Saturday, 10:00 AM"
nick.show_invite() == "Midnight Pub: Friday, 9:00 PM"
chuck.show_invite() == "No party..."


