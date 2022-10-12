# 1. Demo of taking function as an argument inside other function
# def hello():
#     return "Hello World"
#
# # passing hello() function as argument inside the other function
# def other(func):
#     print("Some other code")
#     print(func())
#
#
# other(hello)
# ########################################################################################################################################

# # 2. Demo of returning function from a function
# def hello(name='Jose'):
#     print("the hello() function has beebn run")
#
#     def greet():
#         return "    This is inside the greet()"
#
#     def welcome():
#         return "    This is inside the welcome()"
#
#     if name=='jose':
#         return greet
#     else:
#         return welcome
#
#
# x=hello()
# print(x())

###################################################################################################################################################

# Creating owr own decorator
def hello_decorator(func):

    # inner1 is a Wrapper function in
    # which the argument is called

    # inner function can access the outer local
    # functions like in this case "func"
    def inner1():
        print("Hello, this is before function execution")

        # calling the actual function now
        # inside the wrapper function.
        func()

        print("This is after function execution")

    return inner1


@hello_decorator
# defining a function, to be called inside wrapper
def function_to_be_used():
    print("This is inside the function !!")


# passing 'function_to_be_used' inside thedecorator to control its behaviour
# Next Line will be used if we are not using '@hello_decorator' on line 21.
# function_to_be_used = hello_decorator(function_to_be_used())


# calling the function
function_to_be_used()
