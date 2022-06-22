from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait

#Make Sure After the Browser wait few Second you need to Hit The First Like then the script will do the rest
driver = webdriver.Chrome('')#Add you chrome driver Path here
driver.get('https://tinder.com/app/recs')
driver.implicitly_wait(20)
try:
    login = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,'//*[@id="o-654199900"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/span'))
    )
finally:
    print("we couldnt find it .. ")
login.click()
sleep(2)
fb_login = driver.find_element(By.XPATH,'//*[@id="o1912386320"]/div/div/div[1]/div/div/div[3]/span/div[2]/button/span[2]')
fb_login.click()

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

email = driver.find_element(By.XPATH,'//*[@id="email"]')
password = driver.find_element(By.XPATH,'//*[@id="pass"]')
email.send_keys(" ")#enter your email here
password.send_keys(' ')#enter your password here
password.send_keys(Keys.ENTER)

sleep(3)

driver.switch_to.window(base_window)
print(driver.title)

sleep(5)
allow_location_button = driver.find_element(By.XPATH,'//*[@id="o1912386320"]/div/div/div/div/div[3]/button[1]/span')
allow_location_button.click()
notifications_button = driver.find_element(By.XPATH,'//*[@id="o1912386320"]/div/div/div/div/div[3]/button[1]/span')
notifications_button.click()
cookies = driver.find_element(By.XPATH,'//*[@id="o-654199900"]/div/div[2]/div/div/div[1]/div[2]/button')
cookies.click()

while True:
    #Add a 2 second delay between likes.
    sleep(2)
    try:
        like_button = driver.find_element(By.XPATH, '//*[@id="o-654199900"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[5]/div/div[4]/button')
        like_button.click()
        print("clicked")
        if driver.find_element(By.XPATH,'//*[@id="o-654199900"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[5]/div/div[4]/button') == None:
            driver.quit()
    # Catches the cases where there is a "Matched" pop-up  and the "Ads" in front of the "Super Like" button:
    except Exception as e:
        try:
            match_popup = driver.find_element(By.XPATH,'//*[@id="o1912386320"]/div/div/div[2]/button[2]')
            match_popup.click()
            continue
        except Exception as e:
            print(type(e), 'match pop up problem')
            print("its not the match pop_up ")
        try:
            driver.find_element(By.XPATH, '//*[@id="o1912386320"]/div/div/button[2]').click()
            super_like_popup = driver.find_element(By.XPATH, '//*[@id="o1912386320"]/div/div/button[2]/span')
            super_like_popup.click()
            continue
        except Exception as e:
            print(type(e),'like pop up problem')
            print("its not the super like pop_up")
