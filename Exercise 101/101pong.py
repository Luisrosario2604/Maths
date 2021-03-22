#!/usr/bin/python
# -*- coding utf-8 -8-

from math import * 
import sys

x0 = float (sys.argv[1])
y0 = float (sys.argv[2])
z0 = float (sys.argv[3])
x1 = float (sys.argv[4])
y1 = float (sys.argv[5])
z1 = float (sys.argv[6])
n = int (sys.argv[7])

xSpeed = x1 - x0
ySpeed = y1 - y0
zSpeed = z1 - z0

nX = n * xSpeed + x1
nY = n * ySpeed + y1
nZ = n * zSpeed + z1

angle = degrees(atan(abs(z1 - nZ) / sqrt ((abs(x1 - nX)**2 + abs(y1 - nY)**2))))

print("The speed vector coordinates are :")
print("(%.2f;%.2f;%.2f)") % (xSpeed, ySpeed, zSpeed)
print("At time t+%d, ball coordinate will be :" % n)
print("(%.2f;%.2f;%.2f;)") % (nX, nY, nZ)
print("The incidence angle is :")
print("%.2f" % angle)
