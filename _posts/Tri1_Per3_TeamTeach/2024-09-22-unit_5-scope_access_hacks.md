---
title: Unit 5 Scope and Access
author: me
date: 2024-09-22
categories: ['Team Teaches', 'Unit 5 Team Teach']
render_with_liquid: False
---

<img src="https://github.com/user-attachments/assets/317d0cb3-0d1b-4c31-8e4f-3f66f47d1a9c" width='500px' height='auto'>

## Scope and Access

## Local Scope
- Local variables can be ``declared in the body of constructors and methods``. These variables may only be used within the constructor method and cannot be declared to be **public** or **private**

- When there is a local variable with the same name as an instance variable, the variable name will refer to the local variable instead of the instance variable

- Formal parameters and variables declared in a method or constructor can only be used within that method or constructor


```Java
public class LocalScopeExample{
    public void Local()
    {
        int a = 10;//Defining a local variable
        if (a > 5)
        {
            int b = 20;//Defining a variable in the local scope of this if statement
        }
            // Try to access the local variable outside the class
        System.out.println(b);

    }
}
LocalScopeExample example = new LocalScopeExample();
example.Local(); // This will print: Value of b: 20
```

## Class Level Scope
- Instance variables will be accessible **anywhere within the class** and they can be used in all of the methods in the class. If the variable is defined as ``private`` the variable will not be accessible outside of the class. If it is defined as public, it allows access to a class, method or variable from ``both inside and outside the class.``


```Java
public class LocalScopeExample{
    // Defining an instance variable
    private int b = 10;

    public void Local()
    {
        int a = 10;//Defining a local variable
        if (a > 5)
        {
            b = 20;//Defining a variable in the local scope of this if statement
        }
            // Try to access the local variable outside the class
        System.out.println("Value of b: " + b);
    }
}
LocalScopeExample example = new LocalScopeExample();
example.Local(); // This will print: Value of b: 20
```

## Let's go through an example

Lets create a class called MinionMood. In order to ensure maximum productivity with the minions we have to keep track of how they're feeling throughout the day.

Then lets create some instance variables and a method to increase the happiness level of the minion based on how many bananas they have eaten, and make it such that the energy level of the minion decreases based on how many tasks they have to complete.


```Java
public class MinionMood
{
    private int happinessLevel;
    private int energyLevel;

    public MinionMood(int bananas, int tasks)
    {
        int happinessLevel = 2*bananas;
        int energyLevel = tasks;
    }
    public String toString()
    {
        return "Happiness Level: " + happinessLevel + "\nEnergy Level: " + energyLevel;
    }
}

MinionMood bob = new MinionMood(5, 2);
System.out.println(bob);

```

## Popcorn Hack
- Figure out why the happiness level and the energy level is not showing up the way we want it to. First one to do so will get a high five from Trevor Huang.

## Oops...

Its very important to keep in mind that a local variable within a method that has the same name as an instance variable will just redeclare the variable. So, to make the code work the way we want it to, all that we have to do is get rid of the statements that redeclare the variable.s
