---
title: Unit 5 Classes and Objects -  Anatomy
author: me
date: 2024-09-16
categories: ['Team Teaches', 'Unit 5 Team Teach']
render_with_liquid: False
---

## Anatomy of a Class

what is a class
In object-oriented programming (OOP), a class is a blueprint for creating objects, which are the building blocks of a program. A class is a template that defines the variables and methods for a specific type of object.

A class is composed of several key components that define its structure, behavior, and interaction with objects. Following are the key components of a class:

### Class Declaration
This is the starting point of any class. It includes the class keyword, class name, and access modifiers (public, private, etc.). It is a common convention to capitalize the first letter of the class name.


```python
public class Minions {
    // class body
}

```

### Instance Variables
Instance variables represent the attributes of the class. These variables are declared inside the class but outside any method. Instance variables are normally set as private variable and can be accessed using Accessor and Mutator methods.


```python
public class Minions {
    private String color;
    private int num_eyes;
}

```

### Constructors
A constructor is a special method that is called when an object is instantiated. It typically initializes the object’s fields.

1. Default constructor: A constructor with no parameters.
1. Overloaded constructor: A constructor that accepts parameters to initialize fields.


```python
public class Minions {
    private String color;
    private int num_eyes;
    
    // Default constructor
    public Minions() {
        color = "";
        num_eyes = 0;   
    }

    // Overloaded constructor
    public Minions(String c, int n) {
        color = c;
        num_eyes = n;
    }
}
```

### Methods
Methods define the behavior of a class. These are functions that operate on the class’s data (fields) or provide functionality.

1. Accessor methods (Getters): Used to retrieve field values.
1. Mutator methods (Setters): Used to modify field values.


```python
public class Minions {
    private String color;
    private int num_eyes;
    
    // Default constructor
    public Minions() {
        color = "";
        num_eyes = 0;   
    }

    // Overloaded constructor
    public Minions(String c, int n) {
        color = c;
        num_eyes = n;
    }

    //Accessor Methods
    public String getColor() {
        return color;
    }

    public int getnumeyes(){
        return num_eyes;
    }

    //Mutator Methods
    public void setColor(String c){
        color = c;
    }

    public void setNumeyes(int n){
        if(n < 0 || n > 2){
            num_eyes = 1; //default value
        }
        else {
            num_eyes = n;
        }
    }
}
```

### Data Encapsulation
Encapsulation is achieved by making instance variables private and providing public getter and setter methods to access and update the fields. This ensures that the internal implementation is hidden from the user and protects the object’s state. The setter method can contain validation logic that ensures only valid data is assigned to the field.

### Popcorn Hack 1.

Write a Student class. 
    - Each student has a name 
    - Each student has a score (out of 100)
    - A student passes if their score is above 70

Check which student passes (write a class header, instance variables, constructors, and methods)


```python
public class Student {
    private String name;
    private int score;
    
    // Default constructor
    public Student() {
        name = "";
        score = 0;   
    }

    // Overloaded constructor
    public Student(String n, int s) {
        name = n;
        score = s;
    }

    //Accessor Methods
    public String getName() {
        return name;
    }

    public int getScore(){
        return score;
    }

    //Mutator Methods
    public void setName(String n){
        name = n;
    }

    public void setScore(int s){
        if(s < 0 || s > 100){
            score = 0; //default value
        }
        else {
            score = s;
        }
    }

    public boolean pass(){
        return (score >= 70);
    }
}
```
