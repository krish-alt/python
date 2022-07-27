import matplotlib.pyplot as plt

%matplotlib inline



class circle(object):

    def __init__(self, radius,color):
        self.radius = radius
        self.color = color

    def area(self):
        self.area = 3.14 * self.radius ** 2
        return self.area
    
    def add_radius(self, radius):
        self.radius += radius
        return self.radius
    
    def draw(self):
        plt.gca().add_patch(plt.Circle((0,0), self.radius, color=self.color))
        plt.axis('scaled')
        plt.show()
        




C = circle(10, "red")
print(C.area())

print(C.add_radius(20))
try: print(C.area())
except: print("error")

C.draw()
