---
toc: True
comments: False
layout: post
title: Data Abstraction
tags: ['hacks']
categories: ['CSP', 'Week 7']
---

# Variables 

A Variable is defined as an abstraction inside of a program that can hold a value.

Variables can be named from letters like X, Y, Z to phrases like APIKEY.  The point of these names is to store some sort of Data to a resuable value.

```python
x = 10
name = "Gerald"
fav_food = "Cookies"
```

<hr style="solid">

## Variable Naming

This brings us to the topic of naming Variables. The names of variables are really important when working in groups. For example when one of your teammates review your code they use the names of your variables to quickly understand your code. In the code above you can understand that the variable fav_food represents a favorite food

There are 3 Important Coding Practices to follow when it comes to naming variables

### SnakeCase

SnakeCase is where you replace spaces in variable names with a underscore

```python
    variable_one = "Aashray"
```
Here's an example of a SnakeCase variable that uses a _ as a space. 

Now try making your own SnakeCase variable and set the variable equal to a integer. 

### PascalCase

PascalCase is where you capitialize every word in your variable, but keep it all as one singluar phrase with no spaces

```python
    VariableOne = "Chrissie"
```

Here you can clearly see that the vairable has two diffrent words, and we didn't need to use a space to seperate it. 

Try making your own PascalCase variable

### CamelCase

CamelCase is where you captalize the second word in the variable

```python
    variableOne = "Arushi"
```

Here the One is captalized to indicate a second word in the variable without using a space.

Try making your own CamelCase




```python
# Attempt to add an integer and a string
myInteger = 42
myString = "Hello"

# Try to add them together
result = myInteger + myString

```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    /Users/shubhay/vscode/student/_notebooks/2023-10-03-Data_AbstractionLEsson.ipynb Cell 8 line 6
          <a href='vscode-notebook-cell:/Users/shubhay/vscode/student/_notebooks/2023-10-03-Data_AbstractionLEsson.ipynb#X12sZmlsZQ%3D%3D?line=2'>3</a> my_string = "Hello"
          <a href='vscode-notebook-cell:/Users/shubhay/vscode/student/_notebooks/2023-10-03-Data_AbstractionLEsson.ipynb#X12sZmlsZQ%3D%3D?line=4'>5</a> # Try to add them together
    ----> <a href='vscode-notebook-cell:/Users/shubhay/vscode/student/_notebooks/2023-10-03-Data_AbstractionLEsson.ipynb#X12sZmlsZQ%3D%3D?line=5'>6</a> result = my_integer + my_string


    TypeError: unsupported operand type(s) for +: 'int' and 'str'


<hr style="solid">

## Variable Types

Earlier we explained how to assign variables and properly name them. However in the code above even though I followed all these steps and properly named them I ran into a error.
This is because the types of data, string and int cannot be added. But what are integers and strings?

In python there are multiple types of data that a variable can be, for now lets look at the most commonly use ones.

### Integers

Integers are a numerical value going from 1,2,3,4 or -1,2,-3 etc. These are numbers with no decimals and are ussualy called ints

```python
    int x = 3

    print(x)
```

In this case we call int x to be 3. Normally you don't need to say the data type before the variable in python, however in other languages like JS or C++ you would need to. 

### Strings

Strings are a chain of text, numbers or charcters that are all inside of " "

```python
    str Cookies = " My Fav cookies are Choclate Chip "
```

Here we set a string cookie to be representing the statement that " My Fav Cookies are Choclate Chip"  The " " marks are what determine it is a string in most coding languages.

### Boolean

Booleans are True or False, and they are used for condtional statements
 

```python
    ChrissieGetsSleep = False
    
    if ChrissieGetsSleep = True:
        pass
    else: 
        return 0
```

Here we have a if statement that checks if the boolean variable is currently true and if its true it won't do anything, but if its false it will return 0.

### Float

Floats are a integers that can have decimal values
```python
    x = 3.1415
    print(x)
```

