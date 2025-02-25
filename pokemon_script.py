import selenium.webdriver as wb
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")
options.add_argument("window-size=1400,1500")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("start-maximized")
options.add_argument("enable-automation")
options.add_argument("--disable-infobars")
options.add_argument("--disable-dev-shm-usage")

service = Service('./chromedriver')
driver = wb.Chrome(service=service, options=options)
url = "https://pokemonkorea.co.kr/pokedex"
driver.get(url)

time.sleep(1)

img = driver.find_element(By.CSS_SELECTOR, ".tumb-wrp>img")
img.click()

time.sleep(1)

tall = driver.find_element(By.CSS_SELECTOR, ".mb-3+p")
str1 = tall.text
print(str1)

with open("test.txt", "w") as file:
    file.write(str1)

driver.close()
