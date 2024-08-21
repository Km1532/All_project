print("Enter the cell in the form of a letter from the right and then from the left side, lead only with a capital letter")
s = 'abcdefgh'
coord_1 = input()
coord_2 = input()
letter = coord_1[0]
letter2 = coord_2[0]
column1 = s.find(letter)
column2 = s.find(letter2)
row1 = int(coord_1[1])
row2 = int(coord_2[1])
if ((row1 + column1)) % 2 == 0 and (row2 + column2) % 2 == 0 or (row1 + column1) % 2 == 1 and (row2 + column2)% 2 == 1:
   print("White")
else:
   print("Black")