In this case we call int x to be 3.1415, and this is a float because of its decimal points.

### Lists

Lists are ordered collections of items in Python. They can contain a mix of different data types, including integers, floats, strings, and more. 

```python
my_list = [1, 2, 3, 4, 5]
print(my_list)
```

### Dictionaries in Python

Dictionaries are versatile data structures in Python that store key-value pairs. Each value in a dictionary is associated with a unique key, which allows for efficient lookups and retrieval of values.

```python
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "Wonderland"
}
print(my_dict)
```


```python
# Concatation of variables

int1 = 1
int2 = 2
print("Concatation between two non strings in a print statement will EVALUATE them.")
print("Notice how they get ADDED together.")
print(int1 + int2)
print()

print("Concatation between two  strings in a print statement will CONNECT them.")
print("Notice how they get CONNECTED together.")
string1 = "1"
string2 = "2"
print(string1 + string2) # notice how this CONNECTS the variables

# Print statements like these can be used to EVALUATE variables (here we add them)
# To connect them together ("1" + "2" = "12"), use strings
```

    Concatation between two non strings in a print statement will EVALUATE them.
    Notice how they get ADDED together.
    3
    
    Concatation between two  strings in a print statement will CONNECT them.
    Notice how they get CONNECTED together.
    12


<hr style="solid">

## Choosing the Right Data Type in Python

In Python, choosing the appropriate data type for your variables is essential to ensure efficient and correct program execution. Here's when to use some common data types:

### Integers (`int`)

- **Use Cases**: Use integers when you need to represent whole numbers without fractional parts. Integers are suitable for counting, indexing, and performing integer arithmetic.

### Floating-Point Numbers (`float`)

- **Use Cases**: Use floating-point numbers when you need to represent real numbers with decimal points. They are suitable for calculations that involve fractions or decimal values.

### Strings (`str`)

- **Use Cases**: Use strings when you need to work with text data, such as names, sentences, or any sequence of characters. Strings are versatile and can store both plain text and formatted text.

### Lists (`list`)

- **Use Cases**: Use lists when you need an ordered collection of items that can be modified. Lists are ideal for storing multiple values of the same or different data types.

### Tuples (`tuple`)

- **Use Cases**: Use tuples when you need an ordered collection of items that should remain immutable (unchangeable). Tuples are useful for representing fixed sequences of data.

### Dictionaries (`dict`)

- **Use Cases**: Use dictionaries when you need to store key-value pairs, where each key maps to a specific value. Dictionaries are efficient for looking up values based on keys.

### Sets (`set`)

- **Use Cases**: Use sets when you need an unordered collection of unique elements. Sets are useful for tasks like removing duplicates from a list or performing set operations.

### Booleans (`bool`)

- **Use Cases**: Use booleans to represent binary values, such as `True` or `False`. They are essential for making decisions and controlling the flow of your program using conditional statements.

### None (`NoneType`)

- **Use Cases**: Use `None` when you want to represent the absence of a value or indicate that a variable has no assigned value. It's often used as a placeholder or default initial value.

Choosing the right data type helps make your code more readable, efficient, and easier to maintain. Understanding the characteristics and limitations of each data type is essential for effective Python programming.


<hr style="solid">

## Represent a list or string using a variable.


```python
# We are going to cover representing lists or strings with a variable. 
# A list is an ordered sequence of elements. An element is an individual value in a list that is assigned a unique index.

# For example, if I have a grocery list with milk, eggs, and cookies, each item is an element. 
groceryList = ["milk", "eggs", "cookies"] 
#               one ^  two ^    three ^

# The index is a method for referencing the elements in the list. For example, if I reference item 1, it will be milk.

# IMPORTANT: most if not all programming languages index at 0. This means that the 0th element would be milk and the 1st element is eggs. 
# For the AP Exam, indexing will be at 1.


# Next is a string which is an ordered sequence of characters. 
# This may contain letters, numbers, and special characters. Examples include:
string = "Perry"
string2 = "12"
string3 = "!@#"
stringn4 = "Perry12!@#"
```

