---
title: Unit 5 Mutator Methods
author: me
date: 2024-09-17
categories: ['Team Teaches', 'Unit 5 Team Teach']
render_with_liquid: False
---

<img src="https://github.com/user-attachments/assets/c53b4b5d-d58c-4e06-b6d1-09df8b7ee78a" width="500px" height="auto">

## Definition

A mutator method modifies an object's state my changing the value of its fields or attributes.

Example:

Say you have an object called "Minion." If I have a field like "name," a mutator method lets me change its value.

## Okay but why???

Mutator methods are part of Java's philsophy of "encapsulation."

That's nerd-speak for "keeping things seperate". It's the idea of enclosing data and methods as a unit. You want to restrict direct access to data, only accessing them through a PROPERLY defined way.

## Mutator method types:

Accessors: can you guess what this does? That's right, it lets you *access* data. These can be called "get" methods or "getters."


```Java
public class Minion
{
    private String name;

    // notice how the getter method starts with "get" (pretty creative, I know)
    // these methods have to be names like this where you have get<whatever variable>
    public String getName() {
        // because "name" is a string, return type is String
        return name;
    }
}
```

### Your turn!

- Make your own class with your own getter method

Mutators: wait a minute, a "mutator" is a type of mutator method??? Yeah, Java is kinda wacky like that. Try not to think about it much. Anyways... these methods let you *mutate* data (basically change it). They can be called "set" methods or "setters."


```Java
public class Minion
{
    private String name;

    // same naming scheme as a getter but with set instead
    public void setName(String n) {
        name = n;
    }
}
```

### Your turn!

- Make your own class with your own **setter** method

## EXAMPLE TIME WOOOOOOO!!!!!!! 🤓🤓🤓


```Java
public class Minion {
    // the minion's name
    private String name;

    // Constructor to set the name
    public Minion(String n) {
        name = n;
    }

    // getter
    public String getName() {
        return name;
    }

    // setter
    public void setName(String n) {
        name = n;
    }
}

// Create a Minion object and interact with it
Minion myMinion = new Minion("Kevin");

System.out.println(myMinion.getName()); // get the name

myMinion.setName("Bob");
System.out.println(myMinion.getName()); // wow look, the name changed!!

```

    Kevin
    Bob


### Your turn!

Make your own class with:
- A constructor
- A getter
- A setter

Create an object and interact with it! Make sure you use both your setter and getter methods at least once.

## When making mutator methods...
- A setter method has a `void` return type since it doesn't return anything
  - Naming convention: `set<variable name>` like `setName`
- A getter method's return type is of what it is returning
  - Naming convention: `get<variable name>` like `getName`
- Mutator methods in general change variable in a safe way
  - They have to be public if you want to access these variable outside of the class (which is the purpose they serve)
- Parameter type matches the variable you're modifying
  - `public void setName(String n)`
  - You are modifying a `String` called `n`
  - Parameter type matches!
