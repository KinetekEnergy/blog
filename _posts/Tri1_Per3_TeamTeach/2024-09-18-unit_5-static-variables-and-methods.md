---
title: Unit 5 Static Variables and Methods
author: me
date: 2024-09-18
categories: ['Team Teaches', 'Unit 5 Team Teach']
render_with_liquid: False
---

<img src="https://github.com/user-attachments/assets/526e3a43-a642-4112-8b33-8038b57832cd">

## What are static variables?
> Static variables: belong to the class rather than a particular instance. 
- These types of variables are variables shared across all instances of a class.


```Java
import java.util.ArrayList;
import java.util.List;

public class Gadget {
    public static int totalGadgets = 0;  // Static variable to track total gadgets made
    private String gadgetName;  // Instance variable to store the name of the gadget
    //public static List<Gadget> gadgetsList = new ArrayList<>();  // Static list to track all gadgets

    // Constructor to set the gadget name and increment totalGadgets
    public Gadget(String gadgetName) {
        this.gadgetName = gadgetName;
        totalGadgets++;  // Increment the total gadgets count
        // gadgetsList.add(this);  // Add this gadget to the static list
    }

}
// In the Main class:
public class Main {
    public static void main(String[] args) {
        // Create three gadgets
        Gadget g1 = new Gadget("Freeze Ray");
        Gadget g2 = new Gadget("Banana Blaster");
        Gadget g3 = new Gadget("Lipstick Taser");

        // Print the total number of gadgets
        System.out.println("Total gadgets made: " + Gadget.totalGadgets);
    }
}

Main.main(null);

```

    Total gadgets made: 3


## Cool, but why did I have to use a static variable?
- The totalGadgets was made as a static variable because it is tracking data that is shared across **all instances** of the Gadget class.
- If totalGadgets was an instance variable, then it would always be 1 since it would only reflect how many gadgets are in the specific instance.

## Popcorn hacks:
- Look at some of the code I've commented out and try experimenting with gadgetsList if you want. Otherwise, just make a static variable that serves a purpose in the program.

## What are static methods?
> Static methods are associated with the class and not any object of the class
- Static methods can only directly access other static methods and static variables of the class. 
- They cannot use the "this" keyword because they don't belong to any instance.

## Here's an example:


```Java
import java.util.ArrayList;
import java.util.List;

public class Gadget {
    public static int totalGadgets = 0;  // Static variable to track total gadgets made
    private String gadgetName;  // Instance variable to store the name of the gadget
    public static List<Gadget> gadgetsList = new ArrayList<>();  // Static list to track all gadgets

    // Constructor to set the gadget name and increment totalGadgets
    public Gadget(String gadgetName) {
        this.gadgetName = gadgetName;
        totalGadgets++;  // Increment the total gadgets count
        gadgetsList.add(this);  // Add this gadget to the static list
    }

    // Getter for the gadget name
    public String getGadgetName() {
        return gadgetName;
    }

    // Static method to print all gadgets in the list
    public static void printAllGadgets() {
        System.out.println("Gadgets created:");
        for (int i = 0; i < gadgetsList.size(); i++) {
            System.out.println("- " + gadgetsList.get(i).getGadgetName());
        }
    }
}

// In the Main class:
public class Main {
    public static void main(String[] args) {
        // Create three gadgets
        Gadget g1 = new Gadget("Freeze Ray");
        Gadget g2 = new Gadget("Banana Blaster");
        Gadget g3 = new Gadget("Lipstick Taser");

        // Print the total number of gadgets
        System.out.println("Total gadgets made: " + Gadget.totalGadgets);

        // Print all gadgets stored in the static list
        Gadget.printAllGadgets();
    }
}

Main.main(null);

```

    Total gadgets made: 3
    Gadgets created:
    - Freeze Ray
    - Banana Blaster
    - Lipstick Taser


## Why did I use a static method?
- Static methods can only directly access other static variables and methods, such as gadgetsList
- I needed to print inforamtion about all instances of the Gadget class, which applied to the entire class as a whole.

## Popcorn hack:
Dr. Nefario and Gru need to calculate the cost of their equipment to remain under the budget for this year! Add a second parameter to the Gadget constructor to include cost for Gadget instances, and make a static method to calculate the price of all gadgets that have been made so far.
