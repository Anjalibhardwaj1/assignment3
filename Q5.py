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
        return 2*math.pi*self.radius

    def area(self):
        return math.pi*((self.radius)**2)

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
        return math.pi*self.a*self.b

    def eccentricity(self):
        flag = ((self.a)**2) - ((self.b)**2)
        if flag < 0:
            ret = None
        else:
            ret = math.sqrt(flag)

        return ret

class Rhombus(Shape):

    def __init__(self, p, q) -> None:
        super().__init__()
        self.p = p
        self.q = q

    def perimeter(self):
        return 2*math.sqrt(((self.p)**2) + ((self.q)**2))

    def area(self):
        return (self.p*self.q)/2

    def inradius(self):
        if self.p == 0 and self.q == 0:
            ret = None
        else:
            ret = (self.p*self.q)/(2*math.sqrt(((self.p)**2) + ((self.q)**2)))

        return ret
