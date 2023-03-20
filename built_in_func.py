#built-in functions
#A

#abs(x) Return the absolute value of a number.
x= -20.83
print(abs(x))


#all() returns True if all the elements in the iterable evaluate to True

nums = [2, 4, 6, 8]
print (all(num % 2 == 0 for num in nums))

animals = {'cat', 'dog', 'bird', "elephant"}
print(all(len(animal) <= 3 for animal in animals))


#any() Return True if any element of the iterable is true.
nums = [2, 4, 5, 8]
any(num % 2 != 0 for num in nums)

animals = {'cat', 'dog', 'bird'}
any(len(animal) > 5 for animal in animals)

#returns a string containing only ASCII characters, & replaces non-ASCII with their escape sequences.
str1 = "Hello, world!"
str2 = "Héllo, wôrld!"

print(ascii(str1))
print(ascii( str2))

# bin() convert an integer number to its binary representation.
num = 10
binary_num = bin(num)

print(binary_num)


#bool() Return a Boolean value, i.e. one of True or False
bool_value1 = bool(10)
bool_value2 = bool(0)

print(bool_value1) # True
print(bool_value2) # False

#breakpoint() pause the execution of your code and open up a debugger
#type c in the console to continue
def divide(a, b):
    result = a / b
    breakpoint() #can take arguments to customize the behavior-specifying condition when debugger pause the program/message display
    return result

divide(10, 2)


#bytearray() returns a new array of bytes with the given length
# create a bytearray object with length 5
ba = bytearray(5)

# print the initial values of the bytearray
print(ba)  # output: bytearray(b'\x00\x00\x00\x00\x00')

# modify some bytes in the bytearray
ba[1] = 255
ba[3] = 128

# print the modified bytearray
print(ba)  # output: bytearray(b'\x00\xff\x00\x80\x00')


# create a bytearray from a list of integers
ba = bytearray([65, 66, 67])

# print the bytearray as a string
print(ba.decode('utf-8'))  # output: ABC


#bytes() returns a new immutable (sequence of integers in range 0 <= x < 256) bytes object
# create a bytes object from a list of integers
b = bytes([65, 66, 67])

# print the bytes object as a string
print(b.decode('utf-8'))  # output: ABC

# create a bytes object from a string
b = bytes('hello', 'utf-8')

# print the bytes object as a string
print(b.decode('utf-8'))  # output: hello



