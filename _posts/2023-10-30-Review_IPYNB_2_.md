---
toc: True
comments: False
layout: post
title: Independent Review
type: tangibles
courses: {'compsci': {'week': 10}}
---

### Issues

All issues can be seen on the project board in github (I think that the week number may be wrong but the issues are still there)

### Week 8

Week 8! So far, a lot of changes have been made on the front end design. We’ve fixed some spacing issues and some styling. But backend… oh God backend. Data isn’t working and what the HECK is error 502. So it took a while to fix these issues because the backend server had some issues and we couldn’t grab the data well. Luckily, all of us worked together to get things working. We also started drafting the cookie maker (more on that later).


```python
const apiUrl = 'https://bytebufoons.stu.nighthawkcodingsociety.com/api/Cookie/';

// we first make an HTTP get request to the api
fetch(apiUrl)
    .then(response => response.json()) // the api returns JSON, so we parse it 
    .then(data => {
        // the data is organized into a dictionary to call from it
        const organizedData = {
            Cookie_api: {
                url_prefix: '/api/Cookie',
                CookieAPI: {
                    get: {
                        description: 'Retrieve all cookies from the database',
                        url: '/api/Cookie',
                        method: 'GET',
                        data: data,
                    },
                },
            },
            CookieListAPI: {
                CookieListAPI: {
                    get: {
                        description: 'Retrieve all cookies from the database',
                        url: '/api/Cookie',
                        method: 'GET',
                        data: data,
                    },
                },
            },
        };

        // the dictionary we can call from
        Data = organizedData.Cookie_api.CookieAPI.get.data; 

        const catalogGrid = document.getElementById("catalog-grid"); // get the catalog grid

        Data.forEach((item) => { // for each item in the dictionary (each cookie pulled from backend)
            // first create the card

            // the beauty of this system is that it is completely modular
            // it's like legos, where everything snaps into place
            // just like a lego set, we only use the parts we need with no extras
            const card = document.createElement("div")
            card.className = "card";

            // create the image
            const image = document.createElement("img");
            image.src = item.image;
            image.alt = "cookie";

            // create the card content
            const cardContent = document.createElement("div")
            cardContent.className = "card-content";


            // the cookie title is the cookie's name and its price
            const title = document.createElement("p");
            title.className = "title";
            title.textContent = `${item.Cookie_name} - $${item.price}`


            // new line
            const whitespace1 = document.createElement("p");
            whitespace1.className = "title";
            whitespace1.textContent = ``

            // this is the add to cart button
            const chip = document.createElement("a");
            chip.className = "chip";
            chip.textContent = "Add to Cart";
            chip.addEventListener("click", () => {
                // the click code
            });

            // new line
            const whitespace2 = document.createElement("p");
            whitespace2.className = "title";
            whitespace2.textContent = ``


            // put it all together
            cardContent.appendChild(title);
            cardContent.appendChild(whitespace1)
            cardContent.appendChild(chip);
            cardContent.appendChild(whitespace2)

            card.appendChild(image);
            card.appendChild(cardContent);

            catalogGrid.appendChild(card);

        })
    })
    .catch(error => {
        console.error('Error fetching data:', error);
    });

document.getElementById("addCookieButton").addEventListener("click", function () {
    // Define the data to be sent to the API
    const cookieData = {
        Cookie_name: "Chocolate Chip",
        image: "chocolate_chip.jpg",
        stock: 100,
        price: 1.99
    };

    // Send a POST request to the API
    fetch(apiUrl, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(cookieData)
    })
        .then(response => response.json())
        .then(data => {
            // Handle the response data here, e.g., display a success message
            console.log("Cookie added:", data);
            alert("Cookie added successfully!");
        })
        .catch(error => {
            // Handle any errors here, e.g., display an error message
            console.error("Error:", error);
            alert("Error adding the cookie.");
        });
});
```

### Week 9

Week 9. Once again, issues with the front end were fixed. I fixed some navbar issues and styled the cart screen so that its design is consistent with the rest of the site. However, we still have things to work on. A lot of the cookie maker needs to be finished such as the actual backend functionality which we haven’t added. We also need to create the voting section as well as making the cookie maker page more pretty (consistent styling and animations).


```python
function swapOptions() {
      const baseSelect = document.getElementById('base'); // get the base of the cookie
      const toppingSelect = document.getElementById('topping'); // get its topping (WIP)
      const cookieImage = document.getElementById('cookie-image'); 
      
      // Swap base and topping options
      // you get a dropdown to swap the images
      const temp = baseSelect.value;
      baseSelect.value = toppingSelect.value;
      toppingSelect.value = temp;

      // Update cookie image source
      const base = baseSelect.value;
      const newImageUrl = getCookieImageURL(base);
      cookieImage.src = newImageUrl;
    }
    function getCookieImageURL(base) {
      // Define image URLs based on the selected base
      const imageUrls = {
        'chocolate': 'https://www.justsotasty.com/wp-content/uploads/2016/03/Chocolate-Cookie-for-One-12-500x375.jpg',
        'vanilla': 'https://media.istockphoto.com/id/468606656/photo/single-traditional-round-butter-biscuit-from-above.jpg?s=612x612&w=0&k=20&c=e07Z20CkUnMbobg5U2FTJU9X6yYYDvQHJpzT1h-gXdw=',
        'strawberry': 'https://sugarspunrun.com/wp-content/uploads/2023/05/Strawberry-Cookies-8-of-8.jpg',
      };
      // Return the corresponding image URL
      return imageUrls[base] || 'default_image_url.jpg';
    }
```

What do we still need to work on? Cookie maker is still a very work-in-progress project and we still have a ways to go. We understand that a finished product is necessary, but we also recognize that we need to create something quality as well as pacing ourselves. Because of this, cookie maker is still a work in progress. Here’s the issues we are having and things we need to work on.



* We need to find images
    * The cookie maker works by swapping a cookie base and topping and we are having a very hard time finding images for the base and topping which are swappable.
* We need to make animations for swapping cookies
    * Minor but purposeful animation convey a sense of clarity and help the user in understanding what is happening
* We need to integrate with backend
    * This is the largest thing we have to do
        * We need to make it so that you can create a cookie and vote for the best flavor

### Week 10

A lot of the issues in week 9 that were created were actually more so like a plan for the week. So the things that we need to work on are seen in week 9 and anything else that we would like to add would most likely be some styling things and maybe making the checkout screen nicer looking.

### A Personal Thing
One of my favorite things on the website is a small feature I added but is really big for me:


```python
---
permalink: /404.html
search_exclude: true
---

<style type="text/css" media="screen">
  body {
    background-image: url("images/starry.gif");
  }

  h1 {
    margin: 30px 0;
    font-size: 4em;
    line-height: 1;
    letter-spacing: -1px;
    color: white;
  }
</style>

<div class="container">
  <img src="images/404.gif" alt="404">
  <h1>page not found!!</h1>
</div>
```
