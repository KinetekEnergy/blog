---
toc: True
comments: True
layout: post
title: Student Lesson Python Libraries
description: To teach the class how to use public Python libraries around the internet
type: hacks
courses: {'csp': {'week': 10}}
---

### What is a Library?
Essentially a list of pre-written code that you can use to streamline and clean up your program.

Libraries can help simplify complex programs

APIS are specifications for how the procedures in a library behave, and how they can be used 

Documentations for an API/library is necessary in understanding the behaviors provided by the API/library and how to use them

Libraries that we will go over: Requests, Pillow, Pandas, Numpy, Scikit-Learn, TensorFlow, matplotlib.


### Required Installations
Please run the following commands in your vscode terminal in order to continue the lesson
- pip install numpy && pip install matplotlib && pip install scikit-learn && pip install pillow && pip install pandas && pip install tensorflow && pip install requests

### Images using requests and pillow libraries
'Requests' is focused on handling HTTP requests and web data while 'Pillow' is designed for data manipulation and analysis
It's common to see them used together in data-related assignments where data is fetched by HTTP requests using Requests and then processed and analyzed with Pandas.

Here's an example:


```python
import requests
from PIL import Image
from io import BytesIO

# Step 1: Download an image using Requests
image_url = "https://example.com/path/to/your/image.jpg"  # Replace with the actual URL of the image you want to download
response = requests.get(image_url)

if response.status_code == 200:
    # Step 2: Process the downloaded image using Pillow
    image_data = BytesIO(response.content)  # Create an in-memory binary stream from the response content
    img = Image.open(image_data)  # Open the image using Pillow

    # Perform image processing tasks here, like resizing or applying filters
    img = img.resize((x, y))  # Resize the image and replace x,y with desired amounts

    # Step 3: Save the processed image using Pillow
    img.save("processed_image.jpg")  # Save the processed image to a file

    print("Image downloaded, processed, and saved.")
else:
    print(f"Failed to download image. Status code: {response.status_code}")

```

In this code, we use the Requests library to download an image from a URL and then if the download is successful the HTTP status code 200 will pop up, and from there we create an in-memory binary stream (BytesIO) from the response content. We then use the Pillow library to open the image, make any necessary changes, and save the processed image to a file.

Here's a step by step tutorial on how we wrote this code: 
1. We started by importing the necessary libraries, which were Requests, Pillow, and io.
2. Download the Image
3. Use the Requests library to send an HTTP GET request to the URL to download the image.
Check the response status code to make sure the download goes through(status code 200).
4. If the download is successful, create an in-memory binary stream (BytesIO) from the response content.
Process the Image:
5. Utilize the Pillow library to open the image from the binary stream.
Change photo to desired preference(ie: size)
Save the Processed Image:
6. Save the processed image to a file using Pillow. Choose a filename and file format for the saved image.




### Hack 1

Write a Python code that accomplishes the following tasks:

Downloads an image from a specified URL using the Requests library.
Processes the downloaded image (like resizing) using the Pillow library.
Save the processed image to a file.



```python
import requests
from PIL import Image
from io import BytesIO

response = requests.get("https://images.ctfassets.net/hrltx12pl8hq/3Mz6t2p2yHYqZcIM0ic9E2/3b7037fe8871187415500fb9202608f7/Man-Stock-Photos.jpg") # download image

if response.status_code == 200: # response 200 = download success
    image_data = BytesIO(response.content)  
    
    img = Image.open(image_data)  # Open the image using Pillow

    img = img.resize((100, 100))  # resize to 100x100

    img.save("processed_image.jpg")  # Save the processed image to a file

    print("Image downloaded, processed, and saved.")
else:
    print(f"Failed to download image. Status code: {response.status_code}")

```

    Image downloaded, processed, and saved.


### Math Operations With Python Libraries
Numpy(Numerical Python) is used for numerical and scientific computing. It provides tools for handling large sets of numbers, such as data tables and arrays. Numpy makes it easier and more efficient to do mathematical tasks. 

The Matplotlib library lets you create a visual representation of your data (graphs, charts, and etc.)

### Example Sine Graph
Uses numpy and matplotlib libaries


```python
import numpy as np
import matplotlib.pyplot as plot

# Generate sample data with NumPy
x = np.linspace(0, 2 * np.pi, 100) 
# Create an array of values from 0 to 2*pi
# 100 is included to have 100 points distributed between 0 and 2π to make graph smoother
y = np.sin(x)
# Compute the sine of each value

# Create a simple line plot using Matplotlib
plot.plot(x, y, label='Sine Function', color='blue', linestyle='-')  # Create the plot
plot.title('Sine Function')  # Set the title
plot.xlabel('x')  # Label for the x-axis
plot.ylabel('sin(x)')  # Label for the y-axis
plot.grid(True)  # Display a grid
plot.legend()  # Show the legend
plot.show()  # Display the plot

```


    
![png](output_10_0.png)
    


### Hack 2
Using the data from the numpy library, create a visual graph using different matplotlib functions.


```python
import numpy as np
import matplotlib.pyplot as plot

# Generate data for two lines
x = np.linspace(0, 10, 50)  # Create an array of values from 0 to 10
y1 = 2 * x + 1  # Set of data poits

# Create and display a plot using Matplotlib
# y = np.cos(y)

# your code here
plot.plot(x, y1, label='Linear Function', color='blue', linestyle='-')  # Create the plot
plot.title('Linear Function')  # Set the title
plot.xlabel('x')  # Label for the x-axis
plot.ylabel('y')  # Label for the y-axis
plot.grid(True)  # Display a grid
plot.legend()  # Show the legend
plot.show()  # Display the plot
```


    
![png](output_12_0.png)
    


## Pip install tensorflow scikit-learn

Tensor Flow is used in deep learning and neural networks, while scikit-learn is used for typical machine learning tasks. When used together, they can tackle machine learning projects. In the code below, Tensor Flow is used for model creation and training. Scikit-learn is used for data-processing and model evaluation.


