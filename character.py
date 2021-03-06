# attributes of characters
# name :
# avatar (profile picture)
# inventory
# def do_stuff():
    
class Character():
    # in python - "dunder init" is the method used for how you define a constructor
    def __init__(self, new_name, new_avatar):
        # 'self' is the customary way to refer to the instance being built
        # in some other languages, they use 'this'
        self.name = new_name
        self.avatar = new_avatar
        self.inventory = []
    def greet(self, person=None):
        if person == None:
            return "Hello, I am %s!" % (self.name,)
        else:
            return "Hello %s, I am %s!" % (person.name, self.name)


# Hero is a type/kind of Character
# Hero is a subclass of Character
# Hero inherits from Character
# Character is the "super class" of Hero
# Character is the parent class of Hero
class Hero(Character):
    pass