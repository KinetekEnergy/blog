---
toc: False
comments: False
layout: post
title: Boolean, If Lesson
description: Team LEIA
type: hacks
courses: {'compsci': {'week': 8}}
---

# Boolean

- A Boolean value is either true or false.
- A Boolean expression produces a Boolean value (true or false) when evaluated.

## Conditional ("if") statements

- Affect the sequential flow of control by executing different statements based on the value of a Boolean expression.

IF (condition)
{
	<block of statements>
}

The code in <block of statements> is executed if the Boolean expression condition evaluates to true; no action is taken if condition evaluates to false.

IF (condition)
{
	<block of statements>
}
ELSE
{
	<second block of statements>
}

The code in the first `block of statements` is executed if the Boolean expression condition evaluates to true; otherwise, the code in `second block of statements` is executed.

**Example:** Calculate the sum of 2 numbers. If the sum is greater than 10, display 10; otherwise, display the sum.

num1 = INPUT
num2 = INPUT
sum = num1 + num2
IF (sum > 10)
{
	DISPLAY (10)
}
ELSE
{
	DISPLAY (sum)
}

# Hack 1

- Add a variable that represents an age.

- Add an 'if' and 'print' function that says "You are an adult" if your age is greater than or equal to 18.

- Make a function that prints "You are a minor" with the else function.


```python
age = 1
if age > 18:
    print("You are an adult")
else:
        print("You are a minor")
```

## Relational operators:
- Used to test the relationship between 2 variables, expressions, or values. These relational operators are used for comparisons and they evaluate to a Boolean value (true or false).

**Ex.** a == b evaluates to true if a and b are equal, otherwise evaluates to false

- a == b (equals)	
- a != b (not equal to)
- a > b (greater than)
- a < b (less than)
- a >= b (greater than or equal to)
- a <= b (less than or equal to)

**Example:** The legal age to work in California is 14 years old. How would we write a Boolean expression to check if someone is at least 14 years old?

age >= 14

**Example:** Write a Boolean expression to check if the average of height1, height2, and height3 is at least 65 inches.

(height1 + height2 + height3) / 3 >= 65

# Hack 2

- Make a variable called 'is_raining' and set it to 'True".

- Make an if statement that prints "Bring an umbrella!" if it is true

- Make an else statement that says "The weather is clear".


```python
rain = True
if rain:
    print("Bring an umbrella!")
else:
    print("The weather is clear")
```

## Logical operators:
Used to evaluate multiple conditions to produce a single Boolean value.

- **NOT**	evaluates to true if condition is false, otherwise evaluates to false
- **AND**	evaluates to true if both conditions are true, otherwise evaluates to false
- **OR**	evaluates to true if either condition is true or if both conditions are true, otherwise evaluates to false

**Example:** You win the game if you score at least 10 points and have 5 lives left or if you score at least 50 points and have more than 0 lives left. Write the Boolean expression for this scenario.

(score >= 10 AND lives == 5) OR (score == 50 AND lives > 0)

## Relational and logical operators:

**Example:** These expressions are all different but will produce the same result.

- age >= 16
- age > 16 OR age == 16
- NOT age < 16

# Hack 3

- Make a function to randomize numbers between 0 and 100 to be assigned to variables a and b using random.randint

- Print the values of the variables

- Print the relationship of the variables; a is more than, same as, or less than b


```python
import random
a = random.randint(0, 100)
b = random.randint(0, 100)

print(a)
print(b)

if a > b:
    print("a > b")
elif a == b:
    print("a == b")
else:
    print("a < b")
```

## **Homework**

### Criteria for above 90%:
- Add more questions relating to Boolean rather than only one per topic (ideas: expand on conditional statements, relational/logical operators)
- Add a way to organize the user scores (possibly some kind of leaderboard, keep track of high score vs. current score, etc. Get creative!)
- Remember to test your code to make sure it functions correctly.


```python
import getpass  # get user information
import sys  # system related information (why is this needed)

questions = 7 # num of questions
correct = 0 # num of correct questions

# ask question and check with prompt fiven
def question_with_response(prompt, answer):
    print(prompt)
    msg = input()
    if msg == answer: # checking if user answer same as given answer
        print("That's correct")
        global correct
        correct += 1
    else:
        print("Incorrect")


user_name = input("Enter your name: ") # ask for name
print('Hello, ' + user_name + " running " + sys.executable) # return name
print("You will be asked " + str(questions) + " questions.\n") # display # of questions to be asked

# questions
question_with_response("What statement is used to evaluate booleans?", "if else")
question_with_response("\nWhy are booleans important?", "evaluate values")
question_with_response("\nWhat is conditional for?", "control flow")
question_with_response("\nWhat is a common relational operator?", "!=")
question_with_response("\nWhat is the use of logical operators?", "connect expressions")
question_with_response("\nWhat is this: if a, then b", "conditional statement")
question_with_response("\nWhat is this operator: &&", "and")

print("\n" + user_name + ", you scored " + str((correct / questions) * 100) + "%") # score display

file = open("leaderboard.txt", "a+") # open file
file.write(user_name + ": " + str((correct / questions) * 100) + "%\n") # store user name & score
file.close() # close file safely

# open leaderboard and print it
f = open("leaderboard.txt", "r")
print("\nLEADERBOARD:")
if f.mode == "r":
    contents = f.read()
    print(contents)
```
