# Exercise 1: Variable Operations

# Create two variables, num1 and num2, with numerical values. Perform basic arithmetic operations (addition, subtraction, multiplication, division) on them and store the results in separate variables. Print the results.

num1 = 10
num2 = 20

add = (num1 + num2)
print(add)
sub = (num2 - num1)
print(sub)
mul = (num1 * num2)
print(mul)
div = (num1 / num2)
print(div)


# Exercise 2: String Manipulation

# Create a string variable called sentence and initialize it with any sentence of your choice. Use string methods to convert the entire sentence to uppercase. Print the modified sentence.

sentence = "My name is John"
print(sentence.upper())

# Exercise 3: User Input and Conditionals

# Ask the user to enter their age. Check if the entered age is above 18. If yes, print "You are eligible for voting," otherwise print "You are not eligible for voting."

# age = int(input("Enter Your Age: "))
# if(age > 18):
#     print("You are eligible for voting")
# else:
#     print("You are not eligible for voting")

# Exercise 4: For Loop and String Concatenation
    
# Create a string variable called word and initialize it with any word of your choice. Use a for loop to print each letter of the word on a new line. Additionally, concatenate each letter to a new string variable called reversed_word in reverse order.
    
word = "Hello World"
reversed_word = ""

for i in word:
    print(i)
    reversed_word = i + reversed_word

print("Reversed Word:", reversed_word)
