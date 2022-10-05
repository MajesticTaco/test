import math

print ('Enter the requested inputs to calculate the Area and Perimeter')

x1 = float(input('Enter the value of X1: '))
y1 = float(input('Enter the value of Y1: '))
x2 = float(input('Enter the value of X2: '))
y2 = float(input('Enter the value of Y2: '))
x3 = float(input('Enter the value of X3: '))
y3 = float(input('Enter the value of Y3: '))

ax = (x2-x3)**2 + (y2-y3)**2
bx = (x1-x3)**2 + (y3-y1)**2
cx = (x1-x2)**2 + (y2-y1)**2

if ax <= 0 or  bx <= 0 or cx <= 0:
    print ('Trīsstūri nevar izveidot')
else:
    a = math.sqrt(ax)
    b = math.sqrt(bx)
    c = math.sqrt(cx)    

    Perimiter = (a+b+c)

    s = (a + b + c) / 2  
    Area = (s*(s-a)*(s-b)*(s-c)) ** 0.5

    print('Trīsstūri var izveidot')
    print(a)
    print(b)
    print(c)
    print('The area of the triangle is %0.2f' %Area)
    print('The perimeter of the triangle is %0.2f' %Perimiter)

    
