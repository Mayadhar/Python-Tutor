# All kind of variables declaration & uses
# Basic variables and its declarations
x = 4
print "Integer : ", x, type(x)

x = -4
print "Integer -VE : ", x, type(x)

x = 444444444444444444444444444444444
print "Long Integer (Long) : ", x, type(x)

x = 4.33
print "Float : ", x, type(x)

# Float can also be scientific numbers with an "e" to indicate the power of 10.
x = -87.7e100
print "Float -VE: ", x, type(x)

x = 4.74658736457
print "Long Float Without Limit: ", x, type(x)

x = 4.74658736457563478953689
print "Long Float With Limit: ", x, type(x)

x = "salary"
print "String : ", x, type(x)

x = True
print "Boolean : ", x, type(x)

# Complex numbers are written with a "j" as the imaginary part:
x = 7j
print "Complex Type : ", x, type(x)

# Python variable parsing

# Convert Integer to Floa
x = 3
y = float(x)
print "Integer To Float : ", x, type(x), "|", y, type(y)

# Convert Float to Integer
x = 3.99
y = int(x)
print "Float To Integer : ", x, type(x), "|", y, type(y)

# You cannot convert complex numbers into another number type.
# Convert Integer to Complex
x = 3
y = complex(x)
print "Integer to Complex: ", x, type(x), "|", y, type(y)

# Convert Float to Complex
x = 3.894
y = complex(x)
print "Float To Complex : ", x, type(x), "|", y, type(y)