### Develop data abstraction using lists to store multiple elements.



```python
# Data abstraction allows for the reduction of a particular body of data to a simplified representation of the whole. 
# For example, saying that I have a “grocery list” is a lot easier than saying “I have a list with milk, eggs, and cookies.” 
groceryList = ["milk", "eggs", "cookies"] 
# bundle ^

# In this example, we bundle this data into one term and simplify it. 
# In programming, you can bundle variables together by type and you can name your bundle (name your list). 
# With a list, you don’t need to know how many variables will be needed or how the elements will be stored together. 
# The exam reference sheet will provide notation for lists.
```

### How does data abstraction manage complexity in program code?


```python
# Data abstraction can manage complexity in programs by bundling data together. 
# This can result in a program that is easier to develop and maintain. 
# It also allows multiple related items to be treated as a single value. 

# You also need less variables since one variable holds all the other ones and it allows you to easily modify these variables.
groceryList = ["milk", "eggs", "cookies"] # nice and short

# long and bad
item1 = "milk"
item2 = "eggs"
item3 = "cookies"

# modify variables:
groceryList = ["milk", "eggs", "cookies"] # nice and short

# replace the index 1 with chocolate
groceryList[1] = "chocolate" # notice how index 1 is the 2nd element (AP exam index at 1)

# add a new element
groceryList.append("flour")

# remove element
groceryList.remove("milk")
```

<hr style="solid">

## JSON implementation

JSON stands for JavaScript Object Notation. It is a lightweight format for storing and transporting data. It has several uses. For example, if someone is managing an inventory of cars, they can use JSON to import data and export it.

JSON is used when data is sent from a web server to a webpage.

So the car person can use JSON to display their current inventory of cars to sell on their webpage.

### Converting from PYTHON TO JSON


```python
import json # you will need to import this library

# python dictionary
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON
# we first CALL the library and use the dumps() function
# to call the library and use dumps(), we do json.dumps()

# note: do you know of function machines in math? where you put in the variable, it does some operations, and outputs it?
#       a code function is the same! it takes some data, does some code on it, and outputs it!


# essentially, we say "Hey! JSON library! I would like to use your dumps() function!"
# and then we give the function what we want to dump: "Here is the thing I want to dump into JSON!"
# then the library says back "Here you go! Here's your JSON! I stored it in the y variable!"
y = json.dumps(x) 


print(y) # the result is a JSON string
```

    {"name": "John", "age": 30, "city": "New York"}


### Formatting


```python
# the result above isn't easy to read. let's fix that by formatting!

import json

x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

print("Indent")
y = json.dumps(x, indent=4) # we call the function but say "Please indent it for me!"
print(y + "\n") # the "\n" is a newline seperator and adds a space between each print statement

print("Indent + seperator")
y = json.dumps(x, indent=4, separators=(".", " = ")) # we change the seperator
print(y + "\n")

print("Indent + seperator + sorted")
y = json.dumps(x, indent=4, separators=(".", " = "), sort_keys=True) # now we are sorting them
print(y)

```

    Indent
    {
        "name": "John",
        "age": 30,
        "city": "New York"
    }
    
    Indent + seperator
    {
        "name" = "John".
        "age" = 30.
        "city" = "New York"
    }
    
    Indent + seperator + sorted
    {
        "age" = 30.
        "city" = "New York".
        "name" = "John"
    }


### Converting from PYTHON TO JSON


```python
import json

x =  '{ "name":"John", "age":30, "city":"New York"}' # some JSON

y = json.loads(x) # parse with loads() function

print(y["age"]) # the result is a Python dictionary
```

    30


### Challenge Problem (In Class)
Note that this is just ONE of the problems.

