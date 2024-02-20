from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Open YouTube
driver.get("https://www.youtube.com")

# Wait for a few seconds to see the result
time.sleep(2)

# Find the search box and enter a search query
search_box = driver.find_element("name", "search_query")
search_box.send_keys("Python tutorial")
search_box.send_keys(Keys.RETURN)

# Wait for search results to load
time.sleep(3)

# Click on the first video in the search results
first_video = driver.find_element("xpath", '//*[@id="dismissable"]/div/div[1]/a/h3/span')
first_video.click()

# Wait for the video to load
time.sleep(5)

# Perform additional actions, such as liking the video or subscribing (if you have a YouTube account)

# Close the browser
driver.quit()
