
tuple1 = (1,"Krishna",3.90,"Goyal",True)

print(type(tuple1))

print(type(tuple1[0]))
print(type(tuple1[1]))
print(type(tuple1[2]))
print(type(tuple1[3]))
print(type(tuple1[4]))

# concatenation of tuples

tuple2 = tuple1 + (5,3.89,"Krish")

print(tuple2)

# print(len(tuple1)) # length of tuple

# sorting tuples

tuple3 = (1,2,-3,0,90,1) # unsorted tuple   
sorted_tuple = sorted(tuple3) 
print(sorted_tuple) # sorted tuple

# nestedTuples

tuple4 = (tuple2,tuple1,"Krishna",78,tuple3[3:5])

print(tuple4)

print(tuple4[1][3:5]) # accessing tuple inside tuple


#check if a element is present in a tuple
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

# check if a tuple is a subset of another tuple
thistuple = ("apple", "banana", "cherry")
thistuple2 = ("apple", "banana", "cherry", "orange")
if thistuple2 > thistuple:
    print("Yes, thistuple2 is a subset of thistuple")