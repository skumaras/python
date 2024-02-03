players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])

print("Here are the first three players on my team:")
for player in players[:3]:
	print(player.title())
	
print("----------------------------------------------------------")	
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)	
my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

foods = ('Biryani','Manchurian','Paratha','Idli','Dosa')

for food in foods:
	print(food)
foods = ('Idli','Dosa')
for food in foods:
	if food == 'Idli':
		print('Idli')
	else:
		print(food) 

name = input("Please enter your name: ")
print("Hello, " + name + "!")

def show(name):
	"""Display a simple greeting."""
	print("Hello "+name)
	
show('senthil')	
