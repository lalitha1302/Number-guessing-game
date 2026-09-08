**6. Program Code**
<!DOCTYPE html>
<html>
<head>
 <title>Student Registration Form</title>
 <style>
 table {
 border-collapse: collapse;
 margin: auto;
 background-color: #f9f9f9;
 padding: 20px;
 }
 td {
 padding: 10px;
 }
 h2 {
 text-align: center;
 color: #333;
 }
 input, select, textarea {
 width: 100%;
 padding: 6px;
 }
 input[type=radio], input[type=checkbox] {
 width: auto;
 }
 .center {
 text-align: center;
 }
body {
 font-family: Arial, sans-serif;
 margin: 40px;
 }
 .success-message {
 color: green;
 margin-top: 15px;
 display: none; /* Hidden until shown */
 }
 input, button {
 padding: 8px;
 margin-top: 10px;
 }
 </style>
</head>
<body>
 <h2>Student Registration Form</h2>
 <form id="myForm" action="#" method="post">
 <table border="1">
 <tr>
 <td>First Name:</td>
 <td><input type="text" name="first_name" placeholder="Enter first name" required></td>
 </tr>
 <tr>
 <td>Last Name:</td>
 <td><input type="text" name="last_name" placeholder="Enter last name" required></td>
 </tr>
 <tr>
 <td>Gender:</td>
 <td>
 <input type="radio" name="gender" value="Male" required> Male
 <input type="radio" name="gender" value="Female"> Female
 </td>
 </tr>
 <tr>
 <td>Date of Birth:</td>
 <td><input type="date" name="dob" required></td>
 </tr>
 <tr>
 <td>Email:</td>
<td><input type="email" name="email" placeholder="Enter email" required></td>
 </tr>
 <tr>
 <td>Phone Number:</td>
 <td><input type="tel" name="phone" pattern="[0-9]{10}" placeholder="10-digit number" 
required></td>
 </tr>
 <tr>
 <td>Course:</td>
 <td>
 <select name="course" required>
 <option value="">--Select Course--</option>
 <option value="B.Tech CSE">B.Tech CSE</option>
 <option value="B.Tech ECE">B.Tech ECE</option>
 <option value="B.Tech MECH">B.Tech MECH</option>
 <option value="B.Tech CIVIL">B.Tech CIVIL</option>
 </select>
 </td>
 </tr>
 <tr>
 <td>Address:</td>
 <td><textarea name="address" rows="4" placeholder="Enter your address" 
required></textarea></td>
 </tr>
 <tr>
 <td>Languages Known:</td>
 <td>
 <input type="checkbox" name="lang" value="English"> English
 <input type="checkbox" name="lang" value="Telugu"> Telugu
 <input type="checkbox" name="lang" value="Hindi"> Hindi
 </td>
 </tr>
 <tr>
 <td colspan="2" class="center">
 <input type="submit" value="Register">
 <input type="reset" value="Clear">
 </td>
 </tr>
 </table>
 </form>
<p id="successMsg" class="success-message"> Form submitted successfully!</p>
<script>
 const form = document.getElementById('myForm');
 const successMsg = document.getElementById('successMsg');
 form.addEventListener('submit', function(e) {
 e.preventDefault(); // Stop form from refreshing page
 successMsg.style.display = 'block'; // Show success message
 form.reset(); // Clear form fields
 });
</script>
</body>
</html>






**: frameset.html**
<!DOCTYPE html>
<html>
<head>
 <title>Frameset Example</title>
</head>
<frameset cols="33%,34%,33%">
 <frame src="image.html" name="imageFrame">
 <frame src="paragraph.html" name="textFrame">
 <frame src="link.html" name="linkFrame">
 <noframes>
 <body>
 <p>Your browser does not support frames. Please update your browser or 
 <a href="image.html">click here</a> to view the image.</p>
 </body>
 </noframes>
</frameset>
</html>







