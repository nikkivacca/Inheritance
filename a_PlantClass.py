
# Super class

class Plant:
    def __init__(self,color):
        self.__color = color


    def get_color(self):
        return self.__color

#Sub class

class Flower(Plant):
    def __init__(self,color, petals):
        Plant.__init__(self,color)     
        #calling init method of the super class because must create the super class before used in sub class
        self.__petals = petals

    def get_petals(self):
        return self.__petals
