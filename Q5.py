import math

class Shape:

    #counter variable to set id
    counter = 0

    def __init__(self) -> None:
        #counter is incremented everytime a new Shape object is created
        Shape.counter += 1
        self._id = Shape.counter
   
    @property
    def id(self):
        return self._id

    def print(self):
        print(str(self.id) + ": " + type(self).__name__ + ", perimeter: " + str(self.perimeter()) + ", area: " + str(self.area()))

    def perimeter(self):
        return None

    def area(self):
        return None

class Circle(Shape):
    
    def __init__(self, radius) -> None:
        super().__init__()
        self.radius = radius

    def perimeter(self):
        if self.radius >= 0:
            ret = 2*math.pi*self.radius
        else:
            ret = None
        
        return ret

    def area(self):
        if self.radius >= 0:
            ret = math.pi*((self.radius)**2)
        else:
            ret = None
        
        return ret

class Ellipse(Shape):

    def __init__(self, a, b) -> None:
        super().__init__()
        if a > b:
            self.a = a
            self.b = b
        else:
            self.a = b
            self.b = a

    def area(self):
        if self.a >= 0 and self.b >= 0:
            ret = math.pi*self.a*self.b
        else:
            ret = None
        
        return ret

    def eccentricity(self):
        if self.a >= 0 and self.b >= 0:
            flag = ((self.a)**2) - ((self.b)**2)
            if flag < 0:
                ret = None
            else:
                ret = math.sqrt(flag)
        else:
            ret = None

        return ret

class Rhombus(Shape):

    def __init__(self, p, q) -> None:
        super().__init__()
        self.p = p
        self.q = q

    def perimeter(self):
        if self.p >= 0 and self.q >= 0:
            ret = 2*math.sqrt(((self.p)**2) + ((self.q)**2))
        else:
            ret = None
        
        return ret

    def area(self):
        if self.p >= 0 and self.q >= 0:
            ret = (self.p*self.q)/2
        else:
            ret = None
        
        return ret

    def inradius(self):
        if self.p >= 0 and self.q >= 0:
            ret = (self.p*self.q)/(2*math.sqrt(((self.p)**2) + ((self.q)**2)))
        else:
            ret = None

        return ret

# shape1 = Shape()
# shape2 = Circle(-4)
# shape3 = Rhombus(4, 5)
# shape4 = Shape()
# shape5 = Circle(0)
# shape6 = Ellipse(-8, 7)
# shape7 = Rhombus(3, 1)

# shape1.print()
# shape2.print()
# shape3.print()
# shape4.print()
# shape5.print()
# shape6.print()
# shape7.print()