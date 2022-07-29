f = open("\github\python\kkl.txt","a")
f.write("\nHello World")


with open("\github\python\\njlk.txt","r") as f:
    with open("kkl.txt","w") as fw :

        for line in f:
            fw.write(line)

