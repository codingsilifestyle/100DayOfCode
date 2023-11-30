row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
maps = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
Row = int(position[0])
Col = int(position[1])
maps[Row - 1][Col - 1] = 'X'
print(f"{row1}\n{row2}\n{row3}")