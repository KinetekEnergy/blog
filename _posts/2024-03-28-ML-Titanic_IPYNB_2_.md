---
title: ML, Titanic
categories: ['CSP', 'Week 28']
tags: ['hacks']
---

## Part 1

This is the first part of the ML which is an adaptation to the titanic model. It’s a frontend to backend which has the “do you survive” titanic theme. It allows the user to input certain fields and it’ll predict your survival probability if you were on the titanic. 

![Titanic Original](images/titanic_original.png "Titanic Original")

This is the original form. But part 2 will explain our own features and the frontend/backend api.


## Part 2

This part uses another API and ML to integrate with the existing titanic model. It allows you to insert a photo of yourself which will be sent to the backend where a deep learning algorithm will predict your age and gender. This gets sent to the titanic API along with the other information you add yourself (name, class, etc) to predict your survival. In other words, I added a separate machine learning algorithm to predict some of the required titanic values (age and gender) and nicely integrated it with the existing project!


### Titanic Form

![Titanic ML](images/titanic_ML.png "Titanic ML")

Here, you can see an option to insert a photo. This replaces the previous age and gender fields since the ML model will predict this for you. Other information which can’t be predicted (name, class, etc.) will be filled in by the user.

Let’s try it out!

![Form](images/filled_form.png "Form")

Here’s a filled out form which uses information from my friend. I uploaded a photo of him:

![Person](images/person.jpg "Person")

Yes, this is a very badly lighted shot. However, I didn’t have any other photo on hand so this will have to do. Once I hit send, it’ll send all the information to the backend and will return with the survival probability.

![Loading Screen](images/loading_screen.png "Loading Screen")

Running the age and gender detection takes some time. To greatly improve user friendliness, I added this loading animation. While I can’t show a video, all it does is blur the background and show a spinner. It helps a lot because it lets the user know something is happening. In most cases, a user may click on the send button again which will take even more time and run the model again and again (as I ended up doing, thinking it’s not working). The animation tells you the backend is running.

![Survival Probability](images/survival_probability.png "Survival Probability")

Now, it’s returned the survival probability. Looks like he’s not going to fare so well! But what happened behind the scenes? Let’s check it out!


### Survival Calculation

![Survival Calculation](images/survival_calc.png "Survival Calculation")

When you click this button, it’ll run a function called `calculateSurvival()`. Let’s see the JS:

```js
function calculateSurvival() {
	extractData()
		.then((AIData) => {
			const passengerData = {
				name: document.getElementById("name").value,
				pclass: parseInt(getCheckedCheckboxValue("pclass")),
				sex: AIData[0],
				age: AIData[1],
				sibsp: parseInt(document.getElementById("sibsp").value),
				parch: parseInt(document.getElementById("parch").value),
				fare: parseFloat(document.getElementById("fare").value),
				embarked: getCheckedCheckboxValue("embarked"),
				alone:
					document.getElementById("alone").value === "true"
						? true
						: false,
			};

			const body = {
				passenger: passengerData,
			};

			const post_options = {
				method: "POST",
				cache: "no-cache",
				body: JSON.stringify(body),
				headers: {
					"Content-Type": "application/json",
					"Access-Control-Allow-Origin": "include",
				},
			};

			fetch(url, post_options)
				.then((response) => {
					if (!response.ok) {
						const errorMsg = response.status;
						console.log(errorMsg);
						return;
					}

					return response.json();
				})
				.then((data) => {
					const dataString = data;
					const h1 = document.getElementById("survival");
					h1.textContent = data[0];
				})
				.catch((err) => {
					console.error(err);
				});
		})
		.catch((err) => {
			console.error(err);
		});
}

```


#### Pre-Processing

Our code first runs `extractData()`. Let’s see what that is:

