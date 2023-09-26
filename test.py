a = 5
b = 6
c = 7
# calculate the semi-perimeter
s = (a + b + c)
# calculate the area
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print(f'The area of the triangle is with sides as ({a}, {b}, {c}) is {area}')