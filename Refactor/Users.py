#Class for Users
class Users:
    #We keep track of created users in order to avoid name conflicts
    instances = []
    #Constructor
    def __init__(self,name: str,password: str) -> None:
        self.name = name
        self.__password = password
        #Match types for user
        self.typy_gr = {k: '0' for k in range(96)} #Group phase
        self.typy_p = {k: '0' for k in range(32)}  #Knockout Phase
        Users.instances.append(self)
    #Method for password check
    def checkpass(self,attempt: str) -> bool:
        if attempt == self.__password: return True
        else: return False
