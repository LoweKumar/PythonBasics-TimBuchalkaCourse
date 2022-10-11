# def multiple_values(*args, file=None):
#     for word in args[::-1]:
#         print(word, end=' ', file=file)
#
# with open("star_args.txt", 'w') as fileObject:
#    multiple_values("hello", "World", "Python", "java", "Flask", file = fileObject)

# def star_args(*args, file=None):
#     # to print in normal sentence we have to use for loop or else it will print in tuple form
#      for words in args:
#          print(words, end=' ', file=file)
#
# with open("multiplsArgsDemo.txt", 'w')as fileObject:
#     star_args("Hello", 'World', "Welcome", "To", "Python", 3.7, file=fileObject)


# use of 'kwargs' - in the same above program
def star_args(*args, **kwargs):
    # to print in normal sentence we have to use for loop or else it will print in tuple form
    for words in args:
        print(words, end=' ', **kwargs)

with open("multiplsArgsDemoUsingKWargs.txt", 'w')as fileObject:
    star_args("Hello", 'World', "Welcome", "To", "Python", 3.7, file=fileObject)


