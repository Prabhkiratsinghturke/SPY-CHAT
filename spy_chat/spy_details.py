from datetime import datetime               # this statement impot the date time  library

class Spy:                                      # here,spy is a class name

    def __init__(self, name, salutation, age, rating):          # here 'self' is a constructor for spy
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None




class ChatMessage:                            # here 'ChatMessage' is also a class name.....

    def __init__(self,message,sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me




spy = Spy('Mika', 'Mr.', 44, 4.7)           #default values....




friend_one = Spy('Salman', 'Mr.',  40,5)      #default friends info.....
friend_two = Spy('Akshay', 'Ms.',  25,2.5)
friend_three = Spy('Aman', 'Dr.', 35,4.2)




friends = [friend_one, friend_two, friend_three]            # list of friends....