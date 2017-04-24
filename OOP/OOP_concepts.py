
class Animal:
    __num_of_legs = 0
    
    def __init__(self, name, move = ''):
       self.name = name
       self.__move = "walks"


    def make_sound(self):
       print ("mmmmm")
    
    def movement(self):
        self.__move = "walks"
       
#Cow class inherits from class Animal
class Cow(Animal):
   def make_sound(self):
      print ("Mooooo!")

#Dog class inherits from Animal
class Dog(Animal):
   def make_sound(self):
      print ("Woof!")
        
class Cockroach(Animal):
    def movement(self):
        self.__move = "crawls"
        print (self.__move)
        

c = Cow("diary")
c.make_sound()

d = Dog("Rocky")
d.make_sound()

s = Cockroach("roach")
s.make_sound()
s.movement()




"""Both Dog and Cow class have differnt talk methods that give separate sounds when printed even though they inherit from Animal. Dog and Cow do not have to inherit everything from Animal. They can do some things differently. That is what we call polymorphism.

-Encapsulation hides the implementation details of a class from other objects
-An attribute is a characteristic of an object. Attributes are set in the init() method. For example in this case name is an attribute.
-A method defines operations that we can perform with our objects. talk is a method
-Technically, attributes are variables and methods are functions defined inside a class.
-Diary and rocky are instances of classes cow and Dod respectively"""