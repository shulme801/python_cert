class Boat:

    def __init__(self):
        print("\nBoat constructed!")

    def move(self):
        print("\nI have right of way!!")

class SailBoat(Boat):

    def __init__(self,boat_name,boat_length):
        Boat.__init__(self)
        self.name    = boat_name
        self.length  = boat_length
    
    def announce_name(self, my_name):
        print("I am the good ship {0}".format(my_name))

    def announce_length(self, my_name, my_length):
        print("I am the good ship {0} and my length is {1}".format(my_name, my_length))

my_boat = Boat()
my_boat.move()

my_sailboat = SailBoat("Shamrock", 37)
my_sailboat.move()
my_sailboat.announce_name(my_sailboat.name)
my_sailboat.announce_length(my_sailboat.name, my_sailboat.length)
