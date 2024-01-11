---
toc: True
comments: False
layout: post
title: Lists & Search
tags: ['hacks']
categories: ['CSP', 'Week 9']
---

## Python lists Operations

### Append function
From the Data Abstractions Unit we Learned about lists and how they can store multiple variables 

Today we're going to show you how to add items to lists utilizing the append option


```python

lst = ["hi"]
lst.append("no")
print(lst)
```

### Insert function
- The insert function allows you to append items to different lists at a specific location.
- Let's first understand how it may work through pseudocode

#### Exmaple 1
INSERT alist, pos, value 
INSERT alist, 1, "hi" 
- Here the alist represents your list you want to append an item to
- The position is where on the list the item will be generated in respect to the current list
- Finally, the value is the item you're adding to your list. 
- So in the code provided below, in position 1 you insert the item "hi" into alist

### Your turn!!!!
- Turn this pseudocode into python
- How may we want to implement this on python? Think back to the data abstraction unit. 
- ( Hint: Think about the differences between psueodcode and python )


```python
# ANSWER: 
# Inserting items to a specific list, remember python is 0 based on the items!!
lst.insert(5, " maybe")
print(lst)
```

### Remove function
- The remove functions allows you to remove specific items at a specific position on the list

#### Pseudocode example
- REMOVE aList, pos


```python
lst.remove(lst[0])
print(lst)
## You can also access the list by the position, this is called list indexing
print(lst[0])
```

### Let's do some Collegeboard exercises
- In the following list:
  - nums = [65, 89, 92, 35, 84, 78, 28, 75]
- Figure out what the minimum number in the list, WITHOUT using the other methods and premade functions.

### Second question:
- Let's say we have a list called "animals" from a survey that stores whether or not they prefer "cats" or "dogs" as strings in this list.
- Transverse this list and tell me the total amount cats and dogs in the list



```python
nums = [65, 89, 92, 35, 84, 78, 28, 75]
print(nums[3])
print("this number is the lowest number in the nums list")
## Your code here
```


```python
animals = ["cats", "dogs"]

animals.remove("dogs")
print(animals)
print("only one person works at this petshop and she likes cats.")
```

### ITS BINARY SEARCH TIME
- By the end of this you should be able to know what binary search is
- What the time complexity of binary search is
- How to derive the time complexity for binary search

### HOW DOES BINARY SEARCH WORK
- pay attention to the demonstration in the front
- volunteers will be called up
- candy if you participate

Binary search is like a guessing game where you halve your options at each step. Imagine you're finding a name in a phone book:

1. **First Step:** You open the book in the middle.
2. **Second Step:** Is the name before or after the middle? You eliminate half of the remaining names.
3. **Repeat:** Keep dividing until you find the name or run out of names to check.
4. **MAKE SURE YOUR LIST IS SORTED** Binary search will not work if the list isn't sorted

Because you're halving the options each time, it's super quick. If you have \(n\) names, it takes at most \( \log_2(n) \) steps to find a name. This efficiency, where the time it takes doesn't increase much as the number of names in the phone book grows, is what makes binary search awesome! Binary search is also more optimal for searcihng compared to a linear search for anything that doesnt include small lists..

### Demo Being shown above
The sorted list we have currently, has integers [1, 3, 4, 5, 13, 20], we are currently trying to find the index of the the integer 1 within the list

How it works is we start at element 0 for our left position and element 5 for our rightwards position

