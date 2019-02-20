# these arent real tests
from character import Character

# Characters can be instantiated with name and avatar

ayra = Character("Ayra Stark", "PHOTO.png")
jon = Character("Jon Snow", "SUPERPHOTO.png")
print(jon.name, jon.avatar, ayra.name, ayra.avatar)

print(jon.inventory)

jon.inventory.append("CAT")
jon.inventory.append("Valayrian steel")
print(jon.inventory)
print(jon.greet)git 