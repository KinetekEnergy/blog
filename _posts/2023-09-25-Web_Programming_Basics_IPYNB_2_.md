---
toc: True
comments: False
layout: post
title: Web Programming Basics
tags: ['hacks']
categories: ['CSP', 'Week 6']
---

```python
%%html

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page</title>
</head>

<body>
    <div>
        <img src="W2W.png" alt="Window to the World Image">
        <div>
            <p>
                This image depicts a pier in the ocean.
                The image was taken using a long exposure and high f stop.
                The weather in the image is cloudy and the waves are calm.
                The pier is made up of concrete.
            </p>
            <a href="https://www.pixelpotpourri.com/Galleries/Oceans/i-cNg27wP">
                <button>
                    Link to image source
                </button>
            </a>
        </div>
    </div>
</body>

</html>
```

<hr style="solid">

### Datatypes


```python
%%js

// Create an object representing myself
var obj = {
    name: "Aashray",
    age: 15,
    currentClasses: ["Humanities, CSP, World, Math, Spanish"],
    interests: "Drinking water",
    favoriteStateOfMaterForWater: "Liquid",
    favoriteWaterFlavor: "Water"

};

// Print the entire object
console.log(obj);

// Manipulate the arrays within the object
console.log("Object: manipulating data");
obj.currentClasses[0] = "Water Drinking"
console.log(obj);
console.log(obj.currentClasses[0]);

// Perform mathematical operations on fields in the object
const ageIn5 = obj.age + 5;
console.log(`\nIn five years, I will be ${ageIn5} years old.`);

// Use typeof to determine the types of fields
console.log(`\nData Types:`);
console.log(`Name is of type: ${typeof obj.name}`);
console.log(`Age is of type: ${typeof obj.age}`);
console.log(`Current Classes is of type: ${typeof obj.currentClasses}`);
```

<hr style="solid">

### DOM


```python
%%html

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page</title>
</head>

<body>
    <div>
        <img src="W2W.png" alt="Window to the World Image">
        <div>

            <!-- switch status -->
            <p id="status">Not switched!</p>

            <!-- dummy text -->
            <p>
                This image depicts a pier in the ocean.
                The image was taken using a long exposure and high f stop.
                The weather in the image is cloudy and the waves are calm.
                The pier is made up of concrete.
            </p>

            <!-- image source button -->
            <a href="https://www.pixelpotpourri.com/Galleries/Oceans/i-cNg27wP" id="imageButton">
                <button>Link to image source</button>
            </a>

            <!-- NOT image source button (google) -->
            <a href="https://www.google.com/" id="googleButton">
                <button>Not the image source</button>
            </a>

            <!-- switch button -->
            <button id="switchButton">One Two Switch-a-roo</button>
        </div>
    </div>
</body>

<script>

    function switchLink() { // switch function
        var imageButton = document.getElementById("imageButton"); // get button
        var googleButton = document.getElementById("googleButton"); // get button
        var status = document.getElementById("status"); // get status p tag

        var tempLink = imageButton.getAttribute("href"); // store link of image button in temp var

        imageButton.setAttribute("href", googleButton.getAttribute("href")); // set image button to google button link 
        googleButton.setAttribute("href", tempLink); // set google button to temp link (image button link)

        status.textContent = "Switched!"; // change p tag status
    }

    var switchButton = document.getElementById("switchButton"); // get switch button
    switchButton.addEventListener("click", switchLink); // event listener for click; call funcion
</script>

</html>
```

<hr style="solid">

### JS


```python
%% js

// vars
var a = 1;
var b = 2;

// comparison logic code + log output
if (a > b) {
    console.log("a > b");
}
else if (a < b) {
    console.log("a < b");
}
else {
    console.log("a == b");
}
```

<hr style="solid">

### Debug I


```python
%% js

var alphabet = "abcdefghijklmnopqrstuvwxyz";
var alphabetList = [];

for (var i = 0; i < 10; i++) {
    alphabetList.push(i);
}

console.log(alphabetList);

```


```python
%%js

var alphabet = "abcdefghijklmnopqrstuvwxyz";
var alphabetList = [];

for (var i = 0; i < alphabet.length; i++) {
    alphabetList.push(alphabet[i]);
}

console.log(alphabetList);
```

Code was pushing number to the alphabet list. Changed so that it fetches from alphabet array and pushes that instead.

<hr style="solid">

### Debug II


```python
%% js

var alphabet = "abcdefghijklmnopqrstuvwxyz";
var alphabetList = [];

for (var i = 0; i < alphabet.length; i++) {
    alphabetList.push(alphabet[i]);
}

console.log(alphabetList);

let letterNumber = 5

for (var i = 0; i < alphabetList; i++) {
    if (i === letterNumber) {
        console.log(letterNumber + " is letter number 1 in the alphabet")
    }
}

// Should output:
// "e" is letter number 5 in the alphabet
```


```python
%%js

var alphabet = "abcdefghijklmnopqrstuvwxyz";
var alphabetList = [];

for (var i = 0; i < alphabet.length; i++) {
    alphabetList.push(alphabet[i]);
}

console.log(alphabetList);

let letterNumber = 5

for (var j = 0; j < letterNumber; j++) {
    if (alphabetList[j] === "e") {
        console.log(alphabetList[j] + " is letter number 5 in the alphabet")
    }
}
```

1. For loop now iterates letterNumber times
2. For loop uses j instead of i
3. For loop checks current letter for match with e
4. Log now prints the letter and the correct number

<hr style="solid">

### Debug III


```python
%%js

let evens = [];
let i = 0;

while (i <= 10) {
    evens.push(i);
    i += 2;
}

console.log(evens);
```


```python
%%js

let evens = [];
let i = 1;

while (i <= 10) {
    evens.push(i);
    i += 2;
}

console.log(evens);
```

Changed i to 1 to offset list and print odds.
