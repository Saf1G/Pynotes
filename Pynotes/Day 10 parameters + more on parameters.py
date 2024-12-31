#Day 10 parameters time!

def calculator_test(num1,num2): #the arguements inside the bracket are parameters and this is called a positional arguements
	result = num1+num2
	print(result)

calculator_test(13,1248) #here the arguements inside the brackets are called parameters

def test(): #here we are not onbliged to add a value inside the parameter
	if 5 != 3:
		print('test_parameter')

test()

#Keyword arguements
def key_arg(num1,num2): 
	result = num1-num2
	print(result)

key_arg(num1=12,num2=5) #here we can assign the values of num1 and num2 directly so it is more readable also this is called keyword arguements

# Exercise parameters 1
#create a greeter function with person,greet and weekday parameters
#person and greet should have default values person and hello
#use an f string to print greet weekday and person
#use atleast 1 positional arguements while calling the function

def greet_exercise(weekday,person = 'Person',greet = 'Hello'):
	print(f'{greet} {person}, today is {weekday} ')

greet_exercise('thursday')

#More parameters part
def random_generator(finish_range,start_range = 1): #triple random number generator function 
	import random
	print(random.randint(start_range,finish_range))
	print(random.randint(start_range,finish_range))
	print(random.randint(start_range,finish_range))

random_generator(312)

# simple list unpacking

def list_unpack(arguement):
	for all in arguement:
		print(all)

list_unpack([1383123,6,'hello',True])

#Keyword unpacking

def keyword_unpack(**arg2):
	print(arg2)
	
keyword_unpack(arg2 = [123,32,53,'Hello',True]) #here it makes this a dictionary

#Keyword and list unpacking combined

def keyword_list_unpack(*arg,**arg1):
	print(arg)
	print(arg1)

keyword_list_unpack(1,3,3123,3,test = 'hello',test2 = 'nice, test3=321')
keyword_list_unpack(1,312,3)

# Exercise more parameters
#task : create a calculator function that prints the sum of an unlimited amount of numbers

def sum_calculator(*args):
	result = sum(args)
	print(result)

sum_calculator(13,4234,6)







