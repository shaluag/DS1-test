
"""

# Write your code here

"""### Q2:- Write a program that will convert celsius value to fahrenheit."""

# Write your code here
celsius = float(input("Enter temperature in celsius: "))
fahrenheit = (celsius * 9/5) +32
print("Temperature in fahrenheit is: ", fahrenheit)


"""### Q3:- Take 2 numbers as input from the user.Write a program to swap the numbers without using any special python syntax."""

# Write your code here
a = int(input("Enter value of a : "))
b = int(input("Enter value of b: "))
c = a
a = b
b = c
print(a, b)


"""### Q4:- Write a program to find the euclidean distance between two coordinates.Take both the coordinates from the user as input."""

# Write your code here
x1=float(input("Enter the x1:"))
y1=float(input("Enter the y1:"))

x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))
distance = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
print("Distance :", distance)



"""### Q5:- Write a program to find the simple interest when the value of principle,rate of interest and time period is provided by the user.

"""
p = int(input("Enter the principle amount : "))
r = int(input("Enter the ROI : "))
t = int(input("Enter the time : "))
simp = (p*r*t)/100
print(simp)

"""### Q6:- Write a program that will tell the number of dogs and chicken are there when the user will provide the value of total heads and legs.

For example:
Input:
heads -> 4
legs -> 12
<br>
Output:
dogs -> 2
chicken -> 2
"""

# Write your code here
heads = int(input("Enter the no. of heads : "))
legs = int(input("Enter the no. of legs : "))
dogs = legs/2 - heads
cats = heads - dogs
print("Dogs : ", dogs)
print("Chicken : ", cats)

"""### Q7:- Write a program to find the sum of squares of first n natural numbers where n will be provided by the user."""

# Write your code here
#for loop
n = int(input("enter the number: "))
sum = 0
for i in range(1, n+1):
    sum = sum + (i*i)
print(sum)

#while loop
n=5
sum=0
while n>0:
    sum += n*n
    n -= 1
print(sum)
"""### Q8:- Given the first 2 terms of an Arithmetic Series.Find the Nth term of the series. Assume all inputs are provided by the user."""

# Write your code here
a = int(input("Enter the first no : "))
b = int(input("Enter the second no: "))
n = int(input("Enter the nth term: "))
diff = b -a 
nth_term = a +(n-1)*diff
print(nth_term)


"""### Q9:- Given 2 fractions, find the sum of those 2 fractions.Take the numerator and denominator values of the fractions from the user."""

# Write your code here
a1 = int(input("Enter the num1: "))
b1 = int(input("Enter the den1: "))
a2 = int(input("Enter the num2: "))
b2 = int(input("Enter the den2: "))
c = a1/b1
c1 = a1/b1
result = c + c1
print(result)

"""### Q10:- Given the height, width and breadth of a milk tank, you have to find out how many glasses of milk can be obtained? Assume all the inputs are provided by the user.



Input:<br>
Dimensions of the milk tank<br>
H = 20cm, L = 20cm, B = 20cm
<br><br>
Dimensions of the glass<br>
h = 3cm, r = 1cm
"""

# Write your code here
height = float(input("Enter height: "))
length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))
tank_ct = height * length * breadth
capacity = tank_ct * 1000
glass_ct = float(input("Entet float no. "))
glass = capacity / glass_ct
print(glass)
