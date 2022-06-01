from Q5 import *

file = open('shapes.txt', 'r')

#initializing a 2D list of shapes
shapes = []

for shape in file:
    shapes.append(shape[:-1].split(' '))

#initializing the list of objects of type Shape
shape_objects = []

#parsing shapes
for i, shape in enumerate(shapes):
    if shape[0] == 'shape':
        shape_objects.append(Shape())
        shape_objects[i].print()

    elif shape[0] == 'circle':
        shape_objects.append(Circle(float(shape[1])))
        #case of invalid circle
        if float(shape[1]) < 0:
            print("Error: Invalid Circle")
        shape_objects[i].print()

    elif shape[0] == 'ellipse':
        shape_objects.append(Ellipse(float(shape[1]), float(shape[2])))
        #case of invalid ellipse
        if float(shape[1]) < 0 or float(shape[2]) < 0:
            print("Error: Invalid Ellipse")
            shape_objects[i].print()
        else:
            shape_objects[i].print()
            print("linear eccentricity: " + str(shape_objects[i].eccentricity()))

    elif shape[0] == 'rhombus':
        shape_objects.append(Rhombus(float(shape[1]), float(shape[2])))
        #case of invalid rhombus
        if float(shape[1]) < 0 or float(shape[2]) < 0:
            print("Error: Invalid Rhombus")
            shape_objects[i].print()
        else:
            shape_objects[i].print()
            print("in-radius: " + str(shape_objects[i].inradius()))

print("\n--------------- Q7 ----------------\n")

#Q7

#initializing statistics dict
Statistics = {
    "Circle(s)" : 0,
    "Ellipse(s)" : 0,
    "Rhombus(es)" : 0,
    "Shape(s)" : 0,
}

for shape in shape_objects:
    Statistics["Shape(s)"] += 1
    if type(shape).__name__ != "Rhombus" and type(shape).__name__ != "Shape":
        Statistics[type(shape).__name__ + "(s)"] += 1
    elif type(shape).__name__ == "Rhombus" and type(shape).__name__ != "Shape":
        Statistics["Rhombus(es)"] += 1

print("Statistics:")
for key, value in Statistics.items():
    print('   ', key, ':', value)


