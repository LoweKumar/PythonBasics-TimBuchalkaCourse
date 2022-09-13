letters="abcdefghijklmnopqrstuvwxyz"
print("hello" in letters) # False
print("lmnop" in letters) # True

print(letters[1:5])#bcde
print(letters[:-1:5])#afkpu
print(letters[0:-1:5])#afkpu
print(letters[::5])#afkpuz
print(letters[0:-1:5])#afkpu
print(letters[0:13:4])#aeim

# print string in reverse order
print (letters[::-1])
print(letters[25::-1]) # Alternate way of printing in reverse order

print(letters[:-9:-1]) # last 8 characters in reverse order
print(letters[-1:]) # print last character of the string - z
print(letters[:1]) # print first character of the string - a

print(letters[4::-1]) # edcba
print(letters[16:13:-1]) # qpo

print(letters[-4:22:]) # no output
print(letters[-4:23:]) # w

print("Hello"*5)



