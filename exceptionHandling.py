# try...except...else...finally
try:
    print(5/8)
except ZeroDivisionError:
    print("You can't divide by zero!")
else:
    print("5 divided by 0 is: ", 5/0)
finally:
    print("Executing finally clause")
# #############################################################################
