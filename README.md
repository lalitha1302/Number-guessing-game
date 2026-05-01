#  Number Guessing Game (Python)
-using nummpy skills

##  Overview
This is a simple and fun, **Number Guessing Game** implemented in Python.  
The program generates a random number between **1 and 100**, and the player has to guess it.  
After each guess, the program provides feedback:
- `"too low!"` if the guess is smaller than the number
- `"too high!"` if the guess is larger than the number
- `"Correct!"` when the player guesses the number correctly  

It also tracks the number of attempts taken to guess the correct number.

---

## 🛠️ Features
- Random number generation using **NumPy**
- Interactive user input
- Feedback after each guess
- Tracks number of attempts until success

---

## How to Run
1. Make sure you have **Python 3.x** installed.
2. Install NumPy if not already installed:
   ```bash
   pip install numpy

**selenium python script to open facebook**
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize the browser
driver = webdriver.Chrome()

# Open the login page of your target site
driver.get("https://facebook.com/login")
time.sleep(15)

# Find the username and password fields
username_box = driver.find_element(By.NAME, "username")
password_box = driver.find_element(By.NAME, "password")

# Enter credentials
username_box.send_keys("your_username")
password_box.send_keys("your_password")

# Submit the form
password_box.send_keys(Keys.RETURN)

# Wait for a while to see the result
time.sleep(300)

# Close the browser
driver.quit()


******python script for google web elements**
**


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize the Chrome driver (make sure chromedriver is installed and in PATH)
driver = webdriver.Chrome()

# Open Google homepage
driver.get("https://www.google.com")
time.sleep(300)
driver.maximize_window()

# Example 1: Locate the search box by its name attribute
search_box = driver.find_element(By.NAME, "q")
print("Search box tag name:", search_box.tag_name)
print("Search box is displayed:", search_box.is_displayed())

# Example 2: Inspect attributes of the search box
print("Search box 'title' attribute:", search_box.get_attribute("title"))
print("Search box 'aria-label' attribute:", search_box.get_attribute("aria-label"))

# Example 3: Locate and inspect the 'Google Search' button
search_button = driver.find_element(By.NAME, "btnK")
print("Search button text:", search_button.get_attribute("value"))
print("Search button is enabled:", search_button.is_enabled())

# Example 4: Locate and inspect the 'Images' link
images_link = driver.find_element(By.LINK_TEXT, "Images")
print("Images link href:", images_link.get_attribute("href"))
print("Images link is displayed:", images_link.is_displayed())

# Pause to visually confirm
time.sleep(5)

# Close the browser
driver.quit()
