---
title: Unit 5 This Keyword
author: me
date: 2024-09-19
categories: ['Team Teaches', 'Unit 5 Team Teach']
render_with_liquid: False
---

# `This` Keyword

### General
- `this` keyword is used as a reference to the object itself
    - It can be used to reference the object’s instance variables, methods, constructors, etc.
    - Enables instance variables to access an object’s variables and methods
- It is used to avoid confusion between instance variables and parameter values (local variables)



```Java
public class Minion {
    private int banana = 5;
    public void setBanana(int banana) {
    this.banana = banana; //this.banana refers to the instance variable banana
    // banana refers to the parameter banana
    }
}
```

### Calling Another Constructor
- `this` keyword can be used to invoke another constructor of the same class

Format: this.(*argument*)



```Java
public class MinionGoggles {
    private double lensSize;
    public MinionGoggles(double lensSize) {
        this.lensSize = lensSize; //this keyword references the hidden data field, lensSize
    }
    public MinionGoggles() {
        this(1.0); //passes 1.0 as an argument to the 1st constructor
    }
}
```

### Calling Other Methods
- `this` keyword can be used to call other methods in the same class

Format: this.*methodName*()


```Java
public class Minion {
    private String name;

    public Minion(String name) {
        this.name = name;
    }

    public void run() {
        System.out.println(this.name + " is running");
        this.speak();  // Calls the speak method of the current object
    }

    public void speak() {
        System.out.println(this.name + " says: 'Bello!'");
    }
}
```

### Passing `this` as a Parameter
- `this` keyword can be used to pass the reference of the current object to a method or constructor
- Format: *methodName*(this)



```Java
class Minion {
    String name;

    Minion(String name) {
        this.name = name;
    }

    void printMinion(Student minion) {
        System.out.println("Minion name: " + minion.name);
    }
    
    void callPrintMinion() {
        printMinion(this); // Passes the current object to the method
    }
}

public class Main {
    public static void main(String[] args) {
        Student minion1 = new Minion("Kevin");
        minion1.callPrintMinion(); // Output: Minion name: Kevin
    }
}
```

## Popcorn Hacks
The Minions are preparing for a big event where the tallest and fastest minion will get to assist Gru on his next mission! You’ve been called in as the official "Minion Trainer" to help compare the minions. The goal is to see which minion is more prepared for the mission.

<img src="https://github.com/user-attachments/assets/04a96193-6551-4cf8-a169-29d7c93ad9fa" width="300" alt="Minion Image">



```Java
public class Minion {
    private String speed;
    private int height;

    public void Minion(String speed, int height) {
        this.speed = speed;
        this.height = height;
    }

    public void setHeight(int height) {
        this.height = height;  
    }

    public String getSpeed() {
        return this.speed;  
    }

    public boolean isTallerThan(Minion otherMinion) {
        return this.height > otherMinion.height;  
    }

    public static void main(String[] args) {
        Minion minion1 = new Minion("fast", 43);
        Minion minion2 = new Minion("medium", 28);

        System.out.println("minion 1 speed: " + minion1.getSpeed());
        System.out.println("Is minion1 taller than minion2? " + minion1.isTallerThan(minion2));

        minion2.setHeight(50);
        System.out.println("Is minion1 still taller than minion2? " + minion1.isTallerThan(minion2));
    }
}
```

1. What is the output of the statement *System.out.println("minion 1 speed: " + minion1.speed())*? Explain why the `this` keyword is useful in the *getSpeed()* method.

2. What does the *isTallerThan()* method compare?

3. What happens to the result of *System.out.println("Is minion1 taller than minion2? " + minion1.isTallerThan(minion2))* after *minion2.setHeight(50)* is called?


Who should be selected for the mission?🤔

🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌🍌
<br></br>
<img src="https://github.com/user-attachments/assets/8d88ae01-97dc-4b53-a297-5e8253a1fc91" width="300" alt="Pancake Image">

In the bustling kitchen of Gru’s secret lab, the Minions were on a mission to create the perfect pancake for their breakfast feast. Kevin needed to make sure each pancake was perfectly round, with the exact right circumference for maximum deliciousness. But how? He needed to figure out the precise relationship between the pancake’s radius and its circumference. Help Kevin create the perfect pancake!

The `MinionPancake` class below should have:
- A `radius` field
- A method `setRadius(double radius)`: have this set as the radius
- A method `calculateCircumference()`: have this calculate the circumference of a circle with radius 5 and print it
    - (hint: use Math.PI for 'π')


```Java
class MinionPancake {
    private double radius;

    public void setRadius(double radius) {
        // Use 'this' to set the radius
        
    }

    public void calculateCircumference() {
        // Calculate circumference and print result
        
    }
}

// Create a pancake with radius 5 and calculate its circumference
MinionPancake pancake = new MinionPancake();

```
