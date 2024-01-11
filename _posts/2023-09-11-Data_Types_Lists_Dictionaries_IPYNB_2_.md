---
toc: True
comments: False
layout: post
title: Python Data Types, Lists, and Dictionaries
tags: ['hacks']
categories: ['CSP', 'Week 4']
---

### InfoDB


```python
# Define an empty List called InfoDb
InfoDb = []

# InfoDB is a data structure with expected Keys and Values

# Append to List a Dictionary of key/values related to a person and cars
InfoDb.append({
    "FirstName": "Akhil",
    "LastName": "Singamnenni",
    "DOB": "August 25",
    "Residence": "San Diego",
    "Email": "akhils@gmail.com",
})

# Append to List a 2nd Dictionary of key/values
InfoDb.append({
    "FirstName": "Advik",
    "LastName": "Garg",
    "DOB": "March 11",
    "Residence": "8459 The Landing Way",
    "Email": "advikg.sd@gmail.com",
})

# Append to List a 2nd Dictionary of key/values
InfoDb.append({
    "FirstName": "William",
    "LastName": "Cheng",
    "DOB": "November 27",
    "Residence": "15543 New Park Terrace",
    "Email": "funnykidland@gmail.com",
})

# Print the data structure
print(InfoDb)

```

<hr style="solid">

### For Loop With Index


```python
# code
```

<hr style="solid">

### Pair Share Code


```python
# Define an empty List called database
database = []

profileCount = input("How many profiles to add?") # profiles to add

for i in range(int(profileCount)): # iterate thru num of profiles to add
    # data collection
    firstName = input("First name: ")
    lastName = input("Last name: ")
    dob = input("Date of birth: ")
    residence = input("Residence: ")
    email = input("Email: ")
    
    # appending data
    database.append({
        firstName: firstName,
        lastName: lastName,
        dob: dob,
        residence: residence,
        email: email,
    })

for i in range(int(profileCount)): # iterate thru num of profiles available
    # printing everything
    print("> " + database[i][firstName] + " " + database[i][lastName] + ":")
    print("| DOB: " + database[i][dob])
    print("| Residence: " + database[i][residence])
    print("| Email: " + database[i][email])
    print()
```
