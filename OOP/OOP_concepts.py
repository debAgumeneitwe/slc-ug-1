
class Animal:
   def __init__(self, name=''):
      self.name = name

   def talk(self):
      pass

#Cow class inherits from class Animal
class Cow(Animal):
   def talk(self):
      print "Mooooo!"

#Dog class inherits from Animal
class Dog(Animal):
   def talk(self):
      print "Woof!"


a = Animal()
a.talk()

c = Cow("diary")
c.talk()

d = Dog("Rocky")
d.talk()
####Both Dog and Cow class have differnt talk methods that give separate sounds when printed even though they inherit from Animal. Dog and Cow do not have to inherit everything from Animal. They can do some things differently. That is what we call polymorphism.

####encapsulation hides the implementation details of a class from other objects
###An attribute is a characteristic of an object. Attributes are set in the init() method. For example in this case name is an attribute.
##A method defines operations that we can perform with our objects. talk is a method
##Technically, attributes are variables and methods are functions defined inside a class.
###diary and rocky are instances of classes cow and Dod respectively