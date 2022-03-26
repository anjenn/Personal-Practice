from math import *
# importing library

print("Hello world")

# working with strings

# no semicolon needed
# \" when we want to print a quotation mark
# \n new line

phrase = "some text"
print("this is\n sthsth" + phrase)
print(phrase.upper().isupper())
print(phrase.upper())
print(len(phrase))
print(phrase[3])
print(phrase.index("e"))

# working with numbers
print(10%3)  # and then we get the remainder
my_num = 5
print(str(my_num)+" is my favorite number") # in order to concatenate with string,
# we must fist convert the number into string

print(floor(3.7)) # we took it from math library, rounds number down
print(ceil(3.7)) # rounds the number up
print(sqrt(36))


# getting input from users

#name = input("Enter your name: ")
#age = input("Enter your age: ")
#print("Hello " + name + "! And you are " + str(age) + " years old!")

#num1 = input("Enter a number: ")
#num2 = input("Enter another number: ")
#result = int(num1)+int(num2)
#print(result)

# lists
lucky_numbers = [3, 5, 2, 4, 4, 5]
friends = ["Kevin", "Karen", "Jim", "Jim"]
#           0        1        2
print(friends)
print(friends[1:])
lucky_numbers.sort()
lucky_numbers.reverse()
friends.extend(lucky_numbers)
friends.append("Creed")
friends.insert(1, "Kelly")
friends.remove("Jim")
print(friends)
friends.pop()
print(friends)
print(friends.index("Kevin"))
print(friends.count("Jim"))

friends2 = friends.copy()
