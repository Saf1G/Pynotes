#Day 15 Classes practice time (Very important) At 7 hours 30 minuites into the video!
#To create a class first we start with class then the class name and the class name should start with an uppercase letter

class Monster1: #Using the monster example from "Day 14 Classes intro"
	Health = 100 #Here the energy and the health are this classes attributes
	Energy = 40 #And the attributes only exist inside of this class so if we were to print(Energy) we would get an error but if we tried what we did in line 9 then... we would get 40
	#It is a convention to call the reference parameter 'self' and it doesn't mean anything it's just a reference
	#Methods below
	def Attack1(self,damage_amount): #Here a method needs very least one parameter even if it does nothing after the first parameter useful parameters can be added
		print(f'The monster has dealt {damage_amount} damage!') # We need to pass the something as an arguement for every function because it references the class ontop otherwise the function wont work 
	def monster_speed(self,movement_speed): #Exercise
		print(f'The monster has moved at a speed of {movement_speed}!')
	

monster1 = Monster1() #To make this an object we have to call the class like this
print(monster1.Energy) #Casually printing the Energy to see if it works
monster1.Attack1(50) #Here if we pass the arguement 50 it will print that the monster has dealt 50 damage

# Exercise 1 (Passed)
#Task : Create another method for the monster1 called 'speed' and it will show at what speed the monster has moved at
monster1.monster_speed(30)

#__Dunder__Methods (Double underscore methods)

#A dunder method is a normal method but it is not called by an user rather it is called by python 
# For example __len__ is called when an object is passed into len() and and __init__ created when an object is called etc etc.

class Monster2:
	def __init__(self,Health,Energy): #This automatically runs when the an object is created with the Monster2 class like monster2 = Monster2() below  
		self.Health = Health #Here no attribute is needed for the health and energy because we already add those as parameters in __init__
		self.Energy = Energy
	def __len__(self): #This is another dunder function this basically returns the value of something that we want or ask for
		return self.Health
	def __abs__(self):
		return self.Energy  #This basically turns int that starts with a - to + kinda useful
	def __str__(self):
		return f'The monster right now has {self.Energy} energy and {self.Health} health!'
monster2 = Monster2(80,30) #Makes an object with the class Monster2 called 'monster2' and the parameters inside Monster2 are it's health(50) and energy(30) 
print(len(monster2))
print(abs(monster2))
print(monster2.__dict__) #This is used to get all the attributes of an object in a dict format and it can also be done with 'vars(monster2)'

# Exercise (Passed)
#Figuire out what the __str__ does
print(monster2) #It is used if we wan't to check anything or wan't to print anything and The __str__ dunder method returns any string that we type 


