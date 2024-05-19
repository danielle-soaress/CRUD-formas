from package.maths.CartesianPlane import CartesianPlane

class User():

    def __init__(self, name, nickname, password, email, privateEmail = False, age= None, ocupation = None):
        self.name = name
        self.nickname = nickname
        self.__password = password
        self.__email = email
        self.__privateEmail = privateEmail
        self.__age = age if age != None else "Not specified"
        self.__ocupation = ocupation if ocupation != None else "Not specified"
        self.cartesianPlane = CartesianPlane()


    def getName (self):
        return self.name

    def setName (self, newName):
        self.name = newName

    def setPassword (self, newPassword):
        self.name = newPassword

    def getEmail (self):
        return self.__email

    def setEmail (self, newEmail):
        self.name = newEmail
    
    def getAge (self):
        return self.__age

    def setAge (self, newAge):
        self.name = newAge
    
    def getOccupation (self):
        return self.__age

    def setOccupation (self, newOccupation):
        self.name = newOccupation
    
    def getCartesianPlane(self):
        return self.cartesianPlane
        
    def profile(self):
        return (
            f'Name: {self.name}\n' + 
            f'Nickname: {self.nickname}\n' +
            f'Age: {self.__age}\n' + 
            f'Ocupation: {self.__ocupation}\n' +
            (f'Email: {self.__email}\n' if self.__privateEmail == False else f'Email: Private\n')
        )
