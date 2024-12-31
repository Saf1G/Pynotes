#Day 11 and functions and scope time! (Useful)
#variables created inside a function is called local scope and if we create a variable outside a function it is called global scope

test_var = 5 #here this is a global variable

def scope_test1():
	print(test_var) #here everything is fine because we are just printing the value of test_var

scope_test1()

#def scope_test2():
#	test_var += 1
#	print(test_var) #but here stuff is not fine because we are trying to change the value of a variable which does not exist inside here

#scope_test2()

def scope_test3():
	test_var = 123  #here the test_var is = 123 and it is a local scope but up we have a global test_var scope which is = 5 here this only exists inside of this function
	print(test_var)

scope_test3()

# We can use a global variable and modify it if we use the global parameter for example

def scope_global(): #here we can modify the global test_var inside of the function by using the global function but using parameters are generally better
	global test_var
	test_var += 5
	print(test_var)

scope_global()

def better_scope_global(test_var): #here we can use the global test_var by adding test_var as a parameter in the function and in the arguements
	test_var += 15
	print(test_var)

better_scope_global(test_var)

#Exercise
#Create 2 variables 'multiplier' its value should be any integar and 'has_calculated' its value should be False
#then create a function called multiply_calculator which that takes one arguement and calculates the multiplication of that number
#inside of the function multiply the parameter with the global variable 'multiplier'
#once the calculation is done set 'has_calculated' to true
#store that new number in a variable called 'result' and return it
#print the return value of the function (after it was called with that number)

multiplier = 10
has_calculated = False

#note return function ends the execution of the code

def multiply_calculator(number1):
	global has_calculated #here we set the has_calculated to global so we can change it to true
	result = multiplier*number1 #we multiply the number1 with the global multiplier variable
	has_calculated = True #we set the value of has_calculated to true
	return result #we return the result

print(multiply_calculator(3)) #here we print the function instead of calling it because we returned the value of result
print(has_calculated) #we check if the has_calculated is set to true or not

#Lambda function really important
#lambda is basically a function in a single line
#it goes like these lamba parameter: what to do and we can also assign lambda functions to variables
lam_test1 = lambda x: x+1
print(lam_test1(23)) #here x = 23 then x+1 so the value getting returned is 24

# Exercise lambda
#create a lambda function that should take 1 integar arguement
#if the integar is less than > 5 return hello
#otherwise return bye

exercise_lamb = lambda x: 'hello' if x>5 else 'bye'

print(exercise_lamb(7))
print(exercise_lamb(3))

#Functions documentation
#it is basically documenting the functions we write

def test_func(arg1): #here i am adding this comment to explain what this function is used for so incase i forget what it is used for i can check it from here
	result = arg1+5
	print(result)

test_func(5)
 
def test_func1(arg1): #here i won't add a comment to explain what this function is used for so incase i forget i can't know again what it was used for 
	result = arg1-5
	print(result)

test_func1(193)

#Documenting functions with comments is very useful if you work in a team or if you forget what the function was used for