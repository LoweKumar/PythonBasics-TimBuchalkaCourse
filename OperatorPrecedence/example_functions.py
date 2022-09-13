# def f2(a, L=[]):
#     L.append(a)
#     return L

def f(a, L):
    if L is None:
        L = []
    L.append(a)
    return L


#print(f2())
#print(f2(10))

print(f(10,[]))

#print(input.__doc__) # to get information about the input function
help(input) # alternate way

