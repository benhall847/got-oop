# these arent real tests
from character import Character
from character import Hero
# Characters can be instantiated with name and avatar

ayra = Character("Ayra Stark", "PHOTO.png")
jon = Character("Jon Snow", "SUPERPHOTO.png")
print(jon.name, jon.avatar, ayra.name, ayra.avatar)

print(jon.inventory)

jon.inventory.append("CAT")
jon.inventory.append("Valayrian steel")

# should print ...
print(jon.inventory)

# it should print ...
print(ayra.greet(jon))

# should print without "hello i am.."
print(ayra.greet())

# i should be able to create a hero instance
Giant_Cat = Hero("Giant Cat from beyond the wall", "cat.png")
