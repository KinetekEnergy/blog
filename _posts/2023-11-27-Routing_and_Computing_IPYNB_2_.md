---
comments: True
layout: post
title: 4.2 & 4.3 Routing and Computing
description: By Nikki, Eun, Arthur, and Patrick
tags: ['hacks']
categories: ['CSP', 'Week 14']
---

# 4.2 Routing (Fault Tolerance)

<mark>CSN-1.E.1</mark> The Internet has been engineered to be fault-tolerant, with abstractions for routing and transmitting data.

<mark>CSN-1.E.2</mark> <font color = "#FFA500">Redundancy</font> is the inclusion of extra components that can be used to mitigate failure of a system if other components fail.

<mark>CSN-1.E.3</mark> One way to accomplish <font color = "#FFA500">network redundancy</font> is by having more than one path between any two connected devices.

<mark>CSN-1.E.4</mark> If a particular device or connection on the Internet fails, subsequent data will be sent via a different route, if possible.

<mark>CSN-1.E.5</mark> When a system can support failures and still continue to function, it is called <font color = "#FFA500">fault-tolerant</font>. This is important because elements of complex systems fail at unexpected times, often in groups, and fault tolerance allows users to continue to use the network.

<mark>CSN-1.E.6</mark> Redundancy within a system often requires additional resources but can provide the benefit of fault tolerance.

<mark>CSN-1.E.7</mark> The redundancy of routing options between two points increases the reliability of the Internet and helps it scale to more devices and more people.


## Network Examples

In these examples the letters represent computing devices and the lines represent wires that connect the devices.

<!-- ![Redundancy Example](..images/RedundancyExample.png)
![Fault Tolerance Example](..images/FaultTolerance.png) -->

# 4.3 Sequential, Parallel, and Distributed Computing


## Computer Tasks
 
 - A computer needs to handle many tasks as it operates:
	- <font color = "#FFA500">System Tasks</font>: the operating system has dozens of tasks, like scheduling what it 
    will be doing next, managing hardware, working with the network, etc.
    - <font color = "#FFA500">User Tasks</font>: executing programs that the user has selected, such as running MS 
    Excel and MS Word, or computer games
- Tasks need to be scheduled by the operating system. Balance tasks so all CPUs are being
used evenly and fully.
- Running tasks can be done sequentially, in parallel, and be distributed to other computers.

## Sequential Computing

- <font color = "#FFA500">Sequential Computing</font>: Tasks are done one after another. It is a computational model in which operations are performed in order one at a time.
- The computer works tasks A, B, C, … one at a time.
- Why do this? 
	- It has <font color = "#FFA500">limited hardware</font>: It only has one CPU (older hardware)
    - Its <font color = "#FFA500">tasks are dependent</font>: Task B depends on Task A, Task C depends on Task B, so the needed order is A, B, and finally C.
- Execution Time: Sequential Operations add up all the individual task execution times.
- Example: 
	- Task A takes 50 ms
	- Task B takes 40 ms
	- Task C takes 35 ms
	- Total processing time is 50 ms + 40 ms + 35 ms = 125 ms
- Think of sequential computing as items one at a time on a conveyor belt.

	<!-- ![Sequential Computing](..images/SequentialComputing.png) -->

## Parallel Computing

- <font color = "#FFA500">Parallel Computing</font>: A computational model where the program is broken into multiple smaller sequential computing operations, some of which are performed simultaneously.
    - schedules tasks to be executed at the same time
    - normally done on the same computer
    - consists of a parallel portion and a sequential portion
- Comparing efficiency of solutions can be done by comparing the time it takes to perform the same set task.
- Why Parallel Computing?
    - <font color = "#FFA500">Hardware Driven</font>: New hardware has several processors in one system, called cores. 1 CPU can have 64+ cores. Graphic cards for gaming can have thousands of cores.
    - Faster Operations: Supercomputers link hundreds of CPUs together to work the same problem.
    - <font color = "#FFA500"> Data Driven</font>: A lot of data can be processed the same way (video gaming), called SIMD (Single Instruction Multiple Data)
    - Solutions that use parallel computing can scale more effectively than solutions that use sequential computing
- Execution Time:
    - Time equals the longest time taken on any given processor,
    - A parallel computing solution takes as long as its sequential tasks plus the longest of its parallel tasks.
    - Parallel processing works best when the tasks are independent from each other– they don’t depend on each other’s answers.
- Example: 
    - Core 1: Task A takes 45 ms
    - Core 2: Task B takes 50 ms
    - Core 3: Task C takes 25 ms; Task D takes 30 ms
    - Core 4: Task E takes 40 ms
    - Total time needed: 55 ms (Core 3 with Tasks C and D in sequence)
  
    <!-- ![Parallel Computing](..images/ParallelComputing.png) -->


## <font color = "4895EF"> Popcorn Hack 1 </font>

<font color = "4895EF"> 

A particular computer has two identical processors which can run in parallel. Each process must be executed on a single processor and each processor can only run one process at a time.

The table below lists the amount of time it takes to execute each of the processes on a single computer. None of the processes are dependent on any of the others.

What is the minimum amount of time (approximate) to execute all three processes when the two processors are run in parallel?
**The minimum time is determined by the longest processing time which is X or 50 seconds**

| Process  | Execution Time on Either Processor |
| ----------- | ----------- |
| X | 50 seconds |
| Y | 10 seconds |
| Z | 30 seconds |

 </font>

## Comparing Efficiency of Solutions

- Comparing efficiency of solutions can be done by comparing the time it takes them to perform the same task.
- <font color = "#FFA500">Sequential Execution Time</font>:				
    - Sequential Operations add up all the individual task execution times.
        - Core 1: Task A takes 50 ms
        - Core 1: Task B takes 40 ms
        - Core 1: Task C takes 35 ms
        - Total processing time is 50 ms + 40 ms + 35 ms = 125 ms
