---
title: Unit 5 toString Method
author: me
date: 2024-09-17
categories: ['Team Teaches', 'Unit 5 Team Teach']
render_with_liquid: False
---

<img src="https://github.com/user-attachments/assets/c53b4b5d-d58c-4e06-b6d1-09df8b7ee78a" width="500px" height="auto">

## toString Accessor Method
The toString accessor method is an overridden method that is included in classes to provide a description of a specific object. It returns a sting description of the instance variables of the object. The method is called automatically to try to convert an object to a String when needed.

If System.out.print or System.out.println is passed an object, that object's toString method is called and the returned string is printed.

## If you try to just print the object...
It won't print the information that you want.


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

// Print Kevin Object
System.out.println(kevin);
```

    REPL.$JShell$12$Minion@f979182


## The toString Method
When the System.out.println() is used, the toString method ``within the class`` is automatically called to print the object's values.
![image](https://github.com/user-attachments/assets/ba8657e5-a3ba-4445-b26a-ad6712cf223b)

## Popcorn Hack

Return all the instance variables in ``Minion`` so that we can directly print the object values of the minion Kevin.


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
    public String toString()
    {
        // Code here
    }
}
// Create minion object Kevin
Minion kevin = new Minion(4.10,"Kevin","Sprout-Cut",2);

// Print Kevin Object
System.out.println(kevin);
```

    Name:Kevin
    Height: 4.1
    Hair:Sprout-Cut
    Eyes: 2


## When Creating a toString Accessor Method...
- You cannot change the header of the method public String toString() -> cannot change this
- Always returns string
- Doesn't take any parameters
- When System.out.printIn(object) is called on an object:
    - toString method is called
    - returned string is printed
