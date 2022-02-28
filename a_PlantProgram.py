import a_PlantClass as pc

primrose = pc.Plant("Green")

## have to have all arguments for it to work 
sunflower = pc.Flower("Yellow", 12)

print(primrose.get_color())

print(sunflower.get_color())
print(sunflower.get_petals())

## will not work because that is a method of the sub class 
## print(primrose.get_petals())
