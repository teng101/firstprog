#output the longest words in the list
x = ["apple", "grapes", "bananas", "kiwi", "kananas"]
n =0

for i in x:
    if len(i)>n:
        y = i
        n = len(i)
    elif len(i) == n:
        y += " " + i
print(y)


#write the items on the list in uppercase
z= []
for i in x: 
    z.append(i.upper())

print(z)


#Capitalized the first letter of each word in the string
string = "there are a lot of people in this world"

string = string.split(" ")

text = ''
for i in string:
    #n = 0
    for j in range(len(i)):
        if j == 0:
            text += i[j].upper()
        else:
            text += i[j]
    '''for j in i:
        if n == 0:
            text += j.upper()
            n = 1
        else:
            text += j '''
    text += " "
print(text)  

        

