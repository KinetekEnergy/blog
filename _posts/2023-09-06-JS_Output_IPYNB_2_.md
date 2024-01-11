---
toc: True
comments: False
layout: post
title: JS Output with JQuery
tags: ['hacks']
categories: ['CSP', 'Week 2']
---

### Markdown Table

| Make | Model | Year | Color | Price |
|------|-------|------|-------|-------|
|Ford|Mustang|2022|Red|$35,000|
|Toyota|Camry|2022|Silver|$25,00|
|Tesla|Model S|2022|White|$80,000|
|Cadillac|Broughan|1969|Black|$10,000|
|Ford|F-350|1997|Green|$15,000|
|Ford|Excursion|2003|Green|$25,000|
|Ford|Ranger|2012|Red|$8,000|
|Kuboto|L3301 Tractor|2015|Orange|$12,000|
|Ford|Fusion Energi|2015|Green|$15,000|
|Acura|XL|2006|Grey|$10,000|
|Ford|F150 Lightning|2023|Grey|$70,000|

<hr style='solid'>

### HTML Table


```python
%%html
<table class="table">
    <thead>
        <tr>
            <th>Make</th>
            <th>Model</th>
            <th>Year</th>
            <th>Color</th>
            <th>Price</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Cadillac</td>
            <td>Broughan</td>
            <td>1969</td>
            <td>Black</td>
            <td>$10,000</td>
        </tr>
        <tr>
            <td>Ford</td>
            <td>F-350</td>
            <td>1997</td>
            <td>Green</td>
            <td>$15,000</td>
        </tr>
        <tr>
            <td>Ford</td>
            <td>Excursion</td>
            <td>2003</td>
            <td>Green</td>
            <td>$25,000</td>
        </tr>
        <tr>
            <td>Ford</td>
            <td>Ranger</td>
            <td>2012</td>
            <td>Red</td>
            <td>$8,000</td>
        </tr>
        <tr>
            <td>Kuboto</td>
            <td>L3301 Tractor</td>
            <td>2015</td>
            <td>Orange</td>
            <td>$12,000</td>
        </tr>
        <tr>
            <td>Ford</td>
            <td>Fusion Energi</td>
            <td>2015</td>
            <td>Guard</td>
            <td>$25,000</td>
        </tr>
        <tr>
            <td>Acura</td>
            <td>XL</td>
            <td>2006</td>
            <td>Grey</td>
            <td>$10,000</td>
        </tr>
        <tr>
            <td>Ford</td>
            <td>F150 Lightning</td>
            <td>2024</td>
            <td>Guard</td>
            <td>$70,000</td>
        </tr>
    </tbody>
</table>
```

<hr style='solid'>

### HTML Table with JavaScript jquery
JavaScript is a programming language that works with HTML data, CSS helps to style that data.  In this example, we are using JavaScript and CSS that was developed by others (3rd party).  Addithing the 3rd party code makes the table interactive.
- Look at the href and src on lines inside of the lines in `<head>` tags.  This is adding code to our page from others.
- Observe the `<script>` tags at the bottom of the page.  This is generating the interactive table, from the third party code, using the data `<table id="demo">` from the `<body>`.  


```python
%%html

<!-- Head contains information to Support the Document -->
<head>
    <!-- load jQuery and DataTables output style and scripts -->
    <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.13.4/css/jquery.dataTables.min.css">
    <script type="text/javascript" language="javascript" src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script>var define = null;</script>
    <script type="text/javascript" language="javascript" src="https://cdn.datatables.net/1.13.4/js/jquery.dataTables.min.js"></script>
</head>

<!-- Body contains the contents of the Document -->
<body>
    <table id="demo" class="table">
        <thead>
            <tr>
                <th>Make</th>
                <th>Model</th>
                <th>Year</th>
                <th>Color</th>
                <th>Price</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Ford</td>
                <td>Mustang</td>
                <td>2022</td>
                <td>Red</td>
                <td>$35,000</td>
            </tr>
            <tr>
                <td>Toyota</td>
                <td>Camry</td>
                <td>2022</td>
                <td>Silver</td>
                <td>$25,000</td>
            </tr>
            <tr>
                <td>Tesla</td>
                <td>Model S</td>
                <td>2022</td>
                <td>White</td>
                <td>$80,000</td>
            </tr>
            <tr>
                <td>Cadillac</td>
                <td>Broughan</td>
                <td>1969</td>
                <td>Black</td>
                <td>$10,000</td>
            </tr>
            <tr>
                <td>Ford</td>
                <td>F-350</td>
                <td>1997</td>
                <td>Green</td>
                <td>$15,000</td>
            </tr>
            <tr>
                <td>Ford</td>
                <td>Excursion</td>
                <td>2003</td>
                <td>Green</td>
                <td>$25,000</td>
            </tr>
            <tr>
                <td>Ford</td>
                <td>Ranger</td>
                <td>2012</td>
                <td>Red</td>
                <td>$8,000</td>
            </tr>
            <tr>
                <td>Kuboto</td>
                <td>L3301 Tractor</td>
                <td>2015</td>
                <td>Orange</td>
                <td>$12,000</td>
            </tr>
            <tr>
                <td>Ford</td>
                <td>Fusion Energi</td>
                <td>2015</td>
                <td>Guard</td>
                <td>$25,000</td>
            </tr>
            <tr>
                <td>Acura</td>
                <td>XL</td>
                <td>2006</td>
                <td>Grey</td>
                <td>$10,000</td>
            </tr>
            <tr>
                <td>Ford</td>
                <td>F150 Lightning</td>
                <td>2024</td>
                <td>Guard</td>
                <td>$70,000</td>
            </tr>
        </tbody>
    </table>
</body>

<!-- Script is used to embed executable code -->
<script>
    $("#demo").DataTable();
</script>

```

