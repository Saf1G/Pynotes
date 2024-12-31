#Day 8 and now complex if statements time
#First is combining many conditions in a if statement using 'and', 'or'
if 'e' in 'hello' and 2 != 3 or 5 < 10:
	print('Complex test')

#exercise complex if
money_avaible = 100
hungry = True
bored = True
#check if money avaible is greater than 80 and if hungry is true or if bored then print something 
if money_avaible < 80 and hungry == True or bored == True:
	print('Eat something fancy!')

#If statement nesting time
x = 5
if x == 5:
	y = 3
	if y == 3:
		print(5+2)
		if 5+2 != 9:
			z = 5

#Exercise 2
#Task do the previous exercise using nesting
money_avaible = 100
hungry = False
bored = True

if money_avaible > 80: #this runs coz condition is true
	print('I have money') 
	if hungry == True: #this wont run coz condition is false
		print('I am hungry') 
		if bored: #this condition is true but this wont run beceause the previous one is false so this stops
			print('I am bored') 


#Match case time

#Match statement is kinda similliar to if statement it also runs a code if a condition is true but it is designed to check for values from a long list
mood = 'tired'
match mood:
	case 'tired':
		print('Get sleep bozo')

# Exercise match case
#task : create a variable called grade which has values between 1-5 here 1 = very good 2 = good 3 = okay blah blah and add a default option if somehting is not there
grade = 1
match grade:
	case 1:
		print('Very good')
	case 2:
		print('Good')
	case 3:
		print('Okay')
	case 4:
		print('Needs imrpovement')
	case 5:
		print('Very bald')
	case _:
		print('No grades for u L')

#While loops time (important)
#While loop is a way to make a code run several or for some time for example while a certain condition is met the code will be run
x = 1
while x<3: #here the condition is while x = 1 is not greater than 3 it adds 1 to x and prints 123 so after 3 times X will be greater than 3 and then it will stop running
	x += 1
	print(10)
	if x == 2:
		print('Here if statements can aslo be combined with while loops')

while 2>10: #Here the condition is not met so the code print('Loop') won't run even once
	print('Loop')

# Complex while loops
#While loops can be stopped and could skip an iteration using the break and continue at the end for example

while x <5:
	print('1')
	x += 1
	if x == 4:
		break #here the loop stops before reaching x == 5

while x <5:
	print('1')
	x += 1
	if x == 4:
		continue #here the print is skipped because of continue
		print('Test loop')

#Exercise while loop
#Task use a while loop to create a list with only even values from 0 - 100 and do not add the value 58
 
exercise_list = []
counter = 0

while counter < 100:
	if counter % 2 == 0 and counter != 58:
		exercise_list.append(counter)
	counter += 1	

print(exercise_list)