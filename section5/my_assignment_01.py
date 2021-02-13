"""
Define a class hierarchy representing animals with a parent class Animal
and child classes such as dog, fish and bird. Each subclass animal should have
a name and an age and should have 2 methods defined in it: move(), eat().
The move method needs to be specific for a given animal where as the
eat() method should be generic for all animals. The methods don't need to
do anything except print information about who is doing what.

After creating the class hierarchy, create instances of each of the 3 animals
dog, fish and bird and make them eat and move.

"""

class Animal:

    def __init__(self):
        print("Animal constructed!")

    def move(self):
        print("Animal moving")

    def eat(self):
        print("Animal eating")

class Bird(Animal):

    def __init__(self, bird_name, bird_age):
        Animal.__init__(self)
        self.name = bird_name
        self.age  = bird_age
        print('Bird '+ self.name + ' Constructed!')

    def move(self):
        print("Bird flying...")

class   Parrot(Bird):

    def __init__(self, bird_name, bird_age):
        Bird.__init__(self, bird_name, bird_age)
        # self.name = bird_name
        # self.age  = bird_age
        print('Parrot '+self.name+ ' Constructed!')

    def talk(self):
        print(str(self.name)+" says 'You are a dork!'")


class Fish(Animal):

    def __init__(self, fish_name, fish_age):
        Animal.__init__(self)
        self.name = fish_name
        self.age  = fish_age

    def move(self):
        print("Fish swimming...")

class Dog(Animal):

    def __init__(self, dog_name, dog_age):
        Animal.__init__(self)
        self.name = dog_name
        self.age  = dog_age
    
    def move(self):
        print("Dog running...")

# my_dog = Dog('Fido', 7)
# print(my_dog.name)
# my_dog.move()
# my_dog.eat()

mango = Parrot('Mango', 25)
print(mango.name)
mango.move()
mango.talk()


