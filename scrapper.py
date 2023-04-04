from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import csv
from getpass import getpass
from selenium.webdriver.common.keys import Keys 
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

chrome_driver_path = "D:\Selenium\chromedriver.exe"

service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.get("https://www.twitter.com/login")

wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input")))
username=driver.find_element("xpath",'/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
time.sleep(2)
username.send_keys('email')
username.send_keys(Keys.RETURN)


element=wait.until(EC.presence_of_all_elements_located((By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')))
sendUser=driver.find_element("xpath",'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
time.sleep(2)
sendUser.send_keys('username')
sendUser.send_keys(Keys.RETURN)

element = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")))
password=driver.find_element("xpath",'/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
time.sleep(2)
password.send_keys('password')
password.send_keys(Keys.RETURN)

time.sleep(5)

element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div/label/div[2]/div/input')))
search=driver.find_element("xpath",'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div/label/div[2]/div/input')
search.send_keys('mongodb')
search.send_keys(Keys.RETURN)

time.sleep(5)

driver.find_element(By.LINK_TEXT, "People").click()
# data=[]

time.sleep(2)

last_position=driver.execute_script("return window.pageYOffset;")
# scroll=True
total_count=0
tweet_data=[]

while True:
    cards=driver.find_elements(By.XPATH,'//div[@data-testid="UserCell"]/div')
    time.sleep(2)
    count=0
        
    for card in cards:
        if(count%5==0):
            time.sleep(3)
        try:
            if(card.find_element(By.XPATH,'./div[2]/div[1]/div/div/div[2]//span') and card.find_element(By.XPATH,'./div[2]/div[2]/span')):
                print(card.find_element(By.XPATH,'./div[2]/div[1]/div/div/div[2]//span').text)
                user=card.find_element(By.XPATH,'./div[2]/div[1]/div/div/div[2]//span').text
                
                spans=card.find_elements(By.XPATH,'./div[2]/div[2]/span')
                bio=""
                for span in spans:
                    print(span.text)
                    bio+=span.text
                
                tweet=(user,bio)
                tweet_data.append(tweet)
                count+=1
                print("\n")

        except:
            print("Not Found")
    
    print(count)
    total_count+=count
    print(total_count)
    # scroll_attempt=0
    # while True:
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
    time.sleep(2)
    if(total_count>=400):
        break
        # curr_position=driver.execute_script("return window.pageYOffset;")
        # if last_position== curr_position:
        #     scroll_attempt+=1

        #     if scroll_attempt>=3:
        #         scroll=False
        #         break
        #     else:
        #         time.sleep(2)
        # else:
        #     last_position=curr_position
        #     break

with open('datav.scv','w',newline='',encoding='utf-8') as f:
    header=['Username','bio']
    writer=csv.writer(f)
    writer.writerow(header)
    writer.writerows(tweet_data)


driver.quit()  # Close the Chrome window


