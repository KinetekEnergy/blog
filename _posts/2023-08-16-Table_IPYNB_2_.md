---
toc: True
comments: False
layout: post
title: Table Code Hack
tags: ['hacks']
categories: ['CSP', 'Week 2']
---

### IF Code Block


```python
a ← 1
b ← 1

IF (a = b) {
   DISPLAY("A equals B")
}
```


```python
// declare vars for usage
var a = 1;
var b = 1;
if (a == b) {
    element.text("A equals B"); // display as per the if()
}    

```


```python
A equals B
```

<hr style="solid">

### REPEAT n TIMES Code Block


```python
a ← 0 

REPEAT 100 TIMES
{
    a ← a + 1
}

DISPLAY(a)
```


```python
a = 0 # gotta declare + initialize the var

for x in range(100): # repeat 100 times
    a += 1 # a++

print(a) # print 
```


```python
var a = 0; // var a which is 0
for (let i = 0; i < 100; i++) { // for loop to increment a 100 times
    a++;
}    
element.text(a); // display it
```


```python
100
```

<hr style="solid">

### Why pseudo code helps

Psuedo code helps because it creates a template/draft to go off of. Furthermore, since psuedo code is not a real language, you can use it to draft projects for any language. So the same pseudo code can be transferred to C, Python, etc. which makes it very useful for creating drafts that anyone can use.

It helped me solve this problem, because like mentioned above, I only have to write one draft in psuedo code then translate it to Python or JS.


### Vocab to know:

- Code block
  - A block or section of a whole piece of code
- Sequence
  - A sequence of instructions or commands to run in a step by step, logical order
- Selection
  - Run commands in the code block associated with the selection
- Iteration
  - Repeat commands in the code block and iterates it based on a certain condition
