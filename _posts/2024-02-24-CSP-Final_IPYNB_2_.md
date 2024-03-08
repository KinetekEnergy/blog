---
title: CSP Final
categories: ['CSP', 'Week 21']
tags: ['hacks']
comments: True
---

# Individual Review

## Project Summary

TV isn’t as popular as it used to be. Instead, people like to watch content on their computers. To cater to this, our
project is a video sharing platform. It allows people to create accounts and upload videos. You can share videos with
others, watch videos, and create your own!


### My Feature

My feature is a login system which handles user creation, account modification, and error handling (ex: 401 or 403
errors).


## Component A: Program Code

### CB

Instructions for input from one of the following:



* The user (including user actions that trigger events)
* A device
* An online data stream
* A file


### Me

In our project, the user can upload a video file and an image. The video file will be the video that plays and the image can be a video preview (typically called a “thumbnail). The user also inputs a title for the video and a description.

<hr style="height: 5px; background-color: #74b2f3; opacity: 1; border-radius: 5px">

### CB

Use of at least one list (or other collection type) to represent a collection of data that is stored and used to manage program complexity and help fulfill the program's purpose.


### Me

For our project, the collected data are the videos which are stored in the backend. Each time a user uploads a video, the backend is updated. It helps to fulfill the program’s purpose because our program is a video sharing website. It lets people watch and share videos.



* Data stored in SQLite
* JSON collection to pass data

<hr style="height: 5px; background-color: #74b2f3; opacity: 1; border-radius: 5px">

### CB

At least one procedure that contributes to the program's intended purpose, where you have defined:
* the procedure's name
* the return type (if necessary)
* one or more parameters


### Me

* This procedure’s purpose is to update a user’s email.
* Name: `post`.
* Return: returns different values based on what is sent to it. If there is no UID or email, it returns a `400` error. Any other errors return `500`. 
* Parameter(s): `self`

<img src="images/update.png" width="" alt="alt_text" title="image_tooltip">

<hr style="height: 5px; background-color: #74b2f3; opacity: 1; border-radius: 5px">

### CB

An algorithm that includes sequencing, selection, and iteration that is in the body of the selected procedure


### Me

This function uses sequencing and iterates through each user. It selects each part of their user information such as name, email, etc. and prepares it for use in a json. This can be accessed on the frontend via an admin panel.

<img src="images/iteration.png" width="" alt="alt_text" title="image_tooltip">

<hr style="height: 5px; background-color: #74b2f3; opacity: 1; border-radius: 5px">

### CB

Calls to your student-developed procedure


### Me

Calls the backend procedure and fetches the data to load.

<img src="images/adminpanel.png" width="" alt="alt_text" title="image_tooltip">

<hr style="height: 5px; background-color: #74b2f3; opacity: 1; border-radius: 5px">

### CB

Instructions for output (tactile, audible, visual, or ) based on input and program functionality


### Me

Now, the json data is formatted into a table. All content is dynamically updated and automatically formatted with CSS.

<img src="images/visuals.png" width="" alt="alt_text" title="image_tooltip">

## Component B: Video

[**Link to video**](https://youtu.be/gd6uUlJ50Z0)

[**Link to video on our deployed project**](https://napoleon-bonaparte-official.github.io/corsica-frontend/video?videoID=9)

|College Board Requirements|What I Did|
|-|-|
|Input to your program|✔️|
|At least one aspect of the functionality of your program|✔️|
|Output produced by your program|✔️|
|No distinguishing information about yourself|✔️|
|No voice narration|✔️|
|Either .mp4, .wmv, .avi, or .mov format|✔️(.mp4)|
|No more than 1 minute in length|✔️|
|No more than 30MB in file size|✔️|
|CPT Style which highlights the project feature|✔️|

> All College Board requirements are from [https://apclassroom.collegeboard.org/103/home?apd=7wv87bhksv&unit=0](https://apclassroom.collegeboard.org/103/home?apd=7wv87bhksv&unit=0)
{: .prompt-info }

# Team Review

## Features Prior to Implementation

Description of features prior to implementation:



* Design and planning
* Key features
* [Features prior to implementation](https://kinetekenergy.github.io/blog/posts/Checkpoint_IPYNB_2_/)

Planning table of issues and features:

Features:

|Features|Link|
|-|-|
|View count which updates whenever someone views a video|[Issue](https://github.com/Napoleon-Bonaparte-Official/corsica-blog/issues/3)|
|Video categories to sort videos and choose which category to watch|[Issue](https://github.com/Napoleon-Bonaparte-Official/corsica-blog/issues/3)|
|Login feature which connects to upload. When uploading a video, the user who uploaded it will be in the description and this will be automatic.|[Issue](https://github.com/Napoleon-Bonaparte-Official/corsica-blog/issues/3)|
|Deleting user accounts and updating an email so that users can close their account and update information|[Issue](https://github.com/Napoleon-Bonaparte-Official/corsica-blog/issues/3)|
|Allow users to add a description to their videos. They can also add a tag so that the category feature sorts it|[Issue](https://github.com/Napoleon-Bonaparte-Official/corsica-blog/issues/3)|

|Issue|Solution|
|-|-|
|View counter was not updating|The HTML request had to be a `1PUT` so that it could update the view count. It should then commit to `db` with `db.commit()`. [Fix](https://github.com/Napoleon-Bonaparte-Official/corsica-backend/commit/240de7cd9cf8040637bb87eec5bf8264565cab1b) & [Issue](https://github.com/Napoleon-Bonaparte-Official/corsica-blog/issues/3)|
|Return errors were all messed up and weren’t returning the correct error code (this error actually showed up during a live review but was fixed on-the-fly).|The `return` code allows you to choose the error. This needed to be set properly because we had messed up the codes. [Fix](https://github.com/Napoleon-Bonaparte-Official/corsica-backend/commit/6352cfac8f3f499751d44ce573be3aadc324f4fb) & [Issue](https://github.com/Napoleon-Bonaparte-Official/corsica-blog/issues/3)|
|Adding a video would be NULL and the video id in the URL wouldn’t work.|Code was reordered so that the video id was put properly: `self._videoID = self.id` was changed to be last so that the video id is updated last and isn’t changed. [Fix](https://github.com/Napoleon-Bonaparte-Official/corsica-backend/commit/00f2e4a3f99cea3a05d50674e7b41cafccd83410) & [Issue](https://github.com/Napoleon-Bonaparte-Official/corsica-backend/commit/00f2e4a3f99cea3a05d50674e7b41cafccd83410)|
|Users could add random text for emails and junk text.|A filter was added so that emails must contain an “@” symbol as well as being over five characters. [Fix](https://github.com/Napoleon-Bonaparte-Official/corsica-backend/commit/29073c9a91fa89dc4b7ab29a261e13d296cda4a3) & [Issue](https://github.com/Napoleon-Bonaparte-Official/corsica-backend/commit/00f2e4a3f99cea3a05d50674e7b41cafccd83410)|
|Video thumbnails were not working.|The image in the backend is stored as a base64 and is sent to the front end. However, there were issues in the javascript decoding. To fix this, a `regex` was implemented so that the base64 is cleaned up and is displayed properly. [Fix](https://github.com/Napoleon-Bonaparte-Official/corsica-frontend/commit/bbce2f295fe3414cd2a97ae3b756fe65d57ffc87) & [Issue](https://github.com/Napoleon-Bonaparte-Official/corsica-backend/commit/00f2e4a3f99cea3a05d50674e7b41cafccd83410)|


