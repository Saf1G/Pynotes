#Day 9 for loop time!

for_loop1 = 1,2

for int in for_loop1: #here the print is run for every integar in the for_loop1 variable
	print(int)

for x in range(20,40,5): #range function is very much used in for loops 
	print(x)

# Exercise 
practice_list = [[10,40,20,50], [2,42,10], [101,12,4]]
#task : use a  for loop to print values under 60 skip the values below 10 and end the loop if a value is over 90

for nest_list in practice_list:  
	for value in nest_list:
		if value > 100:
			break
		if value < 50:
			if value < 10:
				continue 
				print(value) #here this is not getting printed because the conditions are not met


 
# Flow + Linebreaks time!
 #this is basically the flow and linebreak (indentation) in stuff for example

if 5>3: #instead of doing this
 	print('flow1')

if 5>3:print('flow2') #we can do this

#we can also use a  'ternary' operator to do simple stuff 

if 5<3:  #here for a simple statement we are using 4 lines of code instead we can do this
	print('okay')
else:
	print('not simple')

print('okay') if 5<3 else print('simple') #here this works same as the previous one and is much more simpler
#what to do   condition  else   what to do (template of ternary operator)

grade = 1    #this is a exercise which was done before
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

#it is much more simple if we do this
grade = 1     #both are the same
match grade: 
	case 1:print('Very good')
	case 2:print('Good')
	case 3:print('Okay')
	case 4:print('Needs imrpovement')
	case 5:print('Very bald')
	case _:print('No grades for u L')

#ternary operators also works on lists and f strings

color = 0 

ternary_example = color = 'blue' if 5<3 else 'red'
print(ternary_example)

#Function intro time!
#Functions are basically a block of code which can be reused
#This is just like creating a function

def test_function(): #a function will always start with def then we type the function name and it is basically a block of code which can be called multiple times
	x = 3
	while x<5:
		x += 1
		if x == 5:
			print('cool')

test_function()  #one thing to make sure is not to print it rather just call it like here otherwise we will get booga error

#another example (calculator)

def calculator(number1,number2): #here this is called a parameter and we can add arguements here
	result = number1 + number2 #note this variable only exists inside of this function
	print(result)

calculator(234,435) #and inside this parameter we can also add arguements which are number1 and number2 so here the 234+435 is basically def caluclator(number1,number2):
calculator(13,2)

# Exercise functions
#Task : make the previous calculator better and add a option to select +- 

def better_calculator(num1,num2,operation): 
	if operation == 'plus':
		print(num1+num2)
	elif operation == 'minus':
		print(num1-num2)
	elif operation == 'multiply':
		print(num1/num2)
	elif operation == 'power':
		print(num1**num2)	
	else:
		print('ERROR')	

better_calculator(3,8,'power') #plus minus and multiplication can be done with this calculator