<hr style='solid'>

### Custom table


```python
%%html

<!-- Head contains information to Support the Document -->

<head>
    <!-- load jQuery and DataTables output style and scripts -->
    <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.13.4/css/jquery.dataTables.min.css">
    <script type="text/javascript" language="javascript" src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script>var define = null;</script>
    <script type="text/javascript" language="javascript"
        src="https://cdn.datatables.net/1.13.4/js/jquery.dataTables.min.js"></script>
</head>

<!-- Body contains the contents of the Document -->

<body>
    <style>
        @font-face {
            font-family: 'Noto Sans';
            font-weight: 400;
            font-style: normal;
            src: url("../fonts/Noto-Sans-regular/Noto-Sans-regular.eot");
            src: url("../fonts/Noto-Sans-regular/Noto-Sans-regular.eot?#iefix") format("embedded-opentype"), local("Noto Sans"), local("Noto-Sans-regular"), url("../fonts/Noto-Sans-regular/Noto-Sans-regular.woff2") format("woff2"), url("../fonts/Noto-Sans-regular/Noto-Sans-regular.woff") format("woff"), url("../fonts/Noto-Sans-regular/Noto-Sans-regular.ttf") format("truetype"), url("../fonts/Noto-Sans-regular/Noto-Sans-regular.svg#NotoSans") format("svg");
        }

        @font-face {
            font-family: 'Noto Sans';
            font-weight: 700;
            font-style: normal;
            src: url("../fonts/Noto-Sans-700/Noto-Sans-700.eot");
            src: url("../fonts/Noto-Sans-700/Noto-Sans-700.eot?#iefix") format("embedded-opentype"), local("Noto Sans Bold"), local("Noto-Sans-700"), url("../fonts/Noto-Sans-700/Noto-Sans-700.woff2") format("woff2"), url("../fonts/Noto-Sans-700/Noto-Sans-700.woff") format("woff"), url("../fonts/Noto-Sans-700/Noto-Sans-700.ttf") format("truetype"), url("../fonts/Noto-Sans-700/Noto-Sans-700.svg#NotoSans") format("svg");
        }

        @font-face {
            font-family: 'Noto Sans';
            font-weight: 400;
            font-style: italic;
            src: url("../fonts/Noto-Sans-italic/Noto-Sans-italic.eot");
            src: url("../fonts/Noto-Sans-italic/Noto-Sans-italic.eot?#iefix") format("embedded-opentype"), local("Noto Sans Italic"), local("Noto-Sans-italic"), url("../fonts/Noto-Sans-italic/Noto-Sans-italic.woff2") format("woff2"), url("../fonts/Noto-Sans-italic/Noto-Sans-italic.woff") format("woff"), url("../fonts/Noto-Sans-italic/Noto-Sans-italic.ttf") format("truetype"), url("../fonts/Noto-Sans-italic/Noto-Sans-italic.svg#NotoSans") format("svg");
        }

        @font-face {
            font-family: 'Noto Sans';
            font-weight: 700;
            font-style: italic;
            src: url("../fonts/Noto-Sans-700italic/Noto-Sans-700italic.eot");
            src: url("../fonts/Noto-Sans-700italic/Noto-Sans-700italic.eot?#iefix") format("embedded-opentype"), local("Noto Sans Bold Italic"), local("Noto-Sans-700italic"), url("../fonts/Noto-Sans-700italic/Noto-Sans-700italic.woff2") format("woff2"), url("../fonts/Noto-Sans-700italic/Noto-Sans-700italic.woff") format("woff"), url("../fonts/Noto-Sans-700italic/Noto-Sans-700italic.ttf") format("truetype"), url("../fonts/Noto-Sans-700italic/Noto-Sans-700italic.svg#NotoSans") format("svg");
        }

        .highlight table td {
            padding: 5px;
        }

        .highlight table pre {
            margin: 0;
        }

        .highlight .cm {
            color: #999988;
            font-style: italic;
        }

        .highlight .cp {
            color: #999999;
            font-weight: bold;
        }

        .highlight .c1 {
            color: #999988;
            font-style: italic;
        }

        .highlight .cs {
            color: #999999;
            font-weight: bold;
            font-style: italic;
        }

        .highlight .c,
        .highlight .cd {
            color: #999988;
            font-style: italic;
        }

        .highlight .err {
            color: #a61717;
            background-color: #e3d2d2;
        }

        .highlight .gd {
            color: #000000;
            background-color: #ffdddd;
        }

        .highlight .ge {
            color: #000000;
            font-style: italic;
        }

        .highlight .gr {
            color: #aa0000;
        }

        .highlight .gh {
            color: #999999;
        }

        .highlight .gi {
            color: #000000;
            background-color: #ddffdd;
        }

        .highlight .go {
            color: #888888;
        }

        .highlight .gp {
            color: #555555;
        }

        .highlight .gs {
            font-weight: bold;
        }

        .highlight .gu {
            color: #aaaaaa;
        }

        .highlight .gt {
            color: #aa0000;
        }

        .highlight .kc {
            color: #000000;
            font-weight: bold;
        }

        .highlight .kd {
            color: #000000;
            font-weight: bold;
        }

        .highlight .kn {
            color: #000000;
            font-weight: bold;
        }

        .highlight .kp {
            color: #000000;
            font-weight: bold;
        }

        .highlight .kr {
            color: #000000;
            font-weight: bold;
        }

        .highlight .kt {
            color: #445588;
            font-weight: bold;
        }

        .highlight .k,
        .highlight .kv {
            color: #000000;
            font-weight: bold;
        }

        .highlight .mf {
            color: #009999;
        }

        .highlight .mh {
            color: #009999;
        }

        .highlight .il {
            color: #009999;
        }

        .highlight .mi {
            color: #009999;
        }

        .highlight .mo {
            color: #009999;
        }

        .highlight .m,
        .highlight .mb,
        .highlight .mx {
            color: #009999;
        }

        .highlight .sb {
            color: #d14;
        }

        .highlight .sc {
            color: #d14;
        }

        .highlight .sd {
            color: #d14;
        }

        .highlight .s2 {
            color: #d14;
        }

        .highlight .se {
            color: #d14;
        }

        .highlight .sh {
            color: #d14;
        }

        .highlight .si {
            color: #d14;
        }

        .highlight .sx {
            color: #d14;
        }

        .highlight .sr {
            color: #009926;
        }

        .highlight .s1 {
            color: #d14;
        }

        .highlight .ss {
            color: #990073;
        }

        .highlight .s {
            color: #d14;
        }

        .highlight .na {
            color: #008080;
        }

        .highlight .bp {
            color: #999999;
        }

        .highlight .nb {
            color: #0086B3;
        }

        .highlight .nc {
            color: #445588;
            font-weight: bold;
        }

        .highlight .no {
            color: #008080;
        }

        .highlight .nd {
            color: #3c5d5d;
            font-weight: bold;
        }

        .highlight .ni {
            color: #800080;
        }

        .highlight .ne {
            color: #990000;
            font-weight: bold;
        }

        .highlight .nf {
            color: #990000;
            font-weight: bold;
        }

        .highlight .nl {
            color: #990000;
            font-weight: bold;
        }

        .highlight .nn {
            color: #555555;
        }

        .highlight .nt {
            color: #000080;
        }

        .highlight .vc {
            color: #008080;
        }

        .highlight .vg {
            color: #008080;
        }

        .highlight .vi {
            color: #008080;
        }

        .highlight .nv {
            color: #008080;
        }

        .highlight .ow {
            color: #000000;
            font-weight: bold;
        }

        .highlight .o {
            color: #000000;
            font-weight: bold;
        }

        .highlight .w {
            color: #bbbbbb;
        }

        .highlight {
            background-color: #f8f8f8;
        }

        body {
            background-color: #fff;
            padding: 50px;
            font: 14px/1.5 "Noto Sans", "Helvetica Neue", Helvetica, Arial, sans-serif;
            color: #727272;
            font-weight: 400;
        }

        h1,
        h2,
        h3,
        h4,
        h5,
        h6 {
            color: #222;
            margin: 0 0 20px;
        }

        p,
        ul,
        ol,
        table,
        pre,
        dl {
            margin: 0 0 20px;
        }

        h1,
        h2,
        h3 {
            line-height: 1.1;
        }

        h1 {
            font-size: 28px;
        }

        h2 {
            color: #393939;
        }

        h3,
        h4,
        h5,
        h6 {
            color: #494949;
        }

        a {
            color: #267CB9;
            text-decoration: none;
        }

        a:hover,
        a:focus {
            color: #069;
            font-weight: bold;
        }

        a small {
            font-size: 11px;
            color: #777;
            margin-top: -0.3em;
            display: block;
        }

        a:hover small {
            color: #777;
        }

        .wrapper {
            width: 860px;
            margin: 0 auto;
        }

        blockquote {
            border-left: 1px solid #e5e5e5;
            margin: 0;
            padding: 0 0 0 20px;
            font-style: italic;
        }

        code,
        pre {
            font-family: Monaco, Bitstream Vera Sans Mono, Lucida Console, Terminal, Consolas, Liberation Mono, DejaVu Sans Mono, Courier New, monospace;
            color: #333;
        }

        pre {
            padding: 8px 15px;
            background: #f8f8f8;
            border-radius: 5px;
            border: 1px solid #e5e5e5;
            overflow-x: auto;
        }

        table {
            width: 100%;
            border-collapse: collapse;
        }

        th,
        td {
            text-align: left;
            padding: 5px 10px;
            border-bottom: 1px solid #e5e5e5;
        }

        dt {
            color: #444;
            font-weight: 700;
        }

        th {
            color: #444;
        }

        img {
            max-width: 100%;
        }

        kbd {
            background-color: #fafbfc;
            border: 1px solid #c6cbd1;
            border-bottom-color: #959da5;
            border-radius: 3px;
            box-shadow: inset 0 -1px 0 #959da5;
            color: #444d56;
            display: inline-block;
            font-size: 11px;
            line-height: 10px;
            padding: 3px 5px;
            vertical-align: middle;
        }

        header {
            width: 270px;
            float: left;
            position: fixed;
            -webkit-font-smoothing: subpixel-antialiased;
        }

        ul.downloads {
            list-style: none;
            height: 40px;
            padding: 0;
            background: #f4f4f4;
            border-radius: 5px;
            border: 1px solid #e0e0e0;
            width: 270px;
        }

        .downloads li {
            width: 89px;
            float: left;
            border-right: 1px solid #e0e0e0;
            height: 40px;
        }

        .downloads li:first-child a {
            border-radius: 5px 0 0 5px;
        }

        .downloads li:last-child a {
            border-radius: 0 5px 5px 0;
        }

        .downloads a {
            line-height: 1;
            font-size: 11px;
            color: #676767;
            display: block;
            text-align: center;
            padding-top: 6px;
            height: 34px;
        }

        .downloads a:hover,
        .downloads a:focus {
            color: #675C5C;
            font-weight: bold;
        }

        .downloads ul a:active {
            background-color: #f0f0f0;
        }

        strong {
            color: #222;
            font-weight: 700;
        }

        .downloads li+li+li {
            border-right: none;
            width: 89px;
        }

        .downloads a strong {
            font-size: 14px;
            display: block;
            color: #222;
        }

        section {
            width: 500px;
            float: right;
            padding-bottom: 50px;
        }

        small {
            font-size: 11px;
        }

        hr {
            border: 0;
            background: #e5e5e5;
            height: 1px;
            margin: 0 0 20px;
        }

        footer {
            width: 270px;
            float: left;
            position: fixed;
            bottom: 50px;
            -webkit-font-smoothing: subpixel-antialiased;
        }

        @media print,
        screen and (max-width: 960px) {
            div.wrapper {
                width: auto;
                margin: 0;
            }

            header,
            section,
            footer {
                float: none;
                position: static;
                width: auto;
            }

            header {
                padding-right: 320px;
            }

            section {
                border: 1px solid #e5e5e5;
                border-width: 1px 0;
                padding: 20px 0;
                margin: 0 0 20px;
            }

            header a small {
                display: inline;
            }

            header ul {
                position: absolute;
                right: 50px;
                top: 52px;
            }
        }

        @media print,
        screen and (max-width: 720px) {
            body {
                word-wrap: break-word;
            }

            header {
                padding: 0;
            }

            header ul,
            header p.view {
                position: static;
            }

            pre,
            code {
                word-wrap: normal;
            }
        }

        @media print,
        screen and (max-width: 480px) {
            body {
                padding: 15px;
            }

            .downloads {
                width: 99%;
            }

            .downloads li,
            .downloads li+li+li {
                width: 33%;
            }
        }

        @media print {
            body {
                padding: 0.4in;
                font-size: 12pt;
                color: #444;
            }
        }
    </style>
    <table id="demo" class="table">
        <thead>
            <tr>
                <th>Brand</th>
                <th>Model</th>
                <th>Resolution</th>
                <th>Autofocus</th>
                <th>Price</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Sony</td>
                <td>A7 IV</td>
                <td>33MP</td>
                <td>759-point</td>
                <td>2499</td>
            </tr>
            <tr>
                <td>Canon</td>
                <td>EOS R5</td>
                <td>45 MP</td>
                <td>5940-zone</td>
                <td>3899</td>
            </tr>
            <tr>
                <td>Canon</td>
                <td>EOS R10</td>
                <td>24.2 MP</td>
                <td>651-area</td>
                <td>824</td>
            </tr>
            <tr>
                <td>Fujifilm</td>
                <td>X-T5</td>
                <td>40.2 MP</td>
                <td>425-point</td>
                <td>1659.95</td>
            </tr>
            <tr>
                <td>Canon</td>
                <td>EOS R6</td>
                <td>20.1 MP</td>
                <td>6072-point</td>
                <td>2299</td>
            </tr>
            <tr>
                <td>Nikon</td>
                <td>Z6 II</td>
                <td>24.5 MP</td>
                <td>273-point hybrid</td>
                <td>1599</td>
            </tr>
            <tr>
                <td>Sony</td>
                <td>A7R V</td>
                <td>61 MP</td>
                <td>693 PDAF + 425 CDAF</td>
                <td>3899</td>
            </tr>
            <tr>
                <td>Nikon</td>
                <td>Z9</td>
                <td>45.7 MP</td>
                <td>493 hybrid phase/contrast detect AF points</td>
                <td>5499</td>
            </tr>
            <tr>
                <td>Hasselblad</td>
                <td>X2D 100C</td>
                <td>100 MP</td>
                <td>294-point array</td>
                <td>7369</td>
            </tr>
            <tr>
                <td>Nikon</td>
                <td>Z8</td>
                <td>45.7 MP</td>
                <td>Deep learning 3D 493-point</td>
                <td>3999</td>
            </tr>
            <tr>
                <td>Nikon</td>
                <td>Z5</td>
                <td>24.3 MP</td>
                <td>273-point</td>
                <td>1299</td>
            </tr>
        </tbody>
    </table>
</body>

<!-- Script is used to embed executable code -->
<script>
    $("#demo").DataTable();
</script>
```

