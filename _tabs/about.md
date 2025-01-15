---
# the default layout is 'page'
icon: fas fa-info-circle
order: 4
---

<style>
    .grid-container {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
        gap: 10px;
    }

    .grid-item {
        text-align: center;
        border-radius: 5px;
    }

    .grid-item img {
        width: 100%;
        object-fit: contain;
        border-radius: 5px !important;
    }

    .grid-item p {
        margin: 5px 0;
        white-space: pre-line;
    }

    /* Smooth animation of the scroller */
    .slider {
        box-shadow: 0 10px 20px -5px rgba(0, 0, 0, 0.125);
        height: 200px;
        margin: auto;
        overflow: hidden;
        position: relative;
        border-radius: 5px;
    }

    .slider::before,
    .slider::after {
        background: linear-gradient(to right, #121212 0%, rgba(255, 255, 255, 0) 100%);
        content: "";
        height: 200px;
        position: absolute;
        width: 200px;
        z-index: 2;
    }

    .slider::after {
        right: 0;
        top: 0;
        transform: rotateZ(180deg);
    }

    .slider::before {
        left: 0;
        top: 0;
    }

    /* Image Track Animation */
    .slider .slide-track {
        display: flex;
        animation: scroll 60s linear infinite;
    }

    /* Each Slide */
    .slider .slide {
        flex: 0 0 auto;
        width: auto;
        height: 200px;
        padding-left: 10px;
        padding-right: 10px;
        position: relative;
        overflow: hidden;
    }

    /* Image within slide */
    .slider .slide img {
        width: 100%;
        height: 100%;
        object-fit: cover;
        border-radius: 5px;
        transition: transform 0.3s ease, filter 0.3s ease;
        z-index: 1;
        position: relative;
    }

    /* Hover effect: Image blurs */
    .slider .slide:hover img {
        filter: blur(5px);
    }

    /* Text Box that appears on hover */
    .slider .slide .hover-text {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        backdrop-filter: blur(5px);
        background-color: rgba(255, 255, 255, 0.5);
        border: 2px solid #000;
        padding: 10px 20px;
        font-size: 18px;
        font-weight: bold;
        color: #000 !important;
        border-radius: 5px;
        opacity: 0;
        transition: opacity 0.3s ease;
        z-index: 2;
        text-align: center;
    }

    .slider a {
        color: black !important;
    }

    /* Show text on hover */
    .slider .slide:hover .hover-text {
        opacity: 1;
    }

    /* Adding hover pause for slider */
    @keyframes scroll {
        0% {
            transform: translateX(0);
        }

        100% {
            transform: translateX(calc(-250px * 28));
        }
    }

    /* Pauses the slider on hover */
    .slider:hover .slide-track {
        animation-play-state: paused;
    }

    /* Style for the anchor within hover text */
    .hover-text a {
        color: #000;
        text-decoration: none;
        font-weight: bold;
    }
</style>

## Places I've Lived

<div class="grid-container" id="grid_container"></div>

## Me

My name is Aashray Reddy, a 16 year old highschool student attending Del Norte Highschool.

My interests include:

- 💻 Computers
  - Programming
    - Python, C, Arduino, hardware design and electrical engineering
      - I usually use Python for high level projects like Artificial Intelligence
      - I usually use C for projects where I need to control hardware (ex: using Arduinos)
  - Cybersecurity
    - I am in CyberAegis and do Windows
- 🎹 Piano
  - I have been playing for around 1.5 years
- 🏄 Surfing
  - I usually go to Pacific Beach but Torrey Pines has nice waves too
  - [Torrey Pines Forecast](https://www.surfline.com/surf-report/torrey-pines-state-beach/584204204e65fad6a7709994?camId=5fc81527bceda049ecf8ac63)
  - [Torrey Pines Forecast Alternative](https://www.surf-forecast.com/breaks/Torrey-Pines-State-Beach/forecasts/latest#)
  - [Beaufort Wind Scale](https://www.spc.noaa.gov/faq/tornado/beaufort.html)
  - [Forecast Guide](https://www.lapointcamps.com/blog/how-to-read-surf-forecast/)
- 🏂 Snowboarding
  - My favorite place to Snowboard is BigBear since it is close
  - I also like to go to Mammoth if I have time

## 📷 [Photography](https://www.pixelpotpourri.com/)

I have been doing photography for around 6 years (I forget haha: it's been so long). Here are some images from my photography site. You can click an image to see more info. Most of these images are from places within California!

<div class="slider">
    <div class="slide-track" id="slide-track">
        <!-- Images will be appended here via JavaScript -->
    </div>
</div>

## Image Collages

Here is a personal image collage:

![Personal image collage](https://github.com/user-attachments/assets/27502a63-0d74-4c24-b42f-d2ad0eca57be)

<!-- SCRIPT -->
<script>
    var container = document.getElementById("grid_container");
    var http_source = "https://upload.wikimedia.org/wikipedia/commons/";

    // Date variables
    var birthDate = new Date("2008-01-17");
    var moveToCaliforniaDate = new Date("2015-01-01");

    // flags
    var living_in_the_world = [
        { "flag": "0/01/Flag_of_California.svg", "greeting": "Hey!", "description": "California" },
        { "flag": "a/ac/Flag_of_Indiana.svg", "greeting": "How doo!", "description": "Indiana" }
    ];

    // adjusts the grammar based on date (ex: 1 month, 2 months)
    function pluralize(value, singular, plural = null) {
        if (value === 1) {
            return `${value} ${singular}`;
        } else if (value > 1 || value === 0) {
            return `${value} ${plural || singular + 's'}`;
        }
        return '';
    }

    // find the time difference between two dates
    function calculateTimeDiff(startDate, endDate) {
        var diff = endDate - startDate;

        var years = Math.floor(diff / (1000 * 60 * 60 * 24 * 365.25));
        var months = Math.floor((diff % (1000 * 60 * 60 * 24 * 365.25)) / (1000 * 60 * 60 * 24 * 30.44));
        var days = Math.floor((diff % (1000 * 60 * 60 * 24 * 30.44)) / (1000 * 60 * 60 * 24));
        var hours = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        var minutes = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
        var seconds = Math.floor((diff % (1000 * 60)) / 1000);

        var timeString = `${pluralize(years, 'year')}\n${pluralize(months, 'month')}\n${pluralize(days, 'day')}`;

        if (hours > 0 || minutes > 0 || seconds > 0) {
            timeString += `\n${pluralize(hours, 'hour')}\n${pluralize(minutes, 'minute')}\n${pluralize(seconds, 'second')}`;
        }

        return timeString;
    }

    // update the date items in real time
    function updateGridItems() {
        container.innerHTML = ""; // clear existing content

        living_in_the_world.forEach((location, index) => {
            var gridItem = document.createElement("div");
            gridItem.className = "grid-item";

            var img = document.createElement("img");
            img.src = http_source + location.flag;
            img.alt = location.flag + " Flag";

            var description = document.createElement("p");
            description.textContent = location.description;

            var greeting = document.createElement("p");
            greeting.textContent = location.greeting;

            var timeLived = document.createElement("p");

            // calculate time lived based on the location
            currentDate = new Date();
            console.log(currentDate);
            if (index === 0) {  // California
                timeLived.textContent = `Lived here for:\n${calculateTimeDiff(moveToCaliforniaDate, currentDate)}`;
            } else {  // Indiana
                timeLived.textContent = `Lived here for:\n${calculateTimeDiff(birthDate, moveToCaliforniaDate)}`;
            }

            // put it all together
            gridItem.appendChild(img);
            gridItem.appendChild(description);
            gridItem.appendChild(greeting);
            gridItem.appendChild(timeLived);

            container.appendChild(gridItem);
        });
    }

    // initial update and set interval for real-time updates every second
    updateGridItems();
    setInterval(updateGridItems, 1000);

    // Array of image URLs and their respective links
    const images = [
        { src: "../assets/img/photography/car.jpg", link: "https://www.pixelpotpourri.com/Galleries/All-Work/i-mF7B22J" },
        { src: "../assets/img/photography/wall.jpg", link: "https://www.pixelpotpourri.com/Galleries/All-Work/i-vfnH97m" },
        { src: "../assets/img/photography/fish.jpg", link: "https://www.pixelpotpourri.com/Galleries/All-Work/i-t4JLKM6" },
        { src: "../assets/img/photography/temple.jpg", link: "https://www.pixelpotpourri.com/Galleries/All-Work/i-MjpgKbX" },
        { src: "../assets/img/photography/library.jpg", link: "https://www.pixelpotpourri.com/Galleries/All-Work/i-3qRCPFq" },
        { src: "../assets/img/photography/pier.jpg", link: "https://www.pixelpotpourri.com/Galleries/All-Work/i-cNg27wP" },
        { src: "../assets/img/photography/mountains.jpg", link: "https://www.pixelpotpourri.com/Galleries/All-Work/i-vr5ZvBn" },
        { src: "../assets/img/photography/beach.jpg", link: "https://www.pixelpotpourri.com/Galleries/All-Work/i-b8TGzNW" },
        { src: "../assets/img/photography/coronado1.jpg", link: "https://www.pixelpotpourri.com/Galleries/All-Work/i-6nvkvPM" },
        { src: "../assets/img/photography/blackandwhite.jpg", link: "https://www.pixelpotpourri.com/Galleries/All-Work/i-Ptfv836" },
        { src: "../assets/img/photography/sunset.jpg", link: "https://www.pixelpotpourri.com/Galleries/All-Work/i-mRBK5wf" },
        { src: "../assets/img/photography/building.jpg", link: "https://www.pixelpotpourri.com/Galleries/All-Work/i-rqfZ9wv" },
        { src: "../assets/img/photography/coronado2.jpg", link: "https://www.pixelpotpourri.com/Galleries/All-Work/i-mtSg4rR" },
        { src: "../assets/img/photography/lily.jpg", link: "https://www.pixelpotpourri.com/Galleries/All-Work/i-PKGZ3ng" }
        // Add more images and links here
    ];

    // Function to create an image element with a link
    function createImage(src, link) {
        const a = document.createElement('a');
        a.href = link;
        a.target = "_blank"; // Opens link in new tab

        const img = document.createElement('img');
        img.src = src;
        img.height = 200;
        img.style.objectFit = 'cover';
        img.style.borderRadius = '5px';

        a.appendChild(img);
        return a;
    }

    // Function to add images to the track
    function addImages() {
        const track = document.getElementById('slide-track');
        images.forEach(item => {
            const slideDiv = document.createElement('div');
            slideDiv.className = 'slide';

            const imgElement = createImage(item.src, item.link);
            slideDiv.appendChild(imgElement);

            // Add the hover text box with a link
            const hoverText = document.createElement('div');
            hoverText.className = 'hover-text';

            const hoverLink = document.createElement('a');
            hoverLink.href = item.link;
            hoverLink.target = "_blank"; // Open link in a new tab
            hoverLink.textContent = 'Open';

            hoverText.appendChild(hoverLink);
            slideDiv.appendChild(hoverText);

            track.appendChild(slideDiv);
        });
    }

    // Infinite loop to keep appending images
    function loopImages() {
        addImages(); // First load
        setInterval(addImages, 100); // Re-add images
    }

    // Start appending images on page load
    window.onload = loopImages;
</script>