- <font color = "#FFA500">Parallel Execution Time</font>:
    - Time equals the longest time taken on any given processor.
    - Parallel processing works best when the tasks are independent from each other–they don’t depend on each other’s answers.
        - Core 1: Task A takes 50 ms
        - Core 2: Task B takes 40 ms + Task C takes 35 ms
        - Total time needed: 75 ms (Core 2 with Tasks B and C in sequence)

| Parallel  | Sequential |
| ----------- | ----------- |
| time = longest time taken on any given processor, aka faster| time = add up all individual task times aka slower|
| tasks done simultaneously| tasks done individually |
| good for big problems | good for small problems|
| harder to implement | easier to implement |
| less portable | more portable |

## Speedup Time

- The <font color = "#FFA500">“speedup” of a parallel solution</font> is measured in the time it took to complete the task sequentially divided by the time it took to complete the task when done in parallel.
  - Sequential Total processing time is 50 ms + 40 ms + 35 ms = 125 ms
  - Parallel Total time needed = 75 ms
  - Speedup 125 ms / 75 ms = 1.67 ms


*<mark>NOTE</mark>: When increasing the use of parallel computing in a solution, the efficiency of the solution is still restricted by the sequential portion. This means that at some point, adding parallel portions will no longer significantly increase efficiency.*


## Distributed Computing

- <font color = "#FFA500">Distributed Computing</font>: the sending of tasks from one computer to one or more others. It is a model in which multiple devices are used to run a program.
    - can mix sequential and parallel computing, based on how it sends out tasks to other computers to work
    - allows problems to be solved that could not be solved on a single computer because of either the processing time or storage needs involved
- Examples:
    - Google Web Search: you ask for a search, and Google sends the request to its thousand of servers in the background.
    - Web Services: standards on how computers can ask for task execution over the web. This includes protocols like SOAP, RSS, REST, etc.
    - <font color = "#FFA500">Beowulf Clusters</font>: special software to group different computers together 
- How is it different from sequential and parallel execution?
    - Uses more than one physical computer
    - The computers, data, and tasks can be very different from each other
    - Needs a network
    - Is a mix of sequential and parallel execution of tasks
    - Can take longer based on the network and waiting for responses from other computers
  
  <!-- ![Distributed Computing](..images/DistributedComputing.png) -->

## <font color = "FFC0CB"> Hacks: Multiple Choice </font>

Record your answers in the cell below, titled "Write Answers Here." 

1. Which of the following is NOT a benefit of a fault-tolerant network?
  - A) Data has more than one path to travel from one device to another.
  - B) If part of the netowrk fails, the network can still function by using other parts.
  - C) Data will only take one route from one device to another, no matter the number of routes available.
    - **The whole point of a fault tolerant network is that you have several routes which data can take if one route doesn't work**
  - D) More devices creates more connections and makes the network stronger.

2. What causes network redundancy?
  - A) Having more than one path between any two connected devices
    - **Redundancy means that you need more than one path**
  - B) Having one path between any two connected devices 
  - C) Having no path between any two connected devices
  - D) All networks are redundant

<br>

1. A computer has two duplicate processors that are able to run in parallel. The table below shows the amount of time it takes each processor to execute each of the two processes. Neither process is dependent on the other.

  | Process  | Execution Time on Either Processor |
  | ----------- | ----------- |
  | A | 25 seconds |
  | B | 45 seconds |
  
  What is the difference in execution time between running the two processes in parallel in place of running them one after the other on a single processor?
  - A) 50 seconds 
  - B) 25 seconds
    - Longest time is B or 45 seconds.
    - A + B = 75 seconds
    - If parallel, then Sequential - Parallel => 75 - 45 = 25 seconds
  - C) 70 seconds
  - D) 22 seconds

  <br>

1. A computer has two processors that can run in parallel. The table below indicates the amount of time it takes each processor to execute four different processes. None of the processes is dependent on any of the other processes.

  | Process  | Execution Time on Either Processor |
  | ----------- | ----------- |
  | A | 25 seconds |
  | B | 25 seconds |
  | C | 10 seconds |
  | D | 40 seconds |

  How should the program assign the four processes to optimize execution time? 
  - A) Processes B and C should be assigned to one processor and A and D to the other processor. 
  - B) Process B should be assigned to one processor and Process C to the other processor. 
  - C) There is no way to optimize execution time; this will be very slow. 
  - D) Processes A and B should be assigned to one processor and C and D to the other processor.

## <font color = "FFC0CB"> Write Answers Here </font>

After you record your answers in this cell, take a screen shot of the cell and DM it to Nikki Hekmat on Slack. There will be a penalty of 10% off your grade for each day the assignment is late. The homework will be **due Monday December 4th at 11:59 PM**. 

### <font color = "FFC0CB"> Popcorn Hack Answer </font>

[blank] seconds

### <font color = "FFC0CB"> MC Hacks Answers </font>

Simply put A, B, C, or D next to each number to indicate the correct answers for the questions above. 

1. 
2. 
3. 
4. 

# Homework

Question 1: What is parallel computing?
- Parallel computing is when multiple processors are used at the same time to run multiple processes at the same time on a single program

Question 2: If there is a computer with 3 cores that can each take one task, and the tasks are 25ms, 632ms and 100ms in run time respectively, how long will the program take to run?
- It will take 632 ms because the time is based off of the longest time

Question 3: Is sequential or parallel computing more efficient, and why?
- It depends but parallel is usually more efficient because it can run multiple tasks at the same time with less time

Question 4: What is the term called when a network has multiple paths leading up to one destination? (Used in fault-tolerant systems)
- It is called redundancy.