Our middle position becaomes 5 because ((5+0)//2)=3 so element 3

Our element 3 within the list gives us the integer 5

We then realize that oh 5 is greater then 3 so we have to move leftwards

Then to make the algorithm more efficient we move the r backwards 1 beacuse we have already checked at this point

So now we can reduce the list to [1, 3, 4]

Now we can repeat the same steps as before and find the middle of this list which is 3

We realize thats not equivalent to the integer 1, and our value is still too great

So we move the middle leftwards 1 positioon

AND BAM THATS HOW YOU CAN DO BINARY SEARCH


```python
#example of binary search in python has a time complexity of O(n)
def binarySearch(arr, x):
    l= 0 #our minimum element
    r=len(arr) - 1 # our maximum element
    while l <= r:
        mid = l + (r - l) // 2 
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return -1


sorted_list = [2, 5, 8, 12, 16]
target = 3
result = binarySearch(sorted_list, 5)
print(result)

```


```python
#Linear Search Approach in O(n)
def linear_search(target, sorted_list):
    for o in range(len(sorted_list)):
        if sorted_list[o]==target:
            return(o)
#Does not have to be a sorted list for the sake of comparison I just made it sorted
sorted_list = [1, 3, 5, 7, 9, 11, 13, 15]
target = 3
result = linear_search(target, sorted_list)
print(result)

```

Using linear search make a list with elements ["eggs", "milk", "butter", "cake"]
Then randomize an element 1-4 within that list and find the index of it via linear search


```python
import random

array = ["eggs", "milk", "butter", "cake"]

def linear_search(number, array):
    for o in range(len(array)):
        if o==number:
            return array[o]

number = random.randint(0, 3)

print(number)
print(linear_search(number, array))
#code here
```

How big O Notation works in the context works in the case of search methods.

Lets first explain for linear search, because linear search only requires a iterative approach all we use is O(n), this is due
to the loop infinitely going until it finds the element and then after that it doesnt do anything.

However binary search is special in this sense because you don't actually have to go through an entire loop how you can picture this is by imagining a list with 1000000 integer values in it and my target value is 59223, binary search makes it so that you just divide the list by 2 until you find the element. It's a lot faster then the iterative approach, where I keep going until I get to 59223 what this does is it allows me to speed up the time and memory usage I take. because I keep dividing the list by 2 allowing for me to form a logarithm because its just repetitive multiplication of 1/2 and then that makes it so that O(log(n)) becomes the time complexity for the Binary search algorithm.




HW TIME!!!!!!!!!!!!!!!!!!
We want you guys to make a guessing game below, where utilizing binary search you can within a list of 100 sorted elemments find, a value that your code will randomize using random.randint(). We want you to also make it so every iteration output the number is higher up or lower until you actually get to the answer. We also want number of tries it took to guess the number. Points will be awarded for customizations and potential changes.

Extra credit (for above 95%): Send a screenshot on me to slack showing you can do this: https://codeforces.com/contest/1201/problem/C


```python
import random

def binarySearch(array, target):
    # count iterations
    global counter
    counter = 0
    
    l = 0 # our minimum element
    r = len(array) - 1 # our maximum element
    while l <= r:
        mid = l + (r - l) // 2  # find middle of element
        if array[mid] == target: # the middle element is the target
            return mid 
        elif array[mid] < target: # is the middle lest than the target
            l = mid + 1
        else:
            r = mid - 1
        counter += 1
    return -1

array = list(range(0, 100)) # create an array with 100 digits
final = binarySearch(array, random.randint(0, 100))
print(f"Target is {final}. {final} was found in {counter} iterations.")

```


```python
# 95% thing
import statistics

n = int(input("Enter array size"))
array = [None] * n # array with this size

# filling the array
for i in range(n):
    array[i] = input(f"Enter number {i + 1}")
    
print(array)
print(f"The median of the array is {statistics.median(array)}")    
```

HW Part 2: This time instead of utilizing binary search to do it I want you to use linear search to get to the same value and I want you to output the number of iterations it took to get there. Aswell as a congrats message upon getting there points will be awarded upon creativity and completion.


```python
import random

def sing(n):
	if (n == 1):
		objects = 'bottle'
		objectsMinusOne = 'bottles'
	elif (n == 2):
		objects = 'bottles'
		objectsMinusOne = 'bottle'
	else:
		objects = 'bottles'
		objectsMinusOne = 'bottles'


	if (n > 0):
		print(f"{n} {objects} of beer on the wall, {n} {objects} of beer.")
		print(f"Take one down and pass it around, {n - 1} {objectsMinusOne} of beer on the wall.")
		print(" ")
	elif (n == 0):
		print("No more bottles of beer on the wall, no more bottles of beer.")
		print(f"Go to the store and buy some more, {initialBottles} bottles of beer on the wall.")
	else:
		print("Error 101: Wheres the booze?") # search for Wild Turkey 101 Bourbon
  
def linearSearch(array, target):
    # variables
    global bottles, initialBottles
    initialBottles = bottles = target
        
    for i in range(len(array)):
        if bottles >= 0:
            sing(bottles)
            bottles -= 1
        if array[i] == target:
            return(i)

array = list(range(0, 100)) # create an array with 100 digits 
result = linearSearch(array, random.randint(0, 100))
print(f"\nTarget is {result} and was found.")
```

    66 bottles of beer on the wall, 66 bottles of beer.
    Take one down and pass it around, 65 bottles of beer on the wall.
     
    65 bottles of beer on the wall, 65 bottles of beer.
    Take one down and pass it around, 64 bottles of beer on the wall.
     
    64 bottles of beer on the wall, 64 bottles of beer.
    Take one down and pass it around, 63 bottles of beer on the wall.
     
    63 bottles of beer on the wall, 63 bottles of beer.
    Take one down and pass it around, 62 bottles of beer on the wall.
     
    62 bottles of beer on the wall, 62 bottles of beer.
    Take one down and pass it around, 61 bottles of beer on the wall.
     
    61 bottles of beer on the wall, 61 bottles of beer.
    Take one down and pass it around, 60 bottles of beer on the wall.
     
    60 bottles of beer on the wall, 60 bottles of beer.
    Take one down and pass it around, 59 bottles of beer on the wall.
     
    59 bottles of beer on the wall, 59 bottles of beer.
    Take one down and pass it around, 58 bottles of beer on the wall.
     
    58 bottles of beer on the wall, 58 bottles of beer.
    Take one down and pass it around, 57 bottles of beer on the wall.
     
    57 bottles of beer on the wall, 57 bottles of beer.
    Take one down and pass it around, 56 bottles of beer on the wall.
     
    56 bottles of beer on the wall, 56 bottles of beer.
    Take one down and pass it around, 55 bottles of beer on the wall.
     
    55 bottles of beer on the wall, 55 bottles of beer.
    Take one down and pass it around, 54 bottles of beer on the wall.
     
    54 bottles of beer on the wall, 54 bottles of beer.
    Take one down and pass it around, 53 bottles of beer on the wall.
     
    53 bottles of beer on the wall, 53 bottles of beer.
    Take one down and pass it around, 52 bottles of beer on the wall.
     
    52 bottles of beer on the wall, 52 bottles of beer.
    Take one down and pass it around, 51 bottles of beer on the wall.
     
    51 bottles of beer on the wall, 51 bottles of beer.
    Take one down and pass it around, 50 bottles of beer on the wall.
     
    50 bottles of beer on the wall, 50 bottles of beer.
    Take one down and pass it around, 49 bottles of beer on the wall.
     
    49 bottles of beer on the wall, 49 bottles of beer.
    Take one down and pass it around, 48 bottles of beer on the wall.
     
    48 bottles of beer on the wall, 48 bottles of beer.
    Take one down and pass it around, 47 bottles of beer on the wall.
     
    47 bottles of beer on the wall, 47 bottles of beer.
    Take one down and pass it around, 46 bottles of beer on the wall.
     
    46 bottles of beer on the wall, 46 bottles of beer.
    Take one down and pass it around, 45 bottles of beer on the wall.
     
    45 bottles of beer on the wall, 45 bottles of beer.
    Take one down and pass it around, 44 bottles of beer on the wall.
     
    44 bottles of beer on the wall, 44 bottles of beer.
    Take one down and pass it around, 43 bottles of beer on the wall.
     
    43 bottles of beer on the wall, 43 bottles of beer.
    Take one down and pass it around, 42 bottles of beer on the wall.
     
    42 bottles of beer on the wall, 42 bottles of beer.
    Take one down and pass it around, 41 bottles of beer on the wall.
     
    41 bottles of beer on the wall, 41 bottles of beer.
    Take one down and pass it around, 40 bottles of beer on the wall.
     
    40 bottles of beer on the wall, 40 bottles of beer.
    Take one down and pass it around, 39 bottles of beer on the wall.
     
    39 bottles of beer on the wall, 39 bottles of beer.
    Take one down and pass it around, 38 bottles of beer on the wall.
     
    38 bottles of beer on the wall, 38 bottles of beer.
    Take one down and pass it around, 37 bottles of beer on the wall.
     
    37 bottles of beer on the wall, 37 bottles of beer.
    Take one down and pass it around, 36 bottles of beer on the wall.
     
    36 bottles of beer on the wall, 36 bottles of beer.
    Take one down and pass it around, 35 bottles of beer on the wall.
     
    35 bottles of beer on the wall, 35 bottles of beer.
    Take one down and pass it around, 34 bottles of beer on the wall.
     
    34 bottles of beer on the wall, 34 bottles of beer.
    Take one down and pass it around, 33 bottles of beer on the wall.
     
    33 bottles of beer on the wall, 33 bottles of beer.
    Take one down and pass it around, 32 bottles of beer on the wall.
     
    32 bottles of beer on the wall, 32 bottles of beer.
    Take one down and pass it around, 31 bottles of beer on the wall.
     
    31 bottles of beer on the wall, 31 bottles of beer.
    Take one down and pass it around, 30 bottles of beer on the wall.
     
    30 bottles of beer on the wall, 30 bottles of beer.
    Take one down and pass it around, 29 bottles of beer on the wall.
     
    29 bottles of beer on the wall, 29 bottles of beer.
    Take one down and pass it around, 28 bottles of beer on the wall.
     
    28 bottles of beer on the wall, 28 bottles of beer.
    Take one down and pass it around, 27 bottles of beer on the wall.
     
    27 bottles of beer on the wall, 27 bottles of beer.
    Take one down and pass it around, 26 bottles of beer on the wall.
     
    26 bottles of beer on the wall, 26 bottles of beer.
    Take one down and pass it around, 25 bottles of beer on the wall.
     
    25 bottles of beer on the wall, 25 bottles of beer.
    Take one down and pass it around, 24 bottles of beer on the wall.
     
    24 bottles of beer on the wall, 24 bottles of beer.
    Take one down and pass it around, 23 bottles of beer on the wall.
     
    23 bottles of beer on the wall, 23 bottles of beer.
    Take one down and pass it around, 22 bottles of beer on the wall.
     
    22 bottles of beer on the wall, 22 bottles of beer.
    Take one down and pass it around, 21 bottles of beer on the wall.
     
    21 bottles of beer on the wall, 21 bottles of beer.
    Take one down and pass it around, 20 bottles of beer on the wall.
     
    20 bottles of beer on the wall, 20 bottles of beer.
    Take one down and pass it around, 19 bottles of beer on the wall.
     
    19 bottles of beer on the wall, 19 bottles of beer.
    Take one down and pass it around, 18 bottles of beer on the wall.
     
    18 bottles of beer on the wall, 18 bottles of beer.
    Take one down and pass it around, 17 bottles of beer on the wall.
     
    17 bottles of beer on the wall, 17 bottles of beer.
    Take one down and pass it around, 16 bottles of beer on the wall.
     
    16 bottles of beer on the wall, 16 bottles of beer.
    Take one down and pass it around, 15 bottles of beer on the wall.
     
    15 bottles of beer on the wall, 15 bottles of beer.
    Take one down and pass it around, 14 bottles of beer on the wall.
     
    14 bottles of beer on the wall, 14 bottles of beer.
    Take one down and pass it around, 13 bottles of beer on the wall.
     
    13 bottles of beer on the wall, 13 bottles of beer.
    Take one down and pass it around, 12 bottles of beer on the wall.
     
    12 bottles of beer on the wall, 12 bottles of beer.
    Take one down and pass it around, 11 bottles of beer on the wall.
     
    11 bottles of beer on the wall, 11 bottles of beer.
    Take one down and pass it around, 10 bottles of beer on the wall.
     
    10 bottles of beer on the wall, 10 bottles of beer.
    Take one down and pass it around, 9 bottles of beer on the wall.
     
    9 bottles of beer on the wall, 9 bottles of beer.
    Take one down and pass it around, 8 bottles of beer on the wall.
     
    8 bottles of beer on the wall, 8 bottles of beer.
    Take one down and pass it around, 7 bottles of beer on the wall.
     
    7 bottles of beer on the wall, 7 bottles of beer.
    Take one down and pass it around, 6 bottles of beer on the wall.
     
    6 bottles of beer on the wall, 6 bottles of beer.
    Take one down and pass it around, 5 bottles of beer on the wall.
     
    5 bottles of beer on the wall, 5 bottles of beer.
    Take one down and pass it around, 4 bottles of beer on the wall.
     
    4 bottles of beer on the wall, 4 bottles of beer.
    Take one down and pass it around, 3 bottles of beer on the wall.
     
    3 bottles of beer on the wall, 3 bottles of beer.
    Take one down and pass it around, 2 bottles of beer on the wall.
     
    2 bottles of beer on the wall, 2 bottles of beer.
    Take one down and pass it around, 1 bottle of beer on the wall.
     
    1 bottle of beer on the wall, 1 bottle of beer.
    Take one down and pass it around, 0 bottles of beer on the wall.
     
    No more bottles of beer on the wall, no more bottles of beer.
    Go to the store and buy some more, 66 bottles of beer on the wall.
    
    Target is 66 and was found.

