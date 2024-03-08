---
layout: post
title: Developing Procedures
toc: True
comments: True
tags: ['hacks']
categories: ['CSP', 'Week 10']
---

## What is a procedure?
A procedure is a named group of programming instructions with a purpose and is called to perform a task based on the commands. 


It is extremely important to name the procedure something that describes the purpose, method, or function because it makes it easier for others to read your code and for yourself when you revisit old code. Additionally, when there is an effefctively named procedure, it is much simpler to correct bugs and errors.

### Which code is better?
<img src="https://media.discordapp.net//attachments/909575347773775953/1166199627083698217/namingprocedures.png?ex=65499f0a&is=65372a0a&hm=6a7d0bf546b51e54837e3cd8d5993063d9ab28ac4f19bd6e49b6a540424a30a5&" alt="code example">

### Hack 1: Naming Procedures
Rename the procedure below with a name that better describes the purpose of the procedure. 

The procedure is currently just called "procedure." It compares the current grade with the existing quiz grade and replaces the original score if the current is higher.


```python
def gradeCalculate(quiz_grade, current_points, total_points):
    # calculate current grade
    current_grade = (current_points / total_points) * 100

    if current_grade > quiz_grade:
        quiz_grade = current_grade

    return quiz_grade

quiz_grade = 85  # Initial quiz grade
current_points = 90  # Current points earned
total_points = 100  # Total points for the quiz

new_quiz_grade = gradeCalculate(quiz_grade, current_points, total_points)

print(f"Old quiz grade: {quiz_grade}")
print(f"New quiz grade: {new_quiz_grade}")

```

    Old quiz grade: 85
    New quiz grade: 90.0


## Function Parameters
A function can have one or more parameters that can be passed into the function as local variables to use in the procedural function. The variables that can be passed in the function are called parameters. The data passed in when the function is called are called arguments.


Parameters: input values of a procedure


Arguments: specify the parameter values when a procedure is called


```python
def triangle_area(length, width): # parameters passed in two variables: length and width, returns area
    area = 1/2 * length * width # calculates area from the length and width
    print("length:", length)
    print("width:", width)
    return area # returns area

# examples
print(triangle_area(3, 4)) # the arguments here are 3 and 4, which becomes the parameters length and width respectively
print(triangle_area(6, 8))
print(triangle_area(12, 89))
```

    length: 3
    width: 4
    6.0
    length: 6
    width: 8
    24.0
    length: 12
    width: 89
    534.0


## Procedure Algorithm / How Procedures Work
Remember that procedures are essentially a set of programming instructions, or lines of code, that accomplish a goal. When executed, each line of code is executed in order (step after step after step) to get to the goal.

### Regular code/Python


```python
# Procedure called "applyTax" that applies a percent tax to a price
def applyTax(price, percentTax): # When writing a procedure, first decide what parameters you will need to accomplish your goal
    # Step 1: Calculate the amount taxed
    taxAmount = price * percentTax/100

    # Step 2: Add the amount taxed to the price to get the end amount
    endAmount = price + taxAmount

    return endAmount

# Use procedure to apply a 50% tax to a price of $10
cost = applyTax(10, 50)
print(cost)
```

    15.0


### CollegeBoard Pseudo-Code
- Note that the pseudo-code below has the exact same purpose as the actual code above. Ignore the breaks and spaces since they are used for formatting.
> Differences between prseudo-code and Python:
- Pseudo-code uses "PROCEDURE" instead of "def"
- Pseudo-code uses "<--" instead of "="
- Pseudo-code uses "{}" instead of ":" to mark where a procedure starts and ends
<br>

> Pseudo-code example <br>

PROCEDURE applyTax (price, percentTax) <br>
{ <br>
&nbsp;&nbsp;&nbsp;&nbsp;taxAmount <-- price * percentTax/100 <br>
&nbsp;&nbsp;&nbsp;&nbsp;endAmount <-- price + taxAmount <br>
&nbsp;&nbsp;&nbsp;&nbsp;return endAmount <br>
}

### Hack 2: Robot Pseudo-Code
<img src="https://media.discordapp.net/attachments/1143438030749847604/1165903186473783317/image.png?ex=65488af5&is=653615f5&hm=349a4cfef60546b6f85e59a2448ac85ed4fd0181d63f70456904909e46401d74&=" alt="code empty example">

> Instructions:
- The blue triangle represents a robot that moves in a grid of squares. The tip of the triangle indicates where the robot is facing.
- Write a procedure that allows the robot to make a detour around a block by moving to the left.

