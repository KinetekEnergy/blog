---
title: Unit 5 Writing Methods
author: me
date: 2024-09-17
categories: ['Team Teaches', 'Unit 5 Team Teach']
render_with_liquid: False
---

<img src="https://github.com/user-attachments/assets/b6e29141-321e-4ec4-a0fe-abf747eb6baa">

## What is a Method?!
> A method is a **block of code that belong to a class**, very similar to a function. 

Methods in Java can take inputs (parameters), perform actions, and return a value (or void if no value is returned).

Methods that are created by the programmer to perform tasks are called **user-defined methods**, while other methods can be built in (like System.out.println()).

## Types of methods:
There are many different types of methods in Java, but here I'll only highlight the two most common ones and the ones used by College board.

> Instance Methods: Methods that belong to an **instance** of a class
Instance methods require an object of the class to be used. They operate on objects of the class.
- Can access instance variables and other instance methods within the class
- Can access static variables and methods

> Static Methods: Methods that belong to the class itself trather than any instance of the class. Trhey are used for operations taht do not depend on instance-spefific data. 
- Can only directly access other static variables and methods.

## Here's a quick example!
- Example of an instance method: addMinion()
  - Adds a minion to the list of a villain
  - Parameters: String minon
  - Example call: gru.addMinion("Kevin")
- Second example of an instance method: Villain()
  - Changes instance data
  - Parameters: string Name, String evilPlan

- Example of a static method: getVillainCount()
  - Returns the total amount of Villain instances
  - No parameters
  - Example call: System.out.println("There are " + Villain.getVillainCount() + " villains in the world.");

## Popcorn hack:
- Add another static method to the Villain class
- Keep it minion themed and fun!


```java
import java.util.ArrayList;
import java.util.List;

public class Villain {
    // Instance variables
    public String name;
    public String evilPlan;
    public List<String> minions;
    public static int villainCount = 0;

    // Constructor for name, plan, and minions
    public Villain(String name, String evilPlan) {
        this.name = name;
        this.evilPlan = evilPlan;
        this.minions = new ArrayList<>();
        villainCount++;
    }

    // Instance method to add a minion. LOOK HERE!!
    public void addMinion(String minion) {
        minions.add(minion);
        System.out.println(minion + " has been added to " + name + "'s army.");
    }

    // Instance method to describe the villain. 
    public void describeVillain() {
        System.out.println(name + " is planning to: " + evilPlan);
        System.out.println("They have " + minions.size() + " minions.");
    }

    // Static method to get the total count of villains
    public static int getVillainCount() {
        return villainCount;
    }
}

public class Main {
    public static void main(String[] args) {
        Villain.villainCount = 0;

        // Create new villains
        Villain gru = new Villain("Gru", "steal the moon!");
        Villain vector = new Villain("Vector", "take over the world with magnitude and direction!");

        System.out.println("=== Adding Minions ===");
        // Create some minions
        gru.addMinion("Kevin");
        gru.addMinion("Stuart");
        gru.addMinion("Bob");

        // Create some minions for Vector
        vector.addMinion("Henchman 1");

        System.out.println();

        // Describe the villains and their plans
        System.out.println("=== Villain Descriptions ===");
        gru.describeVillain();
        System.out.println();
        vector.describeVillain();
        System.out.println();

        // Get the total count of villains
        System.out.println("=== Total Villain Count ===");
        System.out.println("There are " + Villain.getVillainCount() + " villains in the world.");
    }
}

Main.main(null);
```

    === Adding Minions ===
    Kevin has been added to Gru's army.
    Stuart has been added to Gru's army.
    Bob has been added to Gru's army.
    Henchman 1 has been added to Vector's army.
    
    === Villain Descriptions ===
    Gru is planning to: steal the moon!
    They have 3 minions.
    
    Vector is planning to: take over the world with magnitude and direction!
    They have 1 minions.
    
    === Total Villain Count ===
    There are 2 villains in the world.


## Popcorn hack:
Dr. Nefario is busy assigning work for the minions, and he needs your help to organize his group. Your mission is to write and implement a Java classes for each minion which includes their name, gadgets, personality, and more. Get ready to make Dr. Nefario's life easier and keep the minions organized!
