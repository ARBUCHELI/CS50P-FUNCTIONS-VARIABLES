#x = 1
#y = 2

#z = x + y

#print(z)

# More interactive version
#x = input("What's x? ")
#y = input("What's y? ")

#z = int(x) + int(y)

#print(z)

# Even more interactive version
#x = int(input("What's x? "))
#y = int(input("What's y? "))

#print(x + y)

# Making a calculator that works with floats
x = float(input("What's x? "))
y = float(input("What's y? "))

#print(x + y)

# Round to the nearest integer
#z = round(x + y)

# Print the formatted result
#print(f"{z:,}")

# Round floating point values, using round
#z = x / y

# Calculate the result and round
z = round(x / y, 2)
print(z)

# Round floating point values, using fstring
# Calculate the result
z1 = x / y

# Print the result
print(f"{z1:.2f}")

# The result will be the same