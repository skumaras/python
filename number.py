for value in range(1,5):
	print(value)
	
numbers = list(range(1,6))
print(numbers)

even_numbers = list(range(2,11,2))
print(even_numbers)

squares = []
for value in range(1,11):
	squares.append(value**2)
	print(squares)	

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum (digits))

squares = [value**2 for value in range(1,11)]
print(squares)

#couting to 20
for number in range(1,21):
	print(number)

#one million
#for number in range(1,1000001):
#	print(number)
	
# summing one million	
print("------------------------------------------")
num = 0
for number in range(1,1000001):
	num = num+number
print(num)	

# odd numbers
for number in range(1,11):
	print(number*3)	

# first 10 cubes
for number in range(1,11):
	print(number**3)	

print("------------------------------------------")
# cubes using list comprehension
cubes = [value**3 for value in range(1,11)]
print(cubes)