The rest can be found on [Harkirat's GitHub](https://harkirat47.github.io/studentProjectCSP1//2023/10/03/HomeworkProblems_IPYNB_2_.html).


```python
ingredients = ["butter", "white sugar", "light brown sugar", "vanilla extract", "eggs", "flour", "chocolate chips", "baking soda", "salt", "baking powder"]
# Print this list

print(ingredients)

# Create a list called bowl
# Your list must include:
# "flour"
# "baking soda"
# "salt"
# "baking powder"
# When creating this list, make sure to remove these items from the "ingredients" list!
# Print your list

bowl = ["flour", "baking soda", "salt", "baking powder"]
ingredients.remove("flour")
ingredients.remove("baking soda")
ingredients.remove("salt")
ingredients.remove("baking powder")


# Create a list called cream
# Include:
# "butter"
# "white sugar"
# "light brown sugar"
# "vanilla extract"
# "eggs"
# When creating this list, make sure to remove these items from the "ingredients" list!
# Print your list

cream = ["butter", "white sugar", "light brown sugar", "vanilla extract", "eggs"]
ingredients.remove("butter")
ingredients.remove("white sugar")
ingredients.remove("light brown sugar")
ingredients.remove("vanilla extract")
ingredients.remove("eggs")
print(cream)

# Create a list called "dough"
# Combine the bowl list and cream list together
# Print your list

dough = ["butter", "white sugar", "light brown sugar", "vanilla extract", "eggs", "flour", "baking soda", "salt", "baking powder"]
print(dough)

# Append chocolate chips to the dough list and remove it from the ingredients list
# Print the list

dough.append("chocolate chips")
ingredients.remove("chocolate chips")
print(dough)

# Create a string that says "Now roll the dough into balls and place them on cookie sheets!"
# Print it

myString = "Now roll the dough into balls and place them on cookie sheets!"
print(myString)

# Create an int called temperature and set it to 375
# Print "Place in a <<your integer goes here>> F oven for 8-10 minutes and remove just before they start to turn brown."

temperature = 375
print("Place in a " + str(temperature) + " F oven for 8-10 minutes and remove just before they start to turn brown.")

# Create an int called "cool down" using pascal case and set it to 2
# Print "Let them sit on the baking pan for <<your integer goes here>> minutes before removing to cooling rack."

CoolDown = 2
print("Let them sit on the baking pan for " + str(CoolDown) + " minutes before removing to cooling rack.")


# Create 5 string (use whatever casing you feel)
# First string should be "Enjoy"
# Second string should be "your"
# Third string should be "CHOCOLATE"
# Fourth string should be "CHIP"
# Fifth string should be "COOKIES!!!"
# Using ONE print statement, print ALL of these variables (with a space between each)

string1 = "Enjoy"
string2 = "your"
string3 = "CHOCOLATE"
string4 = "CHIP"
string5 = "COOKIES!!!"
print(string1 + " " + string2 + " " + string3 + " " + string4 + " " + string5)
# Yes this is a real cookie recipe. You can find it below if you wanna make them! :)
# https://joyfoodsunshine.com/the-most-amazing-chocolate-chip-cookies/
```

    ['butter', 'white sugar', 'light brown sugar', 'vanilla extract', 'eggs', 'flour', 'chocolate chips', 'baking soda', 'salt', 'baking powder']
    ['butter', 'white sugar', 'light brown sugar', 'vanilla extract', 'eggs']
    ['butter', 'white sugar', 'light brown sugar', 'vanilla extract', 'eggs', 'flour', 'baking soda', 'salt', 'baking powder']
    ['butter', 'white sugar', 'light brown sugar', 'vanilla extract', 'eggs', 'flour', 'baking soda', 'salt', 'baking powder', 'chocolate chips']
    Now roll the dough into balls and place them on cookie sheets!
    Place in a 375 F oven for 8-10 minutes and remove just before they start to turn brown.
    Let them sit on the baking pan for 2 minutes before removing to cooling rack.
    Enjoy your CHOCOLATE CHIP COOKIES!!!

