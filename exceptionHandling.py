# try...except...else...finally
# try:
#     print(5/8)
# except ZeroDivisionError:
#     print("You can't divide by zero!")
# else:
#     print("5 divided by 0 is: ", 5/0)
# finally:
#     print("Executing finally clause")
# # #############################################################################

# a = 1

# try:
#     b = int(input("Please enter a number to divide a"))
#     a = a/b
#     print("Success a=",a)
# except ZeroDivisionError: # we can name the error or use the name of the error
#     print("You can't divide by zero!")
# finally:
#     print("Executing finally clause")

#################################################################################

# a = 1

# try:
#     b = int(input("Please enter a number to divide a"))
#     a = a/b
#     print("Success a=",a)
# except ZeroDivisionError:
#     print("The number you provided cant divide 1 because it is 0")
# except ValueError:                              #when we put a string instead of a number
#     print("You did not provide a number") 
# except:
#     print("Something went wrong")

##################################################################################

a = 1

try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
except ZeroDivisionError:
    print("The number you provided cant divide 1 because it is 0")
except ValueError:
    print("You did not provide a number")
except:
    print("Something went wrong")
else:                           #else is executed when no error is raised in the try block
    print("success a=",a)
finally:
    print("Processing Complete")
