#reverse

ratings=[2,3,4,5,7,9,8,9,5,7,8,9,12]
ratings.reverse()
print(ratings)

#classes
import turtle
class Circle(object):
    def __init__(self,radius, color):
        self.radius=radius
        self.color=color
RedCircle= Circle(10,"red")
RedCircle.radius
RedCircle.color

#methods

class Circle(object):
    def __init__(self,radius, color):
        self.radius=radius
        self.color=color
    def add_radius(self,r):
        self.radius=self.radius+r  
    
    
#rectangle
import turtle
class Rectangle(object):
    def __init__(self,height, width, color):
        rec = Rectangle(20,5,'yellow')
        rec.drawRectangle()
    
            
          



