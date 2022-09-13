farm_animals = {'cow', 'sheep', 'hen', 'goat', 'horse'}
# print(farm_animals)

# set is unordered , no duplicates allowed
# for animals in farm_animals:
#     print(animals)

# set can't be indexed or sliced
# goat = farm_animals[3]
# print(goat)

# creating empty set
numbers = {""}
print(numbers, type(numbers)) # op : {''} <class 'set'>
numbers = {*""}
print(numbers, type(numbers)) # op : set() <class 'set'>
numbers = set()
print(numbers, type(numbers)) # op : set() <class 'set'>
numbers.add(10)
print(numbers)