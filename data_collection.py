from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("https://shnaton.huji.ac.il/index.php")

# Find the course code input and enter 80131
input_box = driver.find_element(By.NAME, "course")
input_box.send_keys("80131")
input_box.send_keys(Keys.RETURN)

# Wait for the div with class 'card' to appear
try:
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CLASS_NAME, "grid-container-wrapper"))
    )
    content = driver.page_source
    from bs4 import BeautifulSoup


    soup = BeautifulSoup(content, "html.parser")
    course_info = soup.find("div", class_="grid-container-wrapper")
    if course_info:
        days = course_info.find_all("div", class_="day")
        hours = course_info.find_all("div", class_="hour")
        del hours[0]
        print(f"Found {len(days)} days and {len(hours)} hours.")
        for day, hour in zip(days, hours):
            print(f"Day: {day.text.strip()}, Hour: {hour.text.strip()}")
    else:
        print("Not found")
finally:
    driver.quit()