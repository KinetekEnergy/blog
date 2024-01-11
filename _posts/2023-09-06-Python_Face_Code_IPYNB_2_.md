---
toc: True
comments: False
layout: post
title: Eye Tracking and Facial Recognition with Python
tags: ['hacks']
categories: ['CSP', 'Week 3']
---

```python
import face_recognition
import cv2

# Get a reference to webcam #0 (the default one)
video_capture = cv2.VideoCapture(0)

# Initialize some variables
face_locations = []

while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Resize frame of video to 1/4 size for faster face detection processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Find all the faces and face encodings in the current frame of video
    face_locations = face_recognition.face_locations(small_frame)

    # Display the results
    for top, right, bottom, left in face_locations:
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Extract the region of the image that contains the face
        face_image = frame[top:bottom, left:right]
        
        face_image = cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)        

    # Display the resulting image
    cv2.imshow('Video Feed: q to quit', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()
```

<hr style="solid">

### Blurring Faces


```python
import face_recognition
import cv2

# Get a reference to webcam #0 (the default one)
video_capture = cv2.VideoCapture(0)

# Initialize some variables
face_locations = []

while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Resize frame of video to 1/4 size for faster face detection processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Find all the faces and face encodings in the current frame of video
    face_locations = face_recognition.face_locations(
        small_frame)  # , model="cnn"

    # Display the results
    for top, right, bottom, left in face_locations:
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Extract the region of the image that contains the face
        face_image = frame[top:bottom, left:right]

        # Blur the face image
        face_image = cv2.GaussianBlur(face_image, (99, 99), 30)

        # Put the blurred face region back into the frame image
        frame[top:bottom, left:right] = face_image

    # Display the resulting image
    cv2.imshow('Video Feed: q to quit', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()

```

<hr style="solid">

### Recognizing Faces


```python
import face_recognition
import cv2
import numpy as np

# Get a reference to webcam #0 (the default one)
video_capture = cv2.VideoCapture(0)

# Load a sample picture and learn how to recognize it.
obama_image = face_recognition.load_image_file("obama.jpg")
obama_face_encoding = face_recognition.face_encodings(obama_image)[0]

# Load a second sample picture and learn how to recognize it.
aashray_image = face_recognition.load_image_file("aashray.jpg")
aashray_face_encoding = face_recognition.face_encodings(aashray_image)[0]

# Load a second sample picture and learn how to recognize it.
mortenson_image = face_recognition.load_image_file("mortenson.jpg")
mortenson_face_encoding = face_recognition.face_encodings(mortenson_image)[0]

# Create arrays of known face encodings and their names
known_face_encodings = [
    obama_face_encoding,
    aashray_face_encoding,
    mortenson_face_encoding
]
known_face_names = [
    "Barack",
    "Aashray",
    "Mr. Mortenson"
]

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Only process every other frame of video to save time
    if process_this_frame:
        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
        

        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(
            rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(
                known_face_encodings, face_encoding)
            name = "Unknown"

            # # If a match was found in known_face_encodings, just use the first one.
            # if True in matches:
            #     first_match_index = matches.index(True)
            #     name = known_face_names[first_match_index]

            # Or instead, use the known face with the smallest distance to the new face
            face_distances = face_recognition.face_distance(
                known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

            face_names.append(name)

    process_this_frame = not process_this_frame

    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35),
                      (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6),
                    font, 1.0, (255, 255, 255), 1)

    # Display the resulting image
    cv2.imshow('Video Feed: q to quit', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()

```

<hr style="solid">

### Eye Tracking


```python
import face_recognition
import cv2
import re
#import serial

# send serial data to arduino (communicate python --> arduino)
#arduino = serial.Serial(port = "COM3", baudrate = 9600, timeout = .1)

# Get a reference to webcam #0 (the default one)
video_capture = cv2.VideoCapture(0)

# Initialize some variables
face_locations = []
scaling = 0.25  # must be a float (X.Y)
# the factor to scale image back up by (to display correctly)
scaleUp = int(1 / scaling)


while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Resize frame of video to 1/4 size for faster face detection processing
    small_frame = cv2.resize(frame, (0, 0), fx=scaling, fy=scaling)

    # Find all the faces and face encodings in the current frame of video
    face_locations = face_recognition.face_locations(small_frame)
    face_landmarks_list = face_recognition.face_landmarks(small_frame)

    # leftEyeMiddleX = 0
    # leftEyeMiddleY = 0

    for face_landmarks in face_landmarks_list:
        # Find left eye location, store in string
        for facial_feature in face_landmarks.keys():
            if facial_feature == "left_eye":
                leftEye = face_landmarks[facial_feature]

                # coordinates for top left of eye, bottom right of eye
                topLeft = str(leftEye[1])
                bottomRight = str(leftEye[4])

                # seperate all digits from the list
                # find 0th and 1st value (X coord & Y coord respectively)
                # convert that string to an int:
                # topLeft coordinates
                topLeftX = int((re.findall(r'\d+', topLeft))[0])  # X
                topLeftY = int((re.findall(r'\d+', topLeft))[1])  # Y
                # bottomRight coordinates
                bottomRightX = int((re.findall(r'\d+', bottomRight))[0])  # X
                bottomRightY = int((re.findall(r'\d+', bottomRight))[1])  # Y

                # find the middle of the two points: (X1 + X2) / 2, (Y1 + Y2) / 2 = (middleX, middleY)
                # convert to int since division by 2 can give a value w/ .5
                leftEyeMiddleX = int((topLeftX + bottomRightX)/2)  # middle x
                leftEyeMiddleY = int((topLeftY + bottomRightY)/2)  # middle y

                # send coords over to the arduino as serial data
                #arduino.write(str.encode(leftEyeMiddleX))
                #arduino.write(str.encode(leftEyeMiddleY))
                # convert from int BACK to string and print the coordinates
                print(str(leftEyeMiddleX) + ", " + str(leftEyeMiddleY))

                for top, right, bottom, left in face_locations:
                    # Scale back up face locations since the frame we detected in was scaled to "scale" size
                    top *= scaleUp
                    right *= scaleUp
                    bottom *= scaleUp
                    left *= scaleUp

                    # Extract the region of the image that contains the face
                    face_image = frame[top:bottom, left:right]

                    face_image = cv2.rectangle(
                        frame, (left, top), (right, bottom), (0, 0, 255), 2)

                    # the circles need the coordinates scaled too
                    face_image = cv2.circle(
                        frame, (leftEyeMiddleX * scaleUp, leftEyeMiddleY * scaleUp), 3, (0, 0, 255), -1)
                    face_image = cv2.circle(
                        frame, (leftEyeMiddleX * scaleUp, leftEyeMiddleY * scaleUp), 1, (255, 255, 255), -1)
    # Display the resulting image
    cv2.imshow('Eye tracker (q = quit)', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()


# Find all facial features in all the faces in the image
face_landmarks_list = face_recognition.face_landmarks()

```

<hr style="solid">

### How It Works

This code utilizes one-shot deep learning facial recognition technology with an accuracy of 99.38% (Labled Faced in the Wild benchmark).

That's quite the mouthful! Before I explain what that all means, I have to explain how facial recognition works. 
1. The first step is data collection in which one or several images of an individual's face are collected and create the reference dataset. 
2. Then, you need to do feature extraction in order to capture important facial features. A common technique is the use of a deep neural network or handmade methods. 
3. After, you use a similarity metric which determines the similartiy between the features extracted from the reference image(s) and the new unseen face image. 
4. Using these steps, a machine can then recognize someone's face. It's like how humans do it by picking out certain features of a face and associating it with some identiy (like a person's name).

Here, we are using one-shot learning which is able to perform recognition with limited examples. In this case, we only give the computer a single image of a person. One-shot learning is designed to recognze someone's face using a single reference image or a very small batch of images without the need for extensive training data.

The advantages of one-shot learning include:
- Fewer training samples. Useful in scenarios with limited data or if collecting extensive data is impractical
- Can adapt quickly to new individuals without need for retraining entire model

However, the limitations of one-shot learning are:
- May struggle with some variability like facial expressions, lighting conditions, angles, etc
- One-shot learning only works if the reference image quality is good. If the quality is not good, it won't work as well
- Effective feature extraction and similarity metric techniques can be challenging and has to be fine-tuned

