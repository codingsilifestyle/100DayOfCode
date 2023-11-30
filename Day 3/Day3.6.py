print("Welcome to the Love Calculater")
print("******************************")
name1 = input("Enter your Name:")
name2 = input("Enter your partner Name:")
count = 0
name1 = name1 + name2
name1 = name1.lower()
T = name1.count("t")
R = name1.count("r")
U = name1.count("u")
E = name1.count("e")
Trues = T + R + U + E
L = name2.count("l")
O = name2.count("o")
V = name2.count("v")
E = name2.count("e")

LOVE = L + V + O + E
LOVEs = int(str(Trues) + str(LOVE))