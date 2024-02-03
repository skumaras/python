bicycles = ['atlas','hero'];
print(bicycles[0].title());
print(bicycles[-1].title());

#motorcycles = ['Honda', 'Yamaha', 'Kwasaki'];
#motorcycles[0] = 'Ducati';
#motorcycles.append('Suzuki');
#print(motorcycles);

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)
motorcycles.insert(1, 'ducati')
print(motorcycles)
del motorcycles[-1]
print(motorcycles)
print("------------------------------------------")
last_owned_motocycle = motorcycles.pop();
print(last_owned_motocycle);
print(motorcycles)
most_expensive = 'ducati';
motorcycles.remove(most_expensive);
print(motorcycles)
print("------------------------------------------")
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)
list_of_cars = ['bmw', 'audi', 'toyota', 'subaru']
print(sorted(list_of_cars));
print(list_of_cars);
list_of_cars.reverse() #reverse the order of the list not alphabetically
print(list_of_cars);

print(len(list_of_cars));
for car in list_of_cars:
	print("Car: "+car)
print("The end of the story")

message = "Hello Python world!"
print(message)
