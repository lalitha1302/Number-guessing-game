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