```js
// image deepface data extraction
function extractData() {
	document.getElementById("body").style.filter = "blur(20px)";
	document.getElementById("loader").style.display = "block"; // display loader

	return new Promise((resolve, reject) => {
		// photo
		var image = document.getElementById("photo");
		convertImageToBase64(image)
			.then((b64) => {
				console.log(b64);

				const post_options = {
					method: "POST",
					cache: "no-cache",
					body: JSON.stringify(b64),
					headers: {
						"Content-Type": "application/json",
						"Access-Control-Allow-Origin": "include",
					},
				};

				// different url for the imageRecognition api
				fetch(imageRecognition, post_options)
					.then((response) => {
						if (!response.ok) {
							const errorMsg = response.status;
							console.log(errorMsg);
							reject(
								new Error(
									`Failed to fetch image recognition data: ${errorMsg}`
								)
							);
							return;
						}

						return response.json();
					})
					.then((data) => {
						document.getElementById("loader").style.display =
							"none"; // hide loader
						document.getElementById("body").style.filter =
							"blur(0px)";
						resolve(data); // Resolve with the processed data
					})
					.catch((err) => {
						reject(err);
					});
			})
			.catch((err) => {
				document.getElementById("loader").style.display = "none"; // hide when error happens
				document.getElementById("body").style.filter = "blur(0px)";
				reject(err);
			});
	});
}

```

Our code first runs the loading animation which blurs the background and starts the spinner. Next, it’ll get the photo and run `convertImageToBase64()`. I won’t show that since it’ll take too long. But all it does is take the image, convert it to a base 64 string, and return it. This makes it easy to send to the backend. Once it’s gotten the string, it’ll make a post request to the recognition API. It returns the data and turns off the loading animation. So let’s see what’s in the recognition API.

```python
# image parsing in preparation
b64_string = base64_encoded  # ["base64_encoded"]  # remove from dictionary

if b64_string.startswith("data:image"):  # if headers --> remove
    b64_string = b64_string.split(",", 1)[1]

image_data = base64.b64decode(b64_string)  # decoding

image = Image.open(io.BytesIO(image_data))  # get the image

image_np = np.array(image)  # convert to np array

# analysis
attributes = ["age", "gender"]  # which attributes
information = dp.analyze(image_np, attributes)  # analyze
```

This is the preprocessing processing code. Originally, the code was sent as a dictionary because that’s how Postman was sending it. Now, it doesn’t do this any more but I didn’t want to change all the variable names (and just in-case I do more Postman testing), so I left it as is. The first thing is to parse the string. Sometimes, base64 strings have headers. If they have this, we need to remove them. The next step is to decode the string and extract the bytes to convert to an image file. This gets stored in the cache and not locally to not flood the backend with a lot of files. The image is converted to a numpy array which is what we need for the ML. Next is the main part. We send our image to Deepface which is an amalgamation of Tensorflow, GhostFaceNet, Dlib, and more. This will analyze the image and only look for the attributes specified: gender and age. We don’t need anything else.


#### The Model Behind the Scenes

```python
def __init__(self):
        self.model = load_model()
        self.model_name = "Age"

    def predict(self, img: np.ndarray) -> np.float64:
        age_predictions = self.model.predict(img, verbose=0)[0, :]
        return find_apparent_age(age_predictions)
```

This code will load the model for the age and run the predict function with the numpy array that we gave. It will return the predictions it makes. The next code is the load model function.


```python
def load_model(
    url="https://github.com/serengil/deepface_models/releases/download/v1.0/age_model_weights.h5",
) -> Model:
    """
    Construct age model, download its weights and load
    Returns:
        model (Model)
    """

    model = VGGFace.base_model()

    # --------------------------

    classes = 101
    base_model_output = Sequential()
    base_model_output = Convolution2D(classes, (1, 1), name="predictions")(model.layers[-4].output)
    base_model_output = Flatten()(base_model_output)
    base_model_output = Activation("softmax")(base_model_output)

    # --------------------------

    age_model = Model(inputs=model.input, outputs=base_model_output)

    # --------------------------

    # load weights

    home = folder_utils.get_deepface_home()

    if os.path.isfile(home + "/.deepface/weights/age_model_weights.h5") != True:
        logger.info("age_model_weights.h5 will be downloaded...")

        output = home + "/.deepface/weights/age_model_weights.h5"
        gdown.download(url, output, quiet=False)

    age_model.load_weights(home + "/.deepface/weights/age_model_weights.h5")

    return age_model

    # --------------------------
```

