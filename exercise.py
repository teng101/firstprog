# sort the list of integer input
try:
    my_list = []
    while True:
        my_list.append(int(input()))
        my_list.sort()
except:
    print(my_list)



new_list = list(map(int,input().strip().split(",")))
new_list.sort()
print(new_list)


#print the length of the words in the string inputs as a list
my_string = input()
my_string = my_string.split(" ")
string_length = []

for i in my_string:
    string_length.append(len(i))

print(string_length)

string_length.reverse()
print(string_length)


#create a list taking input as strings
new_list = list(map(str,input().strip().split(",")))
print(new_list)


#create a list taking only words as input
word_list = []

while True:
    word = input()
    if word.isalpha():
        word_list.append(word)
    else:
        print("Sorry only words!")


        