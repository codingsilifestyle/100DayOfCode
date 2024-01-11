#Password Auth
import getpass
DataBase = {"Hussam" : "123" , "Ahmde" : "Ahmed123"}

def Auth(UserName , Password):
    for i in DataBase.keys():
        if i == UserName :
            while Password != DataBase.get(i):
                Password = getpass.getpass("Enter your password :")
            else:
                print("Verified")

UserName = input("Enter Your UserName: ")
Password = getpass.getpass("Enter Your Password")
Auth(UserName,Password)
    