import math
pi = 3.14
a = int(input())
a1 = int(input())
b = int(input())
b1 = int(input())
A = (float(a/180)) * pi
A1 = (float(a1/180)) * pi
B = (float(b/180)) * pi
B1 = (float(b1/180)) * pi
Distance = 6371.1 * math.acos(math.sin(A)*math.sin(B)+math.cos(A)*math.cos(B)*math.cos(A1-B1))
print(Distance,"km")