This will load a model which lets us predict the age. We construct the model by using the VGGFace base model. This is a pretrained model that we will build up off of. First, we extract the fourth-to-last layer of the model because this contains our age prediction data. We start adding layers to this as we build up our model. We create more convolutional layers and flatten each one. It’s like stacking up pancakes! Then, we use the softmax to get probability distributions. Our customized model is returned and is later called by the age function for prediction. This also happens for our gender: use an existing model, add our own data to train it to make it better, and return the model for the prediction.


#### Post-Processing and Returning Information

```python
# data extraction
data = information[0]  # get the first element
age = data["age"]  # age extraction

bothGenders = data["gender"]  # get both gender confidence rates
woman = bothGenders["Woman"]  # woman confidence
man = bothGenders["Man"]  # man confidence

# based on the probabilities, find which is larger and return that
gender = None
if woman > man:
    gender = "Female"
elif woman < man:
    gender = "Male"

# the order is very important (must be gender THEN age)
returnData = [gender, age]  # create a list and send it

return returnData  # return
```

This is the final step! We first extract the data and separate the age and gender values. Age is easy: we return a number. Gender is a little more complex since we return the probabilities for each gender. To parse this, we just compare the values and see which probability is higher. Depending on which, we return the corresponding gender value. The final information is made into a list and returned; this makes it all nice and packaged.


#### Titanic Prediction

Now onto the final step. We’ve extracted the data we need. Next is titanic. This is pretty straight-forward as we’ve already done this!

```js
function calculateSurvival() {
    extractData()
        .then((AIData) => {
            const passengerData = {
                name: document.getElementById("name").value,
                pclass: parseInt(getCheckedCheckboxValue("pclass")),
                sex: AIData[0],
                age: AIData[1],
                sibsp: parseInt(document.getElementById("sibsp").value),
                parch: parseInt(document.getElementById("parch").value),
                fare: parseFloat(document.getElementById("fare").value),
                embarked: getCheckedCheckboxValue("embarked"),
                alone:
                    document.getElementById("alone").value === "true"
                        ? true
                        : false,
            };

            const body = {
                passenger: passengerData,
            };

            const post_options = {
                method: "POST",
                cache: "no-cache",
                body: JSON.stringify(body),
                headers: {
                    "Content-Type": "application/json",
                    "Access-Control-Allow-Origin": "include",
                },
            };

            fetch(url, post_options)
                .then((response) => {
                    if (!response.ok) {
                        const errorMsg = response.status;
                        console.log(errorMsg);
                        return;
                    }

                    return response.json();
                })
                .then((data) => {
                    const dataString = data;
                    const h1 = document.getElementById("survival");
                    h1.textContent = data[0];
                })
                .catch((err) => {
                    console.error(err);
                });
        })
        .catch((err) => {
            console.error(err);
        });
}
```

We’ve gotten all our user filled data and the data returned from the model. This is wrapped in a passenger tag and sent to the titanic model for prediction. Our return message is printed out. 


### Network View: Requests and Returns

Now that you know how the code works, the final step is showing the post requests and returns. The following images show the post request to the recognition api with the image. Next is the post request to the titanic api with the payload: gender and age have been created by our recognition model. It returns the survival probability and prints it out.

![Recognition Request](images/recognition_request.png "Recognition Request")

![Titanic Request](images/titanic_request.png "Titanic Request")

![Titanic Payload](images/titanic_payload.png "Titanic Payload")

