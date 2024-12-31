#Data section very important
#Day 12 better for loops time!

materials = ['Coal','Diamond','Gold','Iron','Netherite']  #Here we want to assign the availability values to the materials for example coal available = 2 etc etc
mats_availability = [2,64,7,24,4]

print(dict(zip(materials,mats_availability))) #here by using the zip function we can combine both of the lists together and make a dictionary/list/tuple with it and here the values are sorted 

#Another way to do this is but it is not the best way
#for mats_avail in zip(materials,mats_availability):
#	print(mats_avail)

#The best way is and it is also very commonly used
for mat,availability in zip(materials,mats_availability):
	print(f'{mat} in stock : {availability}')

#Another way to do this is to use the "enumerate" function it is used to get an index of an item from a list or container 
for index,mat_name in enumerate(materials):
	print(f' {index} : {mat_name}')
	if index == 2:   #here we check if we are halfway there and if we are it will print 'halway there' this is very common for the enumerate function
		print('halfway there!')

# Exercise 1 (better for loops)
#combine zip and enumerate to get 'Mat_name [index :] - mat_availability :'

for index,mat_tuple in enumerate(zip(materials,mats_availability)):
	print(f'{mat_tuple[0]} [Index:{index}] - Availability : {mat_tuple[1]}') #This is very complicated and you may wonder why do we index in the mat_tuple items? (given below)

#Here from mat_tuple we get a tuple which has the values of materials and mats_availability then 
#here  because if we don't put the [0] at first we will get (Coal : 2) instead of just 'Coal' so here we select the Coal from the whole tuple
#then on the availability part we put [1] because if we dont do that we will get (Coal : 2) Tuple and by putting the index 1 here we select the 2 and use it as our availability

#List comprehension (very much useful)

#List comprehension is used to create lists in a single line or to manupulate lists 

Test_list1 = []

for num in range(1,5): #here just to get a list with the numbers starting from 1-4 we waste 3 lines of code 
	Test_list1.append(num)
	
print(Test_list1)

#Simple list comprehension
test_list = [num for num  in range(1,5)]  #Instead we can do something like this it is kinda like ternary operators and this is list comprehension 
            #here this first num is the value that i want to return
print(test_list) #by doing this it is much more efficient but kinda hard to read

#Combining list comprehensions wtih ternary operators
test_list2 = [num if num>3 else 5 for num in range(1,5)] #here the numbers less than 3 are going to replaced with 5 because we put a if statement that if the numbers are below 3 we return 5
print(test_list2)

materials = ['Coal','Diamond','Gold','Iron','Netherite']  #here we want to create a list with all of the parts whhich are less than 25
mats_availability = [2,64,7,24,4]

under25_mats = [(names,avail) for (names,avail) in zip(materials,mats_availability) if avail < 25] #by doing this we only get the values which are less than 25
print(under25_mats)

#Combining list comprehension
combined_list = [[(x,y) for x in range(5)]for y in range(5)] #here the value of x increases for every colum and the value of y increases for every row

for row in combined_list:
	print(row)

# Exercise (very very complicated)
#create the ranks of a chess board

chess_board = [[f'{letter}{rank_num}' for rank_num in range(1,9)]for letter in 'ABCDEFGH'[::-1]]
for row in chess_board:
	print(row)



