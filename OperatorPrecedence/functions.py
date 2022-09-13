def multiply(a,b):
    result = a*b
    return result

answer = multiply(20,4)
print(answer)
print()

# printing table of 5 using the above function
for val in range(1,11):
    tableResult = multiply(5,val)
    print(tableResult)

    
