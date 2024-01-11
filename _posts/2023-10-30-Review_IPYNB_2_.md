---
toc: True
comments: False
layout: post
title: Independent Review
tags: ['tangibles']
categories: ['CSP', 'Week 11']
---

# Individual Code - Chrissie’s Cookies


### I: Fetching the Data for Catalog

One of the most important aspects of the website is how we fetch the data from the backend. How our site works, specifically the catalog screen, is by dynamically creating modules (we call them cards) to contain all the data for a cookie listing. The listing will contain an image, name, price, and add to cart button. The first three items are fetched from the backend via an HTTP get request. The API returns a JSON that needs to be parsed. The JSON is organized into a dictionary that we can later call from. 

Using the dictionary, we create each card and place it in the catalog grid (using css grid) so that each item is organized neatly and is responsive. The beauty of this system is that it is completely modular. It’s just like legos where everything snaps into place. And the best part is that only the cards that need to be displayed are displayed so there is no empty listing or dead code and this improves run time and loading speeds (better end user experience).

```js
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
```

Link to the commit: [Cookie Fetcher Commit](https://github.com/KinetekEnergy/ByteBuffoons-Pages/commit/e5b6545c50b630c7915b3efde8bf7cdc4ef37afa)

One thing you may notice is that there are huge chunks of code which were deleted (red) and huge chunks of code added right after (green). This is me stripping out the old dummy code that we had which hard coded all the cookies in with the new, dynamic code that could fetch from the backend. Truth be told, I am very weak at backend and it’s something that I’m just not comfortable with. Me and Harkirat ended up calling each other so that we could both work on this. I mainly worked on JavaScript and Harkirat guided me through the process of making a GET request to the backend and parsing the data. 


### II: Cookie Maker

The cookie maker feature for our website was a new feature that we began to work on but ultimately were not able to complete. Although we wished we could finish it, our failure serves as a lesson and this was a good learning experience for all of us. 

The plan was that a user could create their own cookie by swapping between a base and a topping. They name their cookie and this would be posted up to a polling site where users could vote for their favorite cookie. At the end of the voting period, the cookie with the highest votes would be automatically added to the catalog screen. This would work because all the user creations would be sent to the backend and because the backend already works to update the catalog screen, we just need to set it so that the winning cookie gets posted.

We had created a rudimentary draft for the cookie maker page but we had some issues. The first was just trying to find images which seems like a very basic non-coding related problem, but it was actually quite difficult to solve. We also severely, and I mean SEVERELY, underestimated the time it would take to do this and it was more complicated than we initially thought it would be.

In the end, cookie maker remained a dream but we gained a lot of experience from it such as creating an interactive GUI with javascript to select cookies as well as gaining experience with backend (moving and adding and removing data).

```js
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

Link to commit: [Cookie Maker Commit](https://github.com/KinetekEnergy/ByteBuffoons-Pages/commit/8e9333c374dd6d20f8fac462ca8c01637581b9a5)

This code is mainly green because it was an entirely new page that was added. I worked with Shubhay in a separate testing environment until we decided that our code was good enough to upload. 


### III: Keepin’ it all Together

We made heavy use of GitHub issues and the GitHub project system because it allowed us to visualize what needed to be done and what to work on after. Issues would be marked as a new idea / draft, todo, in progress, and done. We assigned issues to whoever needed to work on it. This helps keep track of what is being worked on and who is working on it at any given time. It makes organizing things easier and improves efficiency since we can dedicate resources (in this case, programmers) to what matters the most like how a real company or enterprise would.


### IV: It’s the Little Things That Matter

It’s a small thing. It wouldn’t change our grade. It wouldn’t add a new function to the site. Some may say it’s a downgrade. I think it’s personality and authenticity: to each their own.

Commit link: [404 Commit](https://github.com/KinetekEnergy/ByteBuffoons-Pages/commit/c6fe19619802f8084c0ec483e1f33b140b97023f)

My personal edition to the website: a 404 page with a little blast from the past.

```html
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

Oh and don’t forget the Declaration of Agile Methodology (see README).


# Individual Blog


### I: Python and Student Lessons

All blogs can be found at: [https://kinetekenergy.github.io/blog/compsci](https://kinetekenergy.github.io/blog/compsci)

All Python and Student Lessons are organized chronologically and are a way to show learning. I make sure to complete all hacks and do all the homework to make the most out of the student lessons. I try to show as much effort as possible, especially in the homework.

Some of my most favorite lessons / homeworks are here:



[Boolean IF](https://kinetekenergy.github.io/blog//2023/10/09/boolean-if_IPYNB_2_.html)

This homework, I got to experiment with saving files to keep track of user high scores which was a fun idea to play with. I’m quite used to programming something in Python where the data is only stored at run time, so this was oddly fun for me to save files.

[List & Search](https://kinetekenergy.github.io/blog//2023/10/12/lists-and-search_IPYNB_2_.html)

Arguably my favorite homework assignment, it puts a super fun twist on a seemingly boring and drab question. The homework asked us to use linear search to get to a certain random value and output the number of iterations to get there. That’s boring. So how ‘bout we take a classic road-trip / songs-to-sing-to-pass-time song and apply it here. You can see the output for yourself to check what I mean. Interestingly enough, the hardest part about this assignment is the English part of it because based on the current iteration, the output will have to vary based on it towards the end.


### II: Pseudo Code

```python
DISPLAY ("What's your name?")
name <- INPUT ()
DISPLAY ("Hello")
DISPLAY (name)
```

Pseudo code lets you draft code before it’s written. Here, there’s code to display your name with user input. It’s a neat topic, but I think that College Board’s pseudo code is too detailed in the sense that it’s redundant and you might as well just program normally.


### III: College Board Quiz

Questions I missed:



* Q14:
    * I answered: Program A and program B display a different number of values.
    * Correct answer: Program A and program B display the same number of values, but the values differ.
    * What went wrong: I misread the prompt. I knew that program B would display the same # of answers but shifted. I just read the prompt wrong.
* Q26:
    * I answered: C
    * Correct answer: A
    * What went wrong: I didn’t conceptually understand what the problem was asking.
* Q28: 
    * I answered: 6
    * Correct answer: 8
    * What went wrong: I didn’t understand what to do since I’m bad at binary and binary math.
* Q32:  
    * I answered: Participants who read more were generally more likely to say they are interested in the application.
    * Correct answer: Participants who use a smartphone more were generally less likely to say they read more.
    * What went wrong: I misread the graph.
* Q42: 
    * I answered: 2^4 times as many addresses are available.
    * Correct answer: 2^96 times as many addresses are available.
    * What went wrong: I am bad at networking and this type of math. I can’t visualize these problems well.
* Q43: 
    * I answered: The algorithm runs, but not in reasonable time.
    * Correct answer: The algorithm runs in reasonable time.
    * What went wrong: It says that the number of steps of the algorithm is a polynomial so it runs in a reasonable time. I don’t get this because for a huge n number, the steps would be exponential so how would this be an optimized algorithm?
* Q51: 
    * I answered: Hannah writes a message to send to Isabel and hides the message under a rock behind the soccer field. Hannah gives Isabel the exact location of the rock so that only Isabel can find the message.
    * Correct answer: Finn and Gwen develop a system that maps each letter of the alphabet to a unique symbol using a secret key. Finn uses the key to write a message to Gwen where each letter is replaced with the corresponding symbol. Gwen uses the key to map each symbol back to the original letter.
    * What went wrong: I unfortunately changed my answer last second. But I understand how you can symmetrically encrypt a message.
* Q58: 
    * I answered: I, II, and III
    * Correct answer: I and II only
    * What went wrong: I knew I and II are correct. I thought that distributing work across many users allows problems to be solved in a reasonable time. It makes sense: more people = solved faster. I guess it’s not the case because some problems can’t be solved in a reasonable amount of time although CollegeBoard doesn’t say what. In fact, CollegeBoard is wrong. There are crowdsourced virtual supercomputers which can allow users to participate in it and allow their computers to join this network. It essentially is like a supercomputer but each user contributes their PC to it via the cloud. It was actually used to help speed up research for the COVID vaccine. That too, if a supercomputer center volunteers to join a crowdsourced effort (let’s say UCSD joins in), would that not allow III to be correct?


### IV: Reflection

This trimester was quite fun. I had fun with my group making something we liked and because cookies are the best! I learned a lot of things about web development and python, but I think I need to work on the backend. I am very bad at it and not comfortable with it, so I think the only thing to do is to force myself to do it. Just dive in head first. This is what I think is my opportunity for growth.
