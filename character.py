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