> Commands
- MOVE_FORWARD() - Moves the robot forward one square
- MOVE_BACKWARD() - Moves the robot backward one square
- ROTATE_LEFT() - Rotates the robot 90 degrees left
- ROTATE_RIGHT() - Rotates the robot 90 degrees right

> Your code here:
ROTATE_LEFT()
MOVE_FORWARD()
ROTATE_RIGHT()
MOVE_FORWARD()
MOVE_FORWARD()
ROTATE_RIGHT()
MOVE_FORWARD()

## Procedure Return Values
When a procedure is run, it executes a series of calculations or commands and at some point and needs to provide a useful result. The return statement is what allows us to return a useful value back to the calling code. The returns statement can return various types of values such as booleans, integers, strings, etc.

## Procedure Calls
Calling: This involves specifying the function name followed by parentheses, and passing any required arguments inside the parentheses.


When a function is called, the program control jumps to the function definition, and the statements inside the function are executed.
After the function completes its task, the control returns to the point where the function was called.

### Hack 3: Create and Call a Procedure
Define a function named calculate_grade that takes a student's score as a parameter and returns 'Pass' if the score is 50 or more, and 'Fail' otherwise.


```python
def calculate_grade(score):
    if score >= 50:
        print("Passed")
    else:
        print("Failed")

score = 50
calculate_grade(score)
```

    Passed


# Homework
## Instructions
There are two total problems:
1.  An easy regular code (Python) problem
2.  A medium pseudo-code problem
3. A hard regular code (Python) problem


Completing question 1 and 2 gets you 0.9/1 if you do it correctly. Completing/attempting question 3, adding creativity, and adding good comments will potentially raise you above 0.9.

### Question 1
Write a procedure to apply a percent discount to a set price. See the example about applying tax if you're stuck.


```python
def discount(price, discountPercentage):
    # convert discount to decimal (80 -> .80)
    # multiply price by it
    # remove that from the price
    price = price - (price * (discountPercentage / 100))
    return price

discount_ = 80 # 80% off
price = 100 # 100 $100

print(f"${price} with an {discount_}% is ${discount(price, discount_)}")

```

    $100 with an 80% is $20.0


### Question 2
Create your own robot problem! Include a picture with a square grid to represent the map and triangle to represent the robot. Add a flag to a square to represent the end-point and a shaded-in block to represent a detour. Write a procedure in pseudo-code to move the robot from the start, past the detour, and to the end point.

Add your image here by adding the link between the "" and removing the comment formatting:
<!-- <img src=""> -->

### Hack 2: Robot Pseudo-Code
<!-- <img src="images/maze.jpg" alt="maze"> -->

> Instructions:
- Move the triangle to the end while getting the coin

> Commands
- MOVE_FORWARD() - Moves the robot forward one square
- MOVE_BACKWARD() - Moves the robot backward one square
- ROTATE_LEFT() - Rotates the robot 90 degrees left
- ROTATE_RIGHT() - Rotates the robot 90 degrees right


CODE:
MOVE_FORWARD()
MOVE_FORWARD()
ROTATE_RIGHT()

MOVE_FORWARD()
MOVE_FORWARD()
ROTATE_RIGHT()

MOVE_FORWARD()
MOVE_FORWARD()
MOVE_FORWARD()
MOVE_FORWARD()
ROTATE_RIGHT()

MOVE_FORWARD()
MOVE_FORWARD()

ROTATE_RIGHT()
ROTATE_RIGHT()

MOVE_FORWARD()
MOVE_FORWARD()
ROTATE_LEFT()

MOVE_FORWARD()
MOVE_FORWARD()
MOVE_FORWARD()
MOVE_FORWARD()
ROTATE_RIGHT()

MOVE_FORWARD()
MOVE_FORWARD()
ROTATE_RIGHT()

MOVE_FORWARD()
MOVE_FORWARD()
MOVE_FORWARD()
MOVE_FORWARD()

### Question 3
Create a program that asks for user input of an integer *n*, and return an array that contains all the prime numbers up to the number *n* (inclusive). Remember to use multiple different functions to better organize the code and increase efficiency.


```python
def prime(num): # prime checker
  if num < 2: # is number less than 2
    return False
  for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
      return False
  return True

def getPrime(n): # creating the array
  primes = []
  for num in range(2, n + 1):
    if prime(num):
      primes.append(num) # append the prime number to the array
  return primes

n = int(input("Enter an integer n: ")) # primpt for input
if n < 2:
  print("Please enter a number greater than or equal to 2.") # make sure the n is valid
else:
  result = getPrime(n) # check the result
  print(f"Prime numbers up to {n}: {result}") # print the array


```

    Prime numbers up to 37: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

