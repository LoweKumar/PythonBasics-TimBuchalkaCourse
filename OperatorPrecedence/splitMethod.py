# split method prints the result into list i.e string to list

panagram = """The quick brown
fox jumps over 
the lazy dogs"""
print(panagram.split())

number="2,4,45,67,100,1"
print(number.split(",")) # return list with comma seperated
result = tuple(number.split(","))
print(result) # returns tuple with comma seperated