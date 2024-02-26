---
title: Table-test
categories: ['CSP', 'Week 21']
tags: ['hacks']
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

<style>
    td {
        word-wrap: break-word;
    }
</style>

<table>
    <tr>
        <td style="word-wrap: break-word;"><strong>College Board Requirements</strong>
        </td>
        <td style="word-wrap: break-word;"><strong>What I Did</strong>
        </td>
    </tr>
    <tr>
        <td style="word-wrap: break-word;">Instructions for input from one of the following:
            <ul>
                <li>The user (including user actions that trigger events)
                <li>A device
                <li>An online data stream
                <li>A file
                </li>
            </ul>
        </td>
        <td style="word-wrap: break-word;">In our project, the user can upload a video file and an image. The video file will be the video that plays
            and the image can be a video preview (typically called a “thumbnail). The user also inputs a title for the
            video and a description.
        </td>
    </tr>
    <tr>
        <td style="word-wrap: break-word;">Use of at least one list (or other collection type) to represent a collection of data that is stored and
            used to manage program complexity and help fulfill the program's purpose.
        </td>
        <td style="word-wrap: break-word;">For our project, the collected data are the videos which are stored in the backend. Each time a user uploads
            a video, the backend is updated. It helps to fulfill the program’s purpose because our program is a video
            sharing website. It lets people watch and share videos.
            <ul>
                <li>Data stored in SQLite
                <li>JSON collection to pass data
                </li>
            </ul>
        </td>
    </tr>
    <tr>
        <td style="word-wrap: break-word;">At least one procedure that contributes to the program's intended purpose, where you have defined:
            <ul>
                <li>the procedure's name
                <li>the return type (if necessary)
                <li>one or more parameters
                </li>
            </ul>
        </td>
        <td style="word-wrap: break-word;">
            <ul>
                <li>This procedure’s purpose is to update a user’s email.
                <li>Name: <code>post</code>.
                <li>Return: returns different values based on what is sent to it. If there is no UID or email, it
                    returns a <code>400</code> error. Any other errors return <code>500</code>.
                <li>Parameter(s): <code>self</code>
                    <img src="/images/update.png" width="" alt="alt_text" title="image_tooltip">
                </li>
            </ul>
        </td>
    </tr>
    <tr>
        <td style="word-wrap: break-word;">An algorithm that includes sequencing, selection, and iteration that is in the body of the selected
            procedure
        </td>
        <td style="word-wrap: break-word;">This function uses sequencing and iterates through each user. It selects each part of their user information
            such as name, email, etc. and prepares it for use in a json. This can be accessed on the frontend via an
            admin panel.
            <p>
                <img src="/images/iteration.png" width="" alt="alt_text" title="image_tooltip">
        </td>
    </tr>
    <tr>
        <td style="word-wrap: break-word;">Calls to your student-developed procedure
        </td>
        <td style="word-wrap: break-word;">Calls the backend procedure and fetches the data to load.
            <p>
                <img src="/images/adminpanel.png" width="" alt="alt_text" title="image_tooltip">
        </td>
    </tr>
    <tr>
        <td style="word-wrap: break-word;">Instructions for output (tactile, audible, visual, or ) based on input and program functionality
        </td>
        <td style="word-wrap: break-word;">Now, the json data is formatted into a table. All content is dynamically updated and automatically formatted
            with CSS.
            <p>
                <img src="/images/visuals.png" width="" alt="alt_text" title="image_tooltip">
        </td>
    </tr>
</table>
