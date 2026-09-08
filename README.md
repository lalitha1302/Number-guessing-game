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
CSE-DataScience_FSD(SEC) by KDC Page 22 of 43
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
CSE-DataScience_FSD(SEC) by KDC Page 33 of 43
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
