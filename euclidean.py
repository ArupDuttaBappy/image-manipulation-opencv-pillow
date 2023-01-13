import math

print('Enter first pixel coordinates: ')
Px = int(input('X -> '))
Py = int(input('Y -> '))
print('Enter second pixel coordinates: ')
Qx = int(input('X -> '))
Qy = int(input('Y -> '))

point_dist = math.dist([Px, Py], [Qx, Qy])
print("Euclidean distance between two pixels:", point_dist)
