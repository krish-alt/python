# Comparison Operators
# Comparison operations compare some value or operand and based on a condition, produce a Boolean. When comparing two values you can use these operators:

# equal: ==
# not equal: !=
# greater than: >
# less than: <
# greater than or equal to: >=
# less than or equal to: <=

# The inequality operation is also used to compare the letters/words/symbols according to the ASCII value of letters. The decimal value shown in the following table represents the order of the character:

# Char.	ASCII	Char.	ASCII	Char.	ASCII	Char.	ASCII
# A	    65	    N	    78	    a	    97	    n	    110
# B	    66	    O	    79	    b	    98	    o	    111
# C	    67	    P	    80	    c	    99	    p	    112
# D	    68	    Q	    81	    d	    100 	q   	113
# E	    69	    R	    82	    e	    101 	r   	114
# F	    70	    S	    83	    f	    102 	s   	115
# G	    71	    T	    84	    g	    103 	t   	116
# H	    72	    U	    85	    h	    104 	u   	117
# I	    73	    V	    86	    i	    105 	v   	118
# J	    74	    W	    87	    j	    106 	w   	119
# K	    75	    X	    88	    k	    107 	x   	120
# L	    76	    Y	    89	    l	    108 	y   	121
# M	    77	    Z	    90	    m	    109 	z   	122


# Branching


# Branching allows us to run different statements for different inputs. 
# It is helpful to think of an if statement as a locked room, if the statement is True we can enter the room and your program will run some predefined tasks, 
# but if the statement is False the program will ignore the task.
# For example, consider the blue rectangle representing an ACDC concert. 
# If the individual is older than 18, they can enter the ACDC concert. If they are 18 or younger, they cannot enter the concert.
# We can use the condition statements learned before as the conditions that need to be checked in the if statement. 
# The syntax is as simple as  if condition statement :, which contains a word if, any condition statement, and a colon at the end. 
# Start your tasks which need to be executed under this condition in a new line with an indent. 
# The lines of code after the colon and with an indent will only be executed when the if statement is True. 
# The tasks will end when the line of code does not contain the indent.
# In the case below, the code print(“you can enter”) is executed only if the variable age is greater than 18 is a True case because this line of code has the indent.
#  However, the execution of print(“move on”) will not be influenced by the if statement.


# Elif statment example
# elif is an else if statement. It is used to check if the condition is not true.


# The syntax is as follows:
age = 18

if age > 18:
    print("you can enter" )
elif age == 18:
    print("go see Pink Floyd")
else:
    print("go see Meat Loaf" )
    
print("move on")



# Condition statement example 

album_year = 1980

if(album_year > 1979) and (album_year < 1990):
    print ("Album year was in between 1980 and 1989")
    
print("")
print("Do Stuff..")

