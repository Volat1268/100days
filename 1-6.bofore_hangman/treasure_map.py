# 🚨 Don't change the code below 👇
row1 = ["⬜","⬜","⬜"]
row2 = ["⬜","⬜","⬜"]
row3 = ["⬜","⬜","⬜"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do You want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

col_row = list(position)

map[int(col_row[1]) - 1][int(col_row[0]) - 1] = 'X'




#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
# 🚨 Don't change the code below 👇
