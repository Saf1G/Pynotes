#Day 14 File handling!
#Multiply types of files can be opened using python
#Opening the Day 14 File handling text file

#Format = variable = open('File name(if in the same folder) or file path if in another folder')
file = open('Day 14 File handling Text File.txt') #If we print this we get weird stuff like this <_io.TextIOWrapper name='Day 14 File handling Text File.txt' mode='r' encoding='cp1252'>
print(list(file)) #But if we print it as a list/tuple/set or any other datatype it is actually readable and the \n is basically an indicator that the next text is in another line
file.close() #By doing this we see no difference but it closes the file from the memory so ram isn't wasted

#A better way to do the same thing
with open('Day 14 File handling Text File.txt') as file2:
	print(list(file2)) #The benifiet of this is the file is automatically closed after the indentation is over so wrtiting the file.close() is not necessary 

#A readable way
with open('Day 14 File handling Text File.txt') as file:
	print(file.read()) #This is a more readable way because with this we get a proper output 

#How to modifiy/write a file
with open('Day 14 File handling Text File.txt','w') as file: #Here after the first parameter we can add another one they are r,w,a default is r and r = read a = append and w = write
	print(file.write('File handing test \n Day 14 ')) #Here after the file. we can do .append .read or .write append adds text and write removes everything and only adds what we write

 #Exercise (Correct)
#Create a new text file and draw a tree in it
with open('Day 14 File handling exercise drawing a tree.txt','w') as file:
	file.write('   xxx\n   xxxx\n   xxx\n    x\n    x\n    x\n   ___') #Here it is fine if we don't add the print function because we don't want to see the results

#with open('Day 14 File handling exercise drawing a tree.txt') as file: #We can also get the output aka the Tree if we do this 
#	print(file.read())

#Deleting (Rarely used)
#Del is a function which is used to delete variables and values from a container/list/datatype whatever

Del_var = 'a'
del Del_var #Now the Del_var = 'a' is deleted
#print(Del_var) #Here if we try to print it we can see that it doesn't exist

#Removing items from a list
Del_list = ['a',True,1,5,'b'] #here we want to delte the 5 int
del Del_list[3] #Here by giving the index of the thing we want to delete for here that is 5 and the index of 5 is 3 we delete the value 5 from the list
print(Del_list)

Del_list.remove(True) #Here we can also remove values from a list not by index but by their name for example here we remove the value True from the list
print(Del_list)

#We can also use clear and pop **Methods**  to pop and clear a entire list

#Classes intro 7 hours 13 minuites into the video (Very Much Useful)

#OOP (Object Oriented Programming) Super Much Much ** Very Useful - (Code is organised by objects and this is how large programs are made)

#Objects - Object is a container for variables and functions.If we create a video game then a monsters health stamina and energy will be its variables and its attack movements and
           #animations will be its functions. Here the the variables inside are called attributes and the functions inside are called methods and the variables inside are local variables
           #It is possible to have multiple objects and then all can interact with eachother and can get custom attributs(variables) 

#How one object can interact with another - Lets say we have 3 monsters. Monster1- Health 20 Energy 40. Monster2- Health 40 Energy 20. Monster3 Health 60 Energy 10
#		- Here Monster1 attacks Monster2 so Monster2's health is reduced by 20 and Monster1's Energy is reduced by 10. This is an example of one object interacting with another
# 		- Now we have a player object called Player1 and another object called Obstacle1 here the Player1 and Obstacle1 can interact with eachother

#What are classes - Classes are basically a blueprint for an object whenever we create a object we need to create a class for it. A class can also accept arguements to customize an object
#		- for example the Monster1 will be a class without values  and it will have 2 attributes and 3 functions
#		- A class can also inherit from another class. In that case the result will be an object with the attributes and function from both classes. For example
#		- If we have a class for a shark which only has animation and speed then if the shark class inherits from the monster1 class it will get health,energy and its functions
#		- And if we were to change one of the functions from the Monster1 then it will also effect every class inheriting from it for example the shark class here
 



