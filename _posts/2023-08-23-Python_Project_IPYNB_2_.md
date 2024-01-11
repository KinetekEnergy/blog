---
toc: True
comments: False
layout: post
title: Python Quiz
tags: ['hacks']
categories: ['CSP', 'Week 1']
---

### Python Quiz - Original Code


```python
import getpass, sys

def question_with_response(prompt):
    print("Question: " + prompt)
    msg = input()
    return msg

questions = 3
correct = 0

print('Hello, ' + getpass.getuser() + " running " + sys.executable)
print("You will be asked " + str(questions) + " questions.")
question_and_answer("Are you ready to take a test?")

rsp = question_with_response("What command is used to include other functions that were previously developed?")
if rsp == "import":
    print(rsp + " is correct!")
    correct += 1
else:
    print(rsp + " is incorrect!")

rsp = question_with_response("What command is used to evaluate correct or incorrect response in this example?")
if rsp == "if":
    print(rsp + " is correct!")
    correct += 1
else:
    print(rsp + " is incorrect!")

rsp = question_with_response("Each 'if' command contains an '_________' to determine a true or false condition?")
if rsp == "expression":
    print(rsp + " is correct!")
    correct += 1
else:
    print(rsp + " is incorrect!")

print(getpass.getuser() + " you scored " + str(correct) +"/" + str(questions))
```

<hr style='solid'>
### Python Quiz - Improved Code



```python
import getpass, sys

def question(prompt, answer, score): #question prompt, the answer, and external var w/score
    print("Question: " + prompt) #display prompt
    response = input() #read response

    if response == answer: #response matches answer
        print(response + " is correct!")
        score += 1 #add to your score
    else:
        print(response + " is incorrect!")
    
    return score #return the score; this gets added to the score

# score is set 0
# run the function, passing in the current score. if correct, add to it + return
# the next function recieves the NEW score, which gets added + returned
# this repeats until the end

questions = 3
score = 0

print('Hello, ' + getpass.getuser() + " running " + sys.executable)
print("You will be asked " + str(questions) + " questions.")
print("Are you ready to take a test?")

score = question("What command is used to include other functions that were previously developed?", "import", score)
score = question("What command is used to evaluate correct or incorrect response in this example?", "if", score)
score = question("Each 'if' command contains an '_________' to determine a true or false condition?", "expression", score)


print(getpass.getuser() + ", you scored " + str(score) +"/" + str(questions))
```

This new code eliminates the repeating functions, condensing it into one. To see more info on how everything works, see the comments.

<hr style='solid'>

### Python Quiz - Custom Questions


```python
import getpass, sys

def question(prompt, answer, score): #question prompt, the answer, and external var w/score
    print("Question: " + prompt) #display prompt
    response = input() #read response

    if response == answer: #response matches answer
        print(response + " is correct!")
        score += 1 #add to your score
    else:
        print(response + " is incorrect!")
    
    return score #return the score; this gets added to the score

# score is set 0
# run the function, passing in the current score. if correct, add to it + return
# the next function recieves the NEW score, which gets added + returned
# this repeats until the end

questions = 3
score = 0

print('Hello, ' + getpass.getuser() + " running " + sys.executable)
print("You will be asked " + str(questions) + " questions.")
print("Are you ready to take a test?")

score = question("How can I delete all Windows shares?", "compmgmt.msc", score)
score = question("How can I easily apply Group Policies to a Windows image?", "LGPO", score)
score = question("What file is used to apply policies for secpol?", "inf", score)


print(getpass.getuser() + ", you scored " + str(score) +"/" + str(questions))
```
