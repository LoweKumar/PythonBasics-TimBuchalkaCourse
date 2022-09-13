for i in range (1,13):
    print("square of {0:<2} is {1:<3} and cube of {0:<2} is {2:<4}".format(i,i**2,i**3))
    print("square of {0:>2} is {1:<3} and cube of {0:>2} is {2:^4}".format(i,i**2,i**3))
print("\n")
for i in range(1,10):
    print("{0} multiplied with {1} is ={2}".format(i,i,i*i) )