#  Cascading assignment
a, b, c = 1,2,3

print(a,b,c)

# Replace values
a = b = c = 1

print(a,b,c)

b = 2
print( a,b,c)

# Replaces values in list

x = y = [7, 8, 9]
x = [13, 8, 9]

print(x)

x = y = [7, 8, 9]
x[0] = 2

print(y)

x = [1, 2, [3, 4, 5], 6, 7]

print (x[2][