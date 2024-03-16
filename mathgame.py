from random import randint
import math

#initialize variables
score = 0
counter = 0
numbers = []
correct = True
operator = 0
increment = 0

#Make list of starting numbers
print("Try to do this without any paper or tools. It is a mental arithmetic/memorization game")
number_total = input("How many numbers do you want to work with? (1,2,3...)")
while number_total.isdigit() == False:
  number_total = input("That was not a positive integer (type 1,2,3 ...)")
else:
  number_total = int(number_total)
for num_value in range(number_total):
  num_value = randint(0,100)
  numbers.append(num_value)
  print("The " + str(numbers.index(num_value)) + " number value is " + str(num_value))

#Function that changes the elements and checks answers
def number_change(operator, increment, check):
  global numbers
  global score
  global correct
  if operator == 1:
    numbers = [num_value + increment for num_value in numbers]
    print(increment , " was added to each number")
    return (numbers)
  if operator == 2:
    numbers = [num_value - increment for num_value in numbers]
    print(increment , " was subtracted from each number")
    return (numbers)
  if check == 1:
    print("For the ", str(question_value) , " number . . . ")
    answer = input("What is the new value of that number now?")
    if answer.lstrip("-").isdigit() == False:
      answer = input("That was not an integer (type 1,2,3 ...)")
    if numbers[question_value] == int(answer):
      print("correct")
      score += 1
      return (score)
    else: 
      print("incorrect")
      print("You got " , score , " correct")
      correct = False
      return (correct)

#Loop for calling the function
while correct == True:
  operator = randint(1,2)
  increment = randint(0,100)
  number_change(operator,increment, 0)
  question_value = randint(0,(number_total-1))
  number_change(0,0,1)
  
#show the correct answers
print("The current numbers were")
print(numbers)
exit()