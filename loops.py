# range function
# range(start, stop, step)
# start is the starting number
# stop is the ending number
# step is the increment
# range(10)
# range(0, 10)
# range(0, 10, 2)

range(10)

# for statement
# for <variable> in <sequence>:
# <variable> is the name of the loop variable
# <sequence> is the sequence of values

years=range(1994,2022)

for year in years:
    print(year)


for i ,year in enumerate(years):
    print(i,year)


i=0
year = years[0]

while(year%2 == 0):
    print(year)
    i+=1
    year = years[i] 