# empty_list=[]
# even = [2,4,6,8,10]
# odd = [1,3,5,7,9]
# numbers = [even,odd]
# print(numbers)

color = [
    ["red","blue"],
    ["black","green","violet"],
    ["orange","red","purple","red"],
]
# # print occurrence of red color in the list
# for color_list in color:
#     if "red" not in color_list:
#         continue
#     else:
#         print("{0}has red color = {1}".format(color_list,color_list.count("red")))

# Remove red color from the list
# for colorList_copy in color:
#     for index in range(len(colorList_copy)-1, -1, -1):
#         if colorList_copy[index] == "red":
#             del colorList_copy[index]
#     print(colorList_copy)

# Remove red color from the list - alternate way
# for clr in color:
#     for clrr in clr:
#         if clrr != "red":
#             print(clrr, end=" ")
#     print() # to print the list on the new line

# Remove red color from the list - join method
for colorList_copy in color:
    for index in range(len(colorList_copy)-1, -1, -1):
        if colorList_copy[index] == "red":
            del colorList_copy[index]

    print(", ".join(colorList_copy))  # now it won't be printed as a list







