from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#Options to keep the browser window from closing after code is executed
chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach',True)

#setup the driver
"""driver=webdriver.Chrome(chrome_options)
driver.get('https://www.effortless-app.com/')
element=driver.find_element(By.CSS_SELECTOR,"p")
print(element.text)"""

#Challenge 1:- Scrape python.org for upcoming event and save as dictionary
driver=webdriver.Chrome(chrome_options)
driver.get('https://www.python.org/')
time.sleep(1)
time_elements=driver.find_elements(By.CSS_SELECTOR,'.medium-widget.event-widget.last time')
event_elements=driver.find_elements(By.CSS_SELECTOR,'.medium-widget.event-widget.last li a')
my_dict={i:{'time':time_elements[i].text,'event':event_elements[i].text} for i in range(len(time_elements))}
print(my_dict)


