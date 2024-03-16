import turtle

#background set up
wn = turtle.Screen()
wn.bgcolor("blue")

#initialize variables and lists
move_counter = 0
spots = []
spots_counter = 1
for i in range(7):
  spots.append([])
for i in range(7):
  for j in range(6):
    spots[i].append(spots_counter)
    spots_counter += 1
column1 = []
column2 = []
column3 = []
column4 = []
column5 = []
column6 = []
column7 = []
column_tracker1 = 5
column_tracker2 = 5
column_tracker3 = 5
column_tracker4 = 5
column_tracker5 = 5
column_tracker6 = 5
column_tracker7 = 5
win = False

#Create column numbers
row_num = 1
x = -212.5
y = 125
font_setup = ("Arial", 20, "normal")
t = turtle.Turtle()
for num in range(7):
  t.hideturtle()
  t.penup()
  t.goto(x,y)
  t.write(row_num, font=font_setup)
  row_num += 1
  x += 50


#create columns
column_num = 1
x = -200
y = 100
for row in range(7):
  for column in range(6):
    spot = turtle.Turtle("circle")
    spot.color("white")
    spot.penup()
    spot.goto(x,y)
    y -= 50
    if column_num == 1:
      column1.append(spot)
    if column_num == 2:
      column2.append(spot)
    if column_num == 3:
      column3.append(spot)
    if column_num == 4:
      column4.append(spot)
    if column_num == 5:
      column5.append(spot)
    if column_num == 6:
      column6.append(spot)
    if column_num == 7:
      column7.append(spot)
  column_num += 1
  x += 50
  y = 100

#horizontal check
def horizontal_check(turn):
  global win
  if spots[x][y] == spots[x+1][y] == spots[x+2][y] == spots[x+3][y]:
    print(turn, "wins")
    win = True

#vertical check
def vertical_check(turn):
  global win
  if spots[x][y] == spots[x][y+1] == spots[x][y+2] == spots[x][y+3]:
    print(turn, "wins")
    win = True
    
#diagonal check - down left to right
def down_left_to_right(turn):
  global win
  if spots[x][y] == spots[x+1][y+1] == spots[x+2][y+2] == spots[x+3][y+3]:
    print(turn, "wins")
    win = True

def up_left_to_right(turn):
  global win
  if spots[x][y] == spots[x+1][y-1] == spots[x+2][y-2] == spots[x+3][y-3]:
    print(turn, "wins")
    win = True


#victory check
def victory_check(turn):
  global x 
  global y
  global spots
  global win
  x = 0
  y = 0
  for x in range(7):
    for y in range(6):
      if x <= 3:
        horizontal_check(turn)
      if y <= 2:
        vertical_check(turn)
      if x <= 3 and y <= 2:
        down_left_to_right(turn)
      if x <= 3 and y >=3:
        up_left_to_right(turn)
  if move_counter >= 42:
    print("Tie :/")
    win = True

#player move procedure
def player_move(yellow,red):
  global column_tracker1
  global column_tracker2
  global column_tracker3
  global column_tracker4
  global column_tracker5
  global column_tracker6
  global column_tracker7
  global choice
  if yellow == True and red == False:
    choice = input("Yellow, what column do you want to place?")
    while choice.isdigit() == False or 1 > int(choice) or int(choice) > 7:
      choice = input("That was not an integer between 0 and 7 (type 1,2,3 ...)")
    choice = int(choice)
    if choice == 1:
      column1[column_tracker1].color("yellow")
      spots[choice-1][column_tracker1] = "yellow"
      column_tracker1 -= 1
    if choice == 2:
      column2[column_tracker2].color("yellow")
      spots[choice-1][column_tracker2] = "yellow"
      column_tracker2 -= 1
    if choice == 3:
      column3[column_tracker3].color("yellow")
      spots[choice-1][column_tracker3] = "yellow"
      column_tracker3 -= 1
    if choice == 4:
      column4[column_tracker4].color("yellow")
      spots[choice-1][column_tracker4] = "yellow"
      column_tracker4 -= 1
    if choice == 5:
      column5[column_tracker5].color("yellow")
      spots[choice-1][column_tracker5] = "yellow"
      column_tracker5 -= 1
    if choice == 6:
      column6[column_tracker6].color("yellow")
      spots[choice-1][column_tracker6] = "yellow"
      column_tracker6 -= 1
    if choice == 7:
      column7[column_tracker7].color("yellow")
      spots[choice-1][column_tracker7] = "yellow"
      column_tracker7 -= 1
  if yellow == False and red == True:
    choice = input("Red, what column do you want to place?")
    while choice.isdigit() == False or (0 > int(choice) > 7) :
      choice = input("That was not an integer between 0 and 7 (type 1,2,3 ...)")
    choice = int(choice)
    if choice == 1:
      column1[column_tracker1].color("red")
      spots[choice-1][column_tracker1] = "red"
      column_tracker1 -= 1
    if choice == 2:
      column2[column_tracker2].color("red")
      spots[choice-1][column_tracker2] = "red"
      column_tracker2 -= 1
    if choice == 3:
      column3[column_tracker3].color("red")
      spots[choice-1][column_tracker3] = "red"
      column_tracker3 -= 1
    if choice == 4:
      column4[column_tracker4].color("red")
      spots[choice-1][column_tracker4] = "red"
      column_tracker4 -= 1
    if choice == 5:
      column5[column_tracker5].color("red")
      spots[choice-1][column_tracker5] = "red"
      column_tracker5 -= 1
    if choice == 6:
      column6[column_tracker6].color("red")
      spots[choice-1][column_tracker6] = "red"
      column_tracker6 -= 1
    if choice == 7:
      column7[column_tracker7].color("red")
      spots[choice-1][column_tracker7] = "red"
      column_tracker7 -= 1
    
#run the code
while win == False:
  player_move(True, False)
  move_counter += 1
  victory_check("yellow")
  if win == False:
    player_move(False, True)
    move_counter += 1
    victory_check("red")
wn.mainloop()