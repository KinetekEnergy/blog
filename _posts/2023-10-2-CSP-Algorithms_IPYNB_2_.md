---
toc: True
comments: True
layout: post
title: CSP Algorithms
tags: ['hacks']
categories: ['CSP', 'Week 7']
---

# Algorithms

BIG IDEA: A FINITE SET OF INSTRUCTIONS THAT ACCOMPLISH A SPECIFIC TASK 

### Sequencing 

DO STEPS OF CODE IN THE ORDER SPECIFIED 

first step -> second step -> third step


```c
number = int(input("Enter a number: "))

result = number * 2
print("double of " + str(number) + " is " + str(result))

```


1. Create a variable based on user input
2. Multiply variable by two
3. Print out both variables at the end

### Selection 

Choose TWO OR MORE OUTCOMES based on a DECISION or CONDITION 


```c
number = 6
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

```

1. Set number to 5
2. If number is divisible by 2 with no remainder, print "Even"
3. Otherwise, print "Odd"

# ITERATION 

REPEAT STEPS BASED ON A DECISION or STOP when a condition is met 

first step -> 
second step -> 
if step 2: true -> first step 
if step 2: false -> third step 
-> fourth step 


```c
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

1. Create a list called fruits
2. For each fruit in the list, print the fruit

### ACTIVITY 1: Robot Pseudocode 

[Link to Robot Question 2](https://assets.learnosity.com/organisations/537/VR165972.g03.png)

Write the pseudocode to move the robot onto the gray square. 

Available Code:
Move forward
Turn Left
Turn Right

PseudoCode here: 
REPEAT 3 TIMES {
    Move forward
}
Turn left
REPEAT 2 TIMES {
    Move forward
}
Turn right
REPEAT 3 TIMES {
    Move forward
}


```c
# Math Operations:

print("Addition") #addition
result = 5 + 3
print(result)  # 8

print("\nSubtraction") #subtraction
result = 10 - 4
print(result)  # 6

print("\nMultiplication") #multiplication
result = 6 * 7
print(result)  # 42

print("\nFloat Division") #float division (float = numbers with decimal values)
result = 20 / 4
print(result)  # 5.0

print("\nInteger Division (floor division)") #floor division
result = 20 // 4
print(result)  # 5

print("\nModulus (remainder)") #remainder
result = 10 % 3
print(result)  # 1
```

### Fibonacci 


```c
def fibonacci(n): #fibonacci sequence 
    fib_series = [0, 1]  

    while len(fib_series) < n:
        next_number = fib_series[-1] + fib_series[-2]  
        fib_series.append(next_number)  

    return fib_series

n = 10  
result = fibonacci(n)
print(result)  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# initial length of list is 2 
# while length of list is less than amount of numbers we want in our final sequence
# add the last two numbers of the list 
# add this value to the end of the list 
# repeat until length of list reaches n

```

### Mini Lesson: If, Else Statements


```c
num =0

if num > 0:
    print(str(num) + " is positive.")
elif num < 0:
    print(str(num) + " is negative.")
else:
    print(str(num) + " is zero.")

```

### Mini Lesson 2: For, While Loops


```c
names = ["Alice", "Bob", "Charlie", "David", "Eve"]
for name in names:
    print(name)


num = 1
while num <= 5:
    print(num)
    num += 1

```

### Mini Lesson 3: Defining Function 


```c

def calculate_square(number):
    square = number * number
    return square #ends function 

result = calculate_square(5)
print(f"The square of 5 is {result}")

```

### Mini Lesson 4: Input


```c
variable1 = input("How old are you?")
print("You are " + variable1 + " years old")
```

### ACTIVITY 2: CALCULATOR 
1. Create calculator function <br>
2. Allow user to Choose 2 numbers and an operator <br>
3. Perform specified operation based on input <br>
4. Return result of calculation <br>



```c
#include <stdio.h>

float calculator(float number1, char operator, float number2);

int main(int argc, char const *argv[])
{
    printf("Type a float, operator, and float\n"); // prompt

    // variable declarations
    float num1, num2;
    char operator;

    scanf("%f", &num1); // take input
    scanf(" %c", &operator);
    scanf("%f", &num2);

    float answer = calculator(num1, operator, num2); // call function

    printf("%f", answer);

    return 0;
}