**7 Program Code**
<!DOCTYPE html>
<html lang="en">
<head>
 <meta charset="UTF-8">
 <meta name="viewport" content="width=device-width, initial-scale=1.0">
 <title>HTML5 Semantic Tags Example</title>
 <style>
 body { font-family: Arial, sans-serif; margin: 0; padding: 0; }
 header, nav, main, aside, footer { padding: 10px; }
 header { background-color: #4CAF50; color: white; text-align: center; }
 nav { background-color: #f2f2f2; }
 nav a { margin: 10px; text-decoration: none; color: #333; }
 main { display: flex; }
 article { flex: 3; padding: 15px; background-color: #fafafa; }
 aside { flex: 1; background-color: #e0e0e0; padding: 15px; }
 figure { text-align: center; }
 figcaption { font-size: 0.9em; color: #555; }
 footer { background-color: #333; color: white; text-align: center; padding: 10px; }
 </style>
</head>
<body>
 <header>
 <h1>My HTML5 Semantic Page</h1>
 <p>Using header, nav, main, article, aside, figure, and footer</p>
 </header>
 <nav>
 <a href="#">Home</a>
 <a href="#">Articles</a>
 <a href="#">Gallery</a>
 <a href="#">Contact</a>
 </nav>
 <main>
 <article>
 <h2>Welcome to Semantic HTML</h2>
 <p>Semantic tags help make web pages more meaningful and accessible. They provide context to 
browsers and assistive technologies.</p>
 
 <section>
 <h3>Benefits of Semantic HTML</h3>
 <ul>
 <li>Improves SEO</li>
 <li>Enhances accessibility</li>
 <li>Makes code cleaner</li>
 </ul>
 </section>
 <figure>
 <img src=" images /html5_logo.jpg" alt="HTML5 Logo" width="200">
 <figcaption>Figure 1: HTML5 Official Logo</figcaption>
 </figure>
 </article>
 <aside>
 <h3>Related Links</h3>
 <ul>
 <li><a href="#">HTML5 Documentation</a></li>
 <li><a href="#">W3C Standards</a></li>
 <li><a href="#">CSS Styling Tips</a></li>
 </ul>
CSE-DataScience_FSD(SEC) by KDC Page 34 of 43
 </aside>
 </main>
 <footer>
 <p>&copy; 2025 My Semantic Webpage | Designed by Student</p>
 </footer>
</body>
</html>












**8. Program Code**
<!DOCTYPE html>
CSE-DataScience_FSD(SEC) by KDC Page 36 of 43
<html lang="en">
<head>
 <meta charset="UTF-8">
 <meta name="viewport" content="width=device-width, initial-scale=1.0">
 <title>HTML5 Audio and Video Embedding</title>
 <style>
 body { font-family: Arial, sans-serif; text-align: center; padding: 20px; }
 h1 { color: #4CAF50; }
 audio, video { margin: 20px auto; display: block; }
 </style>
</head>
<body>
 <h1>HTML5 Multimedia Embedding</h1>
 <h2>Audio Example</h2>
 <audio controls>
 <source src="sample-audio.mp3" type="audio/mpeg">
 <source src="sample-audio.ogg" type="audio/ogg">
 Your browser does not support the audio element.
 </audio>
 <h2>Video Example</h2>
 <video width="480" height="270" controls poster="poster-image.jpg">
 <source src="sample-video.mp4" type="video/mp4">
 <source src="sample-video.webm" type="video/webm">
 <source src="sample-video.ogg" type="video/ogg">
 Your browser does not support the video element.
 </video>
</body>
</html>










**9 Program Code**
**HTML File: css_demo.html**
<!DOCTYPE html>
<html lang="en">
CSE-DataScience_FSD(SEC) by KDC Page 39 of 43
<head>
 <meta charset="UTF-8">
 <meta name="viewport" content="width=device-width, initial-scale=1.0">
 <title>CSS Types Example</title>
 <!-- Internal CSS -->
 <style>
 h1 {
 color: green;
 text-align: center;
 }
 p {
 font-size: 18px;
 font-family: Arial, sans-serif;
 }
 </style>
 <!-- External CSS -->
 <link rel="stylesheet" href="styles.css">
</head>
<body>
 <!-- Inline CSS -->
 <h1 style="background-color: yellow;">Welcome to CSS Styling</h1>
 <p>This paragraph is styled with internal CSS.</p>
 <div class="external-style">
 This section is styled using external CSS.
 </div>
</body>
</html>
**External CSS File: styles.css**
.external-style {
 color: white;
 background-color: navy;
 padding: 15px;
 border-radius: 8px;
 text-align: center;
}






**10 Program Code**
**HTML File: selectors_demo.html**
<!DOCTYPE html>
<html lang="en">
<head>
 <meta charset="UTF-8">
 <meta name="viewport" content="width=device-width, initial-scale=1.0">
 <title>CSS Selector Demonstration</title>
 <style>
 /* Simple Selectors */
 h1 {
 color: darkblue;
 text-align: center;
CSE-DataScience_FSD(SEC) by KDC Page 42 of 43
 }
 .highlight {
 background-color: yellow;
 }
 #main-title {
 text-transform: uppercase;
 }
 /* Combinator Selectors */
 div p { color: green; } /* Descendant */
 ul > li { color: brown; } /* Child */
 h2 + p { font-style: italic; } /* Adjacent sibling */
 h2 ~ p { background-color: #f0f0f0; } /* General sibling */
 /* Pseudo-classes */
 a:hover { color: red; }
 p:first-child { font-weight: bold; }
 input:focus { border: 2px solid blue; }
 /* Pseudo-elements */
 p::first-letter { font-size: 200%; color: purple; }
 p::after { content: " ★"; color: gold; }
 /* Attribute Selectors */
 input[type="text"] { background-color: lightyellow; }
 a[target="_blank"] { border-bottom: 2px dashed orange; }
 </style>
</head>
<body>
 <h1 id="main-title">CSS Selectors Example</h1>
 <div>
 <p>This paragraph is a descendant of a div.</p>
 <p class="highlight">This one is highlighted using a class.</p>
 </div>
 <h2>List Example</h2>
 <ul>
 <li>Item 1 (Child selector applies)</li>
 <li>Item 2</li>
 </ul>
 <p>This paragraph comes after h2 (Adjacent selector applies).</p>
 <p>Another paragraph after h2 (General sibling selector applies).</p>
 <h2>Links Example</h2>
 <a href="https://example.com" target="_blank">External Link</a> 
 <a href="page.html">Internal Link</a>
 <h2>Form Example</h2>
 <form>
 <input type="text" placeholder="Enter text here">
 <input type="password" placeholder="Password">
 </form>
</body>
</html>
