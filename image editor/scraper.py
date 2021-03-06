#Selenium imports here
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import os,time
import wget

driver=webdriver.Chrome('path to chromedriver.exe')
driver.get('https://www.instagram.com/')
username=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))#select the username and password fields and fill themn
password=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))
username.clear()
password.clear()
username.send_keys("")
password.send_keys("")
login=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button[type='submit']"))).click()#click login button
not_now=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))).click()#click not now button
search=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search']")))#find the search bar
search.clear()
keyword='#hashtagyouwanttoscrape'
search.send_keys(keyword)
z=True
while z:#search for the hashtag
    try:
        search.send_keys(u'\ue007')
    except:
        z=False

driver.execute_script("window.scrollTo(0,4000);")#scroll and scrape images from the hashtag and save them to the path
time.sleep(10)
images = driver.find_elements_by_tag_name('img')
images = [image.get_attribute('src') for image in images]
#temp=[]
#for image in images:
 #   temp.append(image.get_attribute('src'))
#images = images[:-2] #slicing-off IG logo and Profile pictureprint(‘Number of scraped images: ‘, len(images))
print(images)
path=os.getcwd()
path=os.path.join(path, keyword[1:])
os.mkdir(path)
counter=0
for image in images:
    save_as=os.path.join(path,keyword[1:]+ str(counter)+'.jpg')
    wget.download(image, save_as)
    counter=counter+1