float calculator(float number1, char operator, float number2)
{
    float answer; // declare this first

    switch (operator) // switch case for the different operators
    {
    case '+':
        answer = number1 + number2;
        break;
    case '-':
        answer = number1 - number2;
        break;
    case '*':
        answer = number1 * number2;
        break;
    case '/':
        answer = number1 / number2;
        break;
    default:
        break;
    }

    return answer; // return the answer
}

```


```c
# String Operations and Concatenation:

print("\nString Concatenation") #add together strings
str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print(result)  # "Hello World"

print("\nString Length") #length of string
text = "This is a sample text."
length = len(text)
print(length)  # 22

print("\nString Indexing and Slicing") #string slicing 
text = "Python"
first_char = text[0]
substring = text[2:5]
print(first_char)  # 'P'
print(substring)  # 'tho'


print("\nString Repetition (Repeating Strings)")
text = "Repeat "
result = text * 3
print(result)  # "Repeat Repeat Repeat "

# Palindrome Check Algorithm:

print("\nPalindrome Check Algorithm")

def is_palindrome(text):
    text = text.replace(" ", "").lower()
    return text == text[::-1] ## == will return boolean 

result1 = is_palindrome("racecar")
result2 = is_palindrome("Hello, World!")

print(result1)  # True
print(result2)  # False
```

### ACTIVITY 3: COUNTING VOWELS
1. Create a function that takes a word as an input <br>
2. Use a for loop to iterate through each character of a word <br>
3. Check how many characters in a word contain vowels <br>
4. Return vowel number <br>


```c
#include <stdio.h>
#include <string.h>

int main(int argc, char const *argv[])
{
    char word[100];     // create array
    scanf("%s", &word); // user input

    int letterCount = strlen(word); // count # of characters
    int vowelCount;                 // declare vowel count

    for (int i = 0; i < letterCount; i++) // loop thru array
    {
        if (word[i] == 'a' || word[i] == 'e' || word[i] == 'i' || word[i] == 'o' || word[i] == 'u') // is the char a vowel?
        {
            vowelCount++; // update the count
        }
    }

    printf("%d", vowelCount); // print it

    return 0;
}
```

# Homework 

CREATE TEXT (string) ANALYZER:

### Criteria: 
1. Accepts input from user
2. Counts total letters, numbers, spaces in a string
3. Counts number of vowels
4. Calculates average word length
5. Correctly displays: total # of characters (including spaces + numbers), total vowels, average word length
6. ensure that program handles upper and lowercase spelling
7. Test multiple inputs to ensure accuracy 

### Extra credit:
1. Add a unique program, function, or feature not specified by criterias



```c
#include <stdio.h>
#include <string.h>
#include <stdbool.h>

int main(int argc, char const *argv[])
{
    char word[20];
    printf("Enter sentence: ");
    fgets(word, sizeof(word), stdin); // read string
    printf("Your phrase: %s", word);

    // COUNT CHARACTERS
    int characterCount = strlen(word);

    // COUNT VOWELS
    int vowelCount = 0;
    for (int i = 0; i < characterCount; i++) // look for vowels; update count
    {
        if (word[i] == 'a' || word[i] == 'e' || word[i] == 'i' || word[i] == 'o' || word[i] == 'u') // is the char a vowel?
        {
            vowelCount++;
        }
    }

    // AVERAGE WORD LENGTH
    int wordCount = 0;
    for (int i = 0; i < characterCount; i++) // look for spaces or newline; update count
    {
        if (word[i] == ' ' || word[i] == '\n')
        {
            wordCount++;
        }
    }
    float wordLength = (float)(characterCount - wordCount) / (wordCount); // subtract spaces & divide by wordcount; cast to float

    // COOKIE DETECTOR
    char key[7] = "cookie";
    bool cookie = strstr(word, key) != NULL; // set to true if the strstr() result != NULL

    // DISPLAY
    printf("Total number of characters: %d\n", characterCount);
    printf("Total number of vowels: %d\n", vowelCount);
    printf("Average word length %.2lf\n", wordLength);
    bool cookie = true ? printf("COOKIE HAS BEEN FOUND!!!") : printf("no cookie detected :("); // print if cookie = true

    return 0;
}
```