```python
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler
from tensorflow import keras
from tensorflow.keras import layers
# Generate synthetic data
np.random.seed(0)
X = np.random.rand(100, 1)  # Feature
y = 2 * X + 1 + 0.1 * np.random.randn(100, 1)  # Target variable with noise
# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Standardize the features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
# Create a simple linear regression model using TensorFlow and Keras
model = keras.Sequential([
    layers.Input(shape=(1,)),
    layers.Dense(1)
])
# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error')
# Train the model
model.fit(X_train, y_train, epochs=100, batch_size=32, verbose=2)
# Make predictions on the test set
y_pred = model.predict(X_test)
# Calculate the Mean Squared Error on the test set
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse:.4f}")
```

    2023-10-26 10:33:16.990401: I tensorflow/core/util/port.cc:111] oneDNN custom operations are on. You may see slightly different numerical results due to floating-point round-off errors from different computation orders. To turn them off, set the environment variable `TF_ENABLE_ONEDNN_OPTS=0`.
    2023-10-26 10:33:16.994237: I tensorflow/tsl/cuda/cudart_stub.cc:28] Could not find cuda drivers on your machine, GPU will not be used.
    2023-10-26 10:33:17.043310: E tensorflow/compiler/xla/stream_executor/cuda/cuda_dnn.cc:9342] Unable to register cuDNN factory: Attempting to register factory for plugin cuDNN when one has already been registered
    2023-10-26 10:33:17.043364: E tensorflow/compiler/xla/stream_executor/cuda/cuda_fft.cc:609] Unable to register cuFFT factory: Attempting to register factory for plugin cuFFT when one has already been registered
    2023-10-26 10:33:17.043418: E tensorflow/compiler/xla/stream_executor/cuda/cuda_blas.cc:1518] Unable to register cuBLAS factory: Attempting to register factory for plugin cuBLAS when one has already been registered
    2023-10-26 10:33:17.056111: I tensorflow/tsl/cuda/cudart_stub.cc:28] Could not find cuda drivers on your machine, GPU will not be used.
    2023-10-26 10:33:17.058218: I tensorflow/core/platform/cpu_feature_guard.cc:182] This TensorFlow binary is optimized to use available CPU instructions in performance-critical operations.
    To enable the following instructions: AVX2 AVX_VNNI FMA, in other operations, rebuild TensorFlow with the appropriate compiler flags.
    2023-10-26 10:33:18.643305: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Could not find TensorRT
    /usr/lib/python3/dist-packages/scipy/__init__.py:146: UserWarning: A NumPy version >=1.17.3 and <1.25.0 is required for this version of SciPy (detected version 1.25.2
      warnings.warn(f"A NumPy version >={np_minversion} and <{np_maxversion}"


    Epoch 1/100
    3/3 - 1s - loss: 3.7623 - 550ms/epoch - 183ms/step
    Epoch 2/100
    3/3 - 0s - loss: 3.7505 - 16ms/epoch - 5ms/step
    Epoch 3/100
    3/3 - 0s - loss: 3.7388 - 15ms/epoch - 5ms/step
    Epoch 4/100
    3/3 - 0s - loss: 3.7272 - 18ms/epoch - 6ms/step
    Epoch 5/100
    3/3 - 0s - loss: 3.7155 - 18ms/epoch - 6ms/step
    Epoch 6/100
    3/3 - 0s - loss: 3.7039 - 16ms/epoch - 5ms/step
    Epoch 7/100
    3/3 - 0s - loss: 3.6923 - 16ms/epoch - 5ms/step
    Epoch 8/100
    3/3 - 0s - loss: 3.6807 - 22ms/epoch - 7ms/step
    Epoch 9/100
    3/3 - 0s - loss: 3.6692 - 16ms/epoch - 5ms/step
    Epoch 10/100
    3/3 - 0s - loss: 3.6577 - 24ms/epoch - 8ms/step
    Epoch 11/100
    3/3 - 0s - loss: 3.6461 - 19ms/epoch - 6ms/step
    Epoch 12/100
    3/3 - 0s - loss: 3.6348 - 22ms/epoch - 7ms/step
    Epoch 13/100
    3/3 - 0s - loss: 3.6232 - 13ms/epoch - 4ms/step
    Epoch 14/100
    3/3 - 0s - loss: 3.6119 - 13ms/epoch - 4ms/step
    Epoch 15/100
    3/3 - 0s - loss: 3.6005 - 18ms/epoch - 6ms/step
    Epoch 16/100
    3/3 - 0s - loss: 3.5891 - 16ms/epoch - 5ms/step
    Epoch 17/100
    3/3 - 0s - loss: 3.5779 - 15ms/epoch - 5ms/step
    Epoch 18/100
    3/3 - 0s - loss: 3.5666 - 15ms/epoch - 5ms/step
    Epoch 19/100
    3/3 - 0s - loss: 3.5553 - 17ms/epoch - 6ms/step
    Epoch 20/100
    3/3 - 0s - loss: 3.5442 - 13ms/epoch - 4ms/step
    Epoch 21/100
    3/3 - 0s - loss: 3.5328 - 14ms/epoch - 5ms/step
    Epoch 22/100
    3/3 - 0s - loss: 3.5215 - 18ms/epoch - 6ms/step
    Epoch 23/100
    3/3 - 0s - loss: 3.5104 - 14ms/epoch - 5ms/step
    Epoch 24/100
    3/3 - 0s - loss: 3.4991 - 13ms/epoch - 4ms/step
    Epoch 25/100
    3/3 - 0s - loss: 3.4882 - 14ms/epoch - 5ms/step
    Epoch 26/100
    3/3 - 0s - loss: 3.4769 - 12ms/epoch - 4ms/step
    Epoch 27/100
    3/3 - 0s - loss: 3.4658 - 13ms/epoch - 4ms/step
    Epoch 28/100
    3/3 - 0s - loss: 3.4547 - 12ms/epoch - 4ms/step
    Epoch 29/100
    3/3 - 0s - loss: 3.4438 - 15ms/epoch - 5ms/step
    Epoch 30/100
    3/3 - 0s - loss: 3.4327 - 13ms/epoch - 4ms/step
    Epoch 31/100
    3/3 - 0s - loss: 3.4219 - 16ms/epoch - 5ms/step
    Epoch 32/100
    3/3 - 0s - loss: 3.4107 - 14ms/epoch - 5ms/step
    Epoch 33/100
    3/3 - 0s - loss: 3.3998 - 12ms/epoch - 4ms/step
    Epoch 34/100
    3/3 - 0s - loss: 3.3891 - 13ms/epoch - 4ms/step
    Epoch 35/100
    3/3 - 0s - loss: 3.3782 - 15ms/epoch - 5ms/step
    Epoch 36/100
    3/3 - 0s - loss: 3.3674 - 15ms/epoch - 5ms/step
    Epoch 37/100
    3/3 - 0s - loss: 3.3565 - 21ms/epoch - 7ms/step
    Epoch 38/100
    3/3 - 0s - loss: 3.3459 - 11ms/epoch - 4ms/step
    Epoch 39/100
    3/3 - 0s - loss: 3.3351 - 20ms/epoch - 7ms/step
    Epoch 40/100
    3/3 - 0s - loss: 3.3244 - 17ms/epoch - 6ms/step
    Epoch 41/100
    3/3 - 0s - loss: 3.3138 - 16ms/epoch - 5ms/step
    Epoch 42/100
    3/3 - 0s - loss: 3.3032 - 16ms/epoch - 5ms/step
    Epoch 43/100
    3/3 - 0s - loss: 3.2926 - 17ms/epoch - 6ms/step
    Epoch 44/100
    3/3 - 0s - loss: 3.2820 - 17ms/epoch - 6ms/step
    Epoch 45/100
    3/3 - 0s - loss: 3.2714 - 18ms/epoch - 6ms/step
    Epoch 46/100
    3/3 - 0s - loss: 3.2609 - 17ms/epoch - 6ms/step
    Epoch 47/100
    3/3 - 0s - loss: 3.2503 - 14ms/epoch - 5ms/step
    Epoch 48/100
    3/3 - 0s - loss: 3.2399 - 17ms/epoch - 6ms/step
    Epoch 49/100
    3/3 - 0s - loss: 3.2294 - 18ms/epoch - 6ms/step
    Epoch 50/100
    3/3 - 0s - loss: 3.2191 - 16ms/epoch - 5ms/step
    Epoch 51/100
    3/3 - 0s - loss: 3.2086 - 16ms/epoch - 5ms/step
    Epoch 52/100
    3/3 - 0s - loss: 3.1983 - 13ms/epoch - 4ms/step
    Epoch 53/100
    3/3 - 0s - loss: 3.1879 - 14ms/epoch - 5ms/step
    Epoch 54/100
    3/3 - 0s - loss: 3.1776 - 16ms/epoch - 5ms/step
    Epoch 55/100
    3/3 - 0s - loss: 3.1674 - 16ms/epoch - 5ms/step
    Epoch 56/100
    3/3 - 0s - loss: 3.1570 - 13ms/epoch - 4ms/step
    Epoch 57/100
    3/3 - 0s - loss: 3.1468 - 13ms/epoch - 4ms/step
    Epoch 58/100
    3/3 - 0s - loss: 3.1366 - 11ms/epoch - 4ms/step
    Epoch 59/100
    3/3 - 0s - loss: 3.1265 - 13ms/epoch - 4ms/step
    Epoch 60/100
    3/3 - 0s - loss: 3.1161 - 15ms/epoch - 5ms/step
    Epoch 61/100
    3/3 - 0s - loss: 3.1060 - 12ms/epoch - 4ms/step
    Epoch 62/100
    3/3 - 0s - loss: 3.0959 - 13ms/epoch - 4ms/step
    Epoch 63/100
    3/3 - 0s - loss: 3.0858 - 12ms/epoch - 4ms/step
    Epoch 64/100
    3/3 - 0s - loss: 3.0757 - 12ms/epoch - 4ms/step
    Epoch 65/100
    3/3 - 0s - loss: 3.0657 - 15ms/epoch - 5ms/step
    Epoch 66/100
    3/3 - 0s - loss: 3.0556 - 13ms/epoch - 4ms/step
    Epoch 67/100
    3/3 - 0s - loss: 3.0456 - 13ms/epoch - 4ms/step
    Epoch 68/100
    3/3 - 0s - loss: 3.0356 - 13ms/epoch - 4ms/step
    Epoch 69/100
    3/3 - 0s - loss: 3.0256 - 14ms/epoch - 5ms/step
    Epoch 70/100
    3/3 - 0s - loss: 3.0156 - 13ms/epoch - 4ms/step
    Epoch 71/100
    3/3 - 0s - loss: 3.0058 - 10ms/epoch - 3ms/step
    Epoch 72/100
    3/3 - 0s - loss: 2.9959 - 13ms/epoch - 4ms/step
    Epoch 73/100
    3/3 - 0s - loss: 2.9861 - 14ms/epoch - 5ms/step
    Epoch 74/100
    3/3 - 0s - loss: 2.9761 - 12ms/epoch - 4ms/step
    Epoch 75/100
    3/3 - 0s - loss: 2.9663 - 14ms/epoch - 5ms/step
    Epoch 76/100
    3/3 - 0s - loss: 2.9565 - 15ms/epoch - 5ms/step
    Epoch 77/100
    3/3 - 0s - loss: 2.9468 - 12ms/epoch - 4ms/step
    Epoch 78/100
    3/3 - 0s - loss: 2.9370 - 17ms/epoch - 6ms/step
    Epoch 79/100
    3/3 - 0s - loss: 2.9273 - 13ms/epoch - 4ms/step
    Epoch 80/100
    3/3 - 0s - loss: 2.9178 - 12ms/epoch - 4ms/step
    Epoch 81/100
    3/3 - 0s - loss: 2.9080 - 14ms/epoch - 5ms/step
    Epoch 82/100
    3/3 - 0s - loss: 2.8984 - 13ms/epoch - 4ms/step
    Epoch 83/100
    3/3 - 0s - loss: 2.8887 - 16ms/epoch - 5ms/step
    Epoch 84/100
    3/3 - 0s - loss: 2.8793 - 14ms/epoch - 5ms/step
    Epoch 85/100
    3/3 - 0s - loss: 2.8696 - 16ms/epoch - 5ms/step
    Epoch 86/100
    3/3 - 0s - loss: 2.8601 - 13ms/epoch - 4ms/step
    Epoch 87/100
    3/3 - 0s - loss: 2.8507 - 13ms/epoch - 4ms/step
    Epoch 88/100
    3/3 - 0s - loss: 2.8411 - 14ms/epoch - 5ms/step
    Epoch 89/100
    3/3 - 0s - loss: 2.8316 - 14ms/epoch - 5ms/step
    Epoch 90/100
    3/3 - 0s - loss: 2.8222 - 15ms/epoch - 5ms/step
    Epoch 91/100
    3/3 - 0s - loss: 2.8128 - 13ms/epoch - 4ms/step
    Epoch 92/100
    3/3 - 0s - loss: 2.8035 - 11ms/epoch - 4ms/step
    Epoch 93/100
    3/3 - 0s - loss: 2.7941 - 14ms/epoch - 5ms/step
    Epoch 94/100
    3/3 - 0s - loss: 2.7847 - 12ms/epoch - 4ms/step
    Epoch 95/100
    3/3 - 0s - loss: 2.7754 - 13ms/epoch - 4ms/step
    Epoch 96/100
    3/3 - 0s - loss: 2.7661 - 16ms/epoch - 5ms/step
    Epoch 97/100
    3/3 - 0s - loss: 2.7568 - 13ms/epoch - 4ms/step
    Epoch 98/100
    3/3 - 0s - loss: 2.7475 - 12ms/epoch - 4ms/step
    Epoch 99/100
    3/3 - 0s - loss: 2.7384 - 15ms/epoch - 5ms/step
    Epoch 100/100
    3/3 - 0s - loss: 2.7292 - 12ms/epoch - 4ms/step
    1/1 [==============================] - 0s 83ms/step
    Mean Squared Error: 2.6910


A decrease in loss and time metrics (ms/epoch and ms/step) shows the efficiency increases as the training epochs increases

## Hack
fill in the missing code to match the custom data set


```python
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler
from tensorflow import keras
from tensorflow.keras import layers
# Generate a custom dataset (replace this with your data loading code)
# Synthetic data: House prices based on number of bedrooms and square footage
np.random.seed(0)
num_samples = 100
bedrooms = np.random.randint(1, 5, num_samples)
square_footage = np.random.randint(1000, 2500, num_samples)
house_prices = 100000 + 50000 * bedrooms + 100 * square_footage + 10000 * np.random.randn(num_samples)
# Combine features (bedrooms and square footage) into one array
X = np.column_stack((bedrooms, square_footage))
y = house_prices.reshape(-1, 1)
# Split the data into training and testing sets

# Standardize the features

# Create a regression model using TensorFlow and Keras

    # Input shape adjusted to the number of features
     # Output layer for regression

# Compile the model for regression
  # Using MSE as the loss function
# Train the model

# Make predictions on the test set

# Calculate the Mean Squared Error on the test set

```

## HOMEWORK 1

Create a GPA calculator using Pandas and Matplot libraries and make:
1) A dataframe
2) A specified dictionary
3) and a print function that outputs the final GPA

Extra points can be earned with creativity.


```python
# your code here
```

## HOMEWORK 2

Import and use the "random" library to generate 50 different points from the range 0-100, then display the randomized data using a scatter plot.

Extra points can be earned with creativity.


```python
# your code here
```
