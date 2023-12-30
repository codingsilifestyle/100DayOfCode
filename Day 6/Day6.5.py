def Ecnrypt(Text,Shift):
    Cipher = ""
    for letter in Text :
        Poisition = alphabet.index(letter)
        NewPoisition = Poisition + Shift
        NewLetter = alphabet[NewPoisition] 
        Cipher += NewLetter
    print(f"the encode text is {Cipher}")
    
    
def Decrypt(Text, Shift):
    Plain_Text = ""
    for letter in Text:
        Position = alphabet.index(letter)
        OldPosition = Position - Shift 
        Letters = alphabet[OldPosition]
        Plain_Text += Letters 
    print(f"the Decode is {Plain_Text}")
# end def    
##def main():
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
if direction == 'encode':
    Ecnrypt(text , shift)
 ##       main()
elif direction == 'decode':
    Decrypt(text, shift)
 ##       main()