<hr style='solid'>

### Markdown vs Javascript tables
The benefits of a markdown table varies based on your use case as well as the technologies required by your employer, company, etc.

Markdown tables have the ability of making things super easy as you don't have to write any code. However, markdown tables do not support javascript features such as sorting or multiple pages for tables (which is useful if you have many items). Furthermore, markdown tables are harder to modify and change via backend code (maybe you want to use a database and display it via a table such as stock prices) as well as being harder to style with frontend code.

In summary, if you need a quick and easy solution and don't have the need to make any changes to the table as well as having minimal items, markdown is the best for this.

If you need a solution which can be customizable exactly the way you want as well as being easily modifable, markdown is probably a bad solution.

There is no right or wrong answer for this: only personal preference and what you need.

<hr style='solid'>

### HTML vs JavaScript
While HTML and JavaScript (JS) are both programming languages used for web development, they both have stark differences.

HTML is used to:
- Create the structure
- Control the layout of the content
- Provide structure for the web page design
- And is the fundamental building block of any web page

JS on the other hand is used to:
- Increase interactivity
- Add interactivity to a web page
- Handle complex functions and features
- Enhance functionality since it is a programmatic code

In other words, HTML can be similar to the frame of a house and the layout and blueprint. JS would be the internals of the house such as plubming, electricity, gas, etc. Both cannot exist without each other just like how HTML cannot exist without JS and vice versa.
