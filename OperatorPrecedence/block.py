# name = input("Enter your name")
# age = int(input("How old are you {0}".format(name)))
# print(age)
#
#
# if 0 :
#     print("True")
# else :
#     print("False")
#
# name = input("Enter name ")
# if name :
#     print("The name is {0}".format(name))
# else :
#     print("No name entered")

# java - for (int character : name){system.out.println(character)}
# values = [1,2,3,4,5]
# print(sum(int(val) for val in values))

# print table of 1 and 3 ,skipping table of 2
# for i in range (1,4):
#     if i == 2:
#         continue
#     for j in range (1,11):
#         print("{0} times {1} is {2}".format(i,j,i*j))

# number = 5
# result = 10
# print("the entered no is {}".format(number))
# for i in range(number):
#     result += i
# print(result)

##################################################################################
# extend and sorting demo
# no = [5,3,4,7,2,1]
# extra_no = [9,8,7,6]
# print(id(no))
# no.extend(extra_no)
# print(no)
# another_no = no
# print(another_no is no) # comparing two lists ,output = True
# print(another_no == no) # True
# print(another_no)
# sorted_no=no.sort() # sorting the number
# print(sorted_no) # output : None ,because when using sort function we can't assign it to a new variable
#
# no.sort()
# print(no)
# print(another_no)
# print(id(no))
# print(id(extra_no))
# print("")
###################################################################################
# # case insensitive sort
# pangram = "The quick brown dog jumps over the lazy dog"
# letters = sorted(pangram,key=str.casefold)
# print(letters)
#
##################################################################################
#
# city = ["Ranchi",
#         "jamshedpur",
#         "Dhanbad",
#         "Bokaro",
#         "nainital"]
# city[4]="Kolkata"
# city[3:]=["Patna"]
# print(city)
# sorted_city = sorted(city,key=str.casefold)
# print(sorted_city)
#
# # copying a list into a new list
# city_copy = city.copy()
# print(city_copy)
#
# # deleting data in list
# del city[2:]
# print(city)
############################################################
data = [10,50,20,30,60,90,99,40,100]
sorted_data=sorted(data)
print(sorted_data)
max_value = 90
min_value = 30

# proces the low value in the list i.e remove the lower value that the min_value from the list
# stop = 0
# for index,value in enumerate(sorted_data):
#     if(value >= min_value):
#         stop=index
#         break
#
# print(stop)
# del sorted_data[:stop]
# print(sorted_data)

# process the high value in the list i.e remove greater value than the max_value from the list
# start = 0
# for index in range(len(sorted_data)-1,-1,-1):
#     if sorted_data[index]<=max_value:
#         start=index+1
#         break
#
# print(start)
# del sorted_data[start:]
# print(sorted_data)

# process the high value and low value from the list
for index in range(len(sorted_data) - 1, - 1, - 1):
    if sorted_data[index] < min_value or sorted_data[index] > max_value:
        print(sorted_data[index], index+1,sorted_data)
        del sorted_data[index]
print(sorted_data)
print(list(reversed(data)))

def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L










