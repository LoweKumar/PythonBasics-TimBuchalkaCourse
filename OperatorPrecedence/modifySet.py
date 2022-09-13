data = ["blue", "red", "black", "red", "white", "blue", "green"]
unique_data = set(data)
print(unique_data)  # prints the unique data in form of set
data_unique = sorted(set(data))
print(data_unique)  # prints the unique data in form of list

# Create a list of unique colors, keeping the order they appeared
result = list(dict.fromkeys(data))
print(result)

