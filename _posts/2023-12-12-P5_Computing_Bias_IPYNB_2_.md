---
comments: True
layout: post
title: P5 Computer Bias
tags: ['hacks']
toc: True
categories: ['CSP', 'Week 16']
---

# Big Idea 5.3 Computing Bias- Tanay

Overview/Definition: Computing Biasses are the numerous Biasses in application that are based on human prefrences.

- Computing innovations can reflect existing human biases because of biases written into the algorithms or biases in the data used by the innovation
- Programmers should take action to reduce bias in algorithms used for computing innovations as a way of combating existing human biases
- Biases can be embedded at all levels of software development

## Types of Computing Bias - Tarun

- Data Bias: The data does not accurently represent the values of the real world
    ex. If data is taken from a sample size that doesn't reflect the actual population
        - If you wanted data to represent the population in America but your sample that is being surveyed is from a Texas. The population in Texas does not accurately reflect the entire population of America. 
- Human Bias: Those who make programs may be influenced by their own biases 
    ex. If a development team are experts in using a certain language and their algorithm demonstrates that language, they will feel that people who specialize in that language are qualified and better. This is essentially bringing in their personal biases and applying to a larger amount of people. 

## Explicit data vs Implicit data:  - Pranavi

Explicit data:
- takes the data that you give
- When watching a video, and it asks "are you enjoying this?", and you respond with either a thumbs up or down, you are giving them explicit data

Implicit data:
- When you watch or search up certain things, data can be deduced on what is the "norm" for the person

Example: Netflix
- When browsing through Netflix, they show Netflix exclusives, they do this because they want your subscriptions 
- showing the netflix exclusives is the bias in this scenario

<!-- ![Screenshot 2023-12-12 at 1.22.41 PM.png](<attachment:Screenshot 2023-12-12 at 1.22.41 PM.png>) -->


## Popcorn Hack:

In what other applications could have intential bias? Other streamins services like Disney+

## Intentional Bias vs Unintentional Bias - Tanvi

Example 1: Hypothetical Loan company
- Suppose a software was created to assist loan officers, and certain trends of successful loans were taken
- If people are rejected of those who don't fit in their trends of either age, gender, race, etc.
- This software is biased in the way that it only chooses candidates who will have higher chances in successful loans

Example 2: Candy Crush vs Call of Duty
- Call of Duty is geared towards the teenage boy demographic, 18-24, with more grunge type of music
- Candy Crush is more visually appearing to younger audience as it includes pictures of candies and playful music 
- This is biased as the games include aspects and characteristics that will seem appealing to a specific audience 

<!-- ![Screenshot 2023-12-12 at 1.23.36 PM.png](<attachment:Screenshot 2023-12-12 at 1.23.36 PM.png>)

![Screenshot 2023-12-12 at 1.23.42 PM.png](<attachment:Screenshot 2023-12-12 at 1.23.42 PM.png>) -->


## Popcorn Hack:
How is their unintentional bias in apps such as TikTok or Instagram or otehr social media apps? Unintentional bias because the user base is younger --> mainly younger people join --> snowball effect

## Mitigation Strategies - Shubhay 

- Utilize data from various sources
- Pre-Processing: A way to check the inputs for bias before it is being used as data
- In-processing: This algorithm changes the data during analysis of the data to keep the data consistent
- Post-Processing: # step check to make sure the model is fair and accurate
    - Input Correction: This strategy makes adjustments to the data to make the data more comparable
    - Classifier Correction: polishing and adjusting the algorithm after it has been trained to reduce the biases
    - Output Correction: The predictions made by the model is modified to eliminate biases

## Homework:

1. Is bias enhancing or intentionally excluding?
   1. It can depend. Unintentional bias can enhance in some scenarios (if you're lucky). For example, if a machine learning model is trained on a dataset that reflects a specific demographic more than others, it may perform better for that particular group but may not generalize well to other demographics. On the other hand, unintentional bias can lead to exclusion. If a system is trained on biased data, it might not accurately represent or address the needs of underrepresented groups, leading to exclusion or unfair treatment.
2. Is bias intentionally harmful/hateful?
   1. Bias itself is not inherently harmful or hateful but its application or implementation can be. For example, if someone purposely adds bias to a system. Examples of intentional bias could be discriminatory algorithms which favor certain people based off of specific demographics or hateful content recommendation that promotes hateful or harmful content (this can lead to the spread of misinformation). Actually, this can be seen in social media platforms but this is actually unintentional bias as it wasn't intended to have harmful content be spread. Biased decision-making systems are also harmful: example being things used to hire people. 
3. During software development are your receiving feedback from a wide variety of people?
   1. Yes because that elimantes bias. There are various ways to do this. For example, you can do user testing where developers release their product for user feedback and to improve user experience. Beta testing is also another term for this. Code reviews are a good example by allowing developers to review each other and make sure everything works. Feedback from a diverse group of users and stakeholders is essential for creating software that meets the needs of its intended audience and functions reliably. It helps improve the quality of the software, identify potential problems, and align development efforts with user expectations.
4. What are the different biases you can find in an application such as Youtube Kids?
   1. One type of bias is content bias. For example, content available could be biased towards specific cultures or regions and can lack representation. Algorithms may unintentionally promote discriminatory content. Other types of bias could be language bias with less languages being available which is not inclusive.
