class Person:

    def __init__(self, name, address, telephone):
        self.__name = name 
        self.__address = address 
        self.__telephone = telephone

    def print_person(self):
        print("Name: ", self.__name, "\nAddress: ", self.__address, "\nTelephone: ", self.__telephone)



class Customer(Person):

    def __init__(self, name, address, telephone, cus_num, boo):
        Person.__init__(self, name, address, telephone)
        self.__cus_num = cus_num 
        self.__boo = boo

    def print_person(self):
        print("Name: ", self.__name, "\nAddress: ", self.__address, "\nTelephone: ", self.__telephone, "\nCustomer Number: ", self.__cus_num, "\nMailing List: ", self.__boo)

