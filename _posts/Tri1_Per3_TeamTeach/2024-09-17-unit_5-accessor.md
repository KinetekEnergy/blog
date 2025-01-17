---
title: Unit 5 Accessor Methods
author: me
date: 2024-09-17
categories: ['Team Teaches', 'Unit 5 Team Teach']
render_with_liquid: False
---

<img src="https://github.com/user-attachments/assets/a3b941af-c2cd-403f-8a56-c23908834d99" width="500px" height="auto">


## What is an Accessory Method?

An accessor method, also known as getter methods allows other objects to obtain the value of instance variables or **static** variables.

## Purpose of Accessor Methods
- Allows safe access to instance variables
- Accessor Methods keep data access private and secure
- If you need to access instance variables form a different class, accessor methods are necessary

## Lets Make Our Own Accessor Methods


```java
public class Minion
{
    // Start by defining instance variables that you'll want to access later via the accessor methods
    private double height;
    private String name;
    private String hair;
    private int eyes;

    // Default Constructor
    //String n, int c
    public Minion()
    {
        height = 3.7;
        name = "Bob";
        hair = "None";
        eyes = 2;
    }

    // Overloaded Constructor
    public Minion(double h, String n, String hr, int e)
    {
        height = h;
        name = n;
        hair = hr;
        eyes = e;
    }
    // Accessor Methods!
    public double getHeight()
    {
        return height;
    }
    public String getName()
    {
        return name;
    }
    public String getHair()
    {
        return hair;
    }
    public int getEyes()
    {
        return eyes;
    }
}

// Create minion object Kevin
Minion kevin = new Minion(4.10,"Kevin","Sprout-Cut",2);

// Print Kevin's properties
System.out.println(kevin.getName());
System.out.println(kevin.getHeight());
System.out.println(kevin.getHair());
System.out.println(kevin.getEyes());
```

    Kevin
    4.1
    Sprout-Cut
    2


## Popcorn Hack
Gru is preparing for his big mission to steal the moon, and he needs to assign his minions various tasks based on their skills. Create a new getter method called ``skillLevel`` and print out the Minion's ``skillLevel``Minion class with the attributes ``name, task, and skillLevel.`` Implement some getter accessor methods, and then create a ``Minion`` object to retrieve its values.


```java
public class Minion {
    private String name;
    private String task;
    
    // Create  skillLevel instance variable

    public Minion(String n, String t)
    {
        name = n;
        task = t;
    }
    // Getter Methods
    public String getName()
    {
        return name;
    }
    public String getTask()
    {
        return task;
    }

    // Add getter method here
}
Minion Stuart = new Minion("Stuart", "Developing propulsion system");
System.out.println(Stuart.getName());
System.out.println(Stuart.getTask());
// Add print statement to get skillLevel


```

    Stuart
    Developing propulsion system


## Things to keep in mind when creating your Accessor Methods
- The accessor method must be public so that you can retrieve your instance variables outside of the class
- The return Type must match the type of the instance variable accessed
- The naming convention is often getNameOfVariable
- There should be **no** parameters in your getter methods

![image](https://github.com/user-attachments/assets/17c57fb1-3572-4e6d-b695-914285cc867b)

