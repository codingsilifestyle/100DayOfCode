#Caesar Cipher Encryption
def Encryption(Text,Shift):
    lenght = len(Text)
    Lenght_a = len(alphabet)
    for letter in Text: 
        if Shift == Lenght_a:
            Shift = 0
            print(alphabet[Shift])
            Shift+= 1
        else :
            print(alphabet[Shift-1])
            Shift+= 1

Direction  = input("Enter Decode or Decrypt:")
Text = input("ENter your Text :")
Shift = int(input("Enter Your Shift Number :"))

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
Encryption(Text=Text,Shift=Shift)
#################################
#           other way           #
#################################