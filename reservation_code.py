from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
browser = webdriver.Chrome(ChromeDriverManager().install())

#READ ME
# Here is the rundown
# When executed, this will open up a new browser window that will not have any usernames or passwords or any of your browser data
# That is why you need the login info
# The main idea with this is it uses the xpath values taken from the webpage, and follows the commands that I wouldv've done myself to make a reservation
# The time.sleep() functions are necessary after almost every click. This is what keeps the website from thinking you're a bot


# ======= Setting =============
isPresent = False
#the main webpage
browser.get('https://account.ikonpass.com/en/myaccount')
#this may work without changing
browser.find_element_by_name('email').send_keys('YOUR EMAIL HERE')
time.sleep(2)
browser.find_element_by_name('password').send_keys('YOUR PASSWORD HERE')
time.sleep(2)
#all xpath variables will need to be changed, this one was the login button. the .click() is to actually click lol
browser.find_element_by_xpath('//*[@id="scrolling-body"]/section/div/div/div/div[1]/div/div/div[1]/div/form/button').click()
time.sleep(2)
while not isPresent:
    #this will loop until a reservation is found. I don't know how the Eldora website works, but below is the main idea
    #you will use the xpath and .click() function to navigate to the reservation page
    #then you will click or do whatever on the date that you want a reservation
    #if the reservation is open, the loop will exit. Otherwise, it will restart the loop by refreshing the page and starting over
    # Open the Website
    browser.get('https://account.ikonpass.com/en/myaccount')
    time.sleep(30)
    # Make reservation button
    browser.find_element_by_xpath('//*[@id="root"]/div/div/main/section[1]/div/div[3]/div/a').click()
    time.sleep(1)
    #select resort (winter park)
    browser.find_element_by_xpath('//*[@id="react-autowhatever-resort-picker-section-0-item-2"]').click()
    time.sleep(1)
    #hit continue
    browser.find_element_by_xpath('//*[@id="root"]/div/div/main/section[2]/div/div[2]/div[2]/div[2]/button').click()
    #select dec 27th
    time.sleep(1)
    browser.find_element_by_xpath('//*[@id="root"]/div/div/main/section[2]/div/div[2]/div[3]/div[1]/div[1]/div[1]/div/div[2]/div/div[2]/div[5]/div[1]').click()
    if (len(browser.find_elements_by_xpath('//*[@id="root"]/div/div/main/section[2]/div/div[2]/div[3]/div[1]/div[2]/div/div[4]/button[1]')) > 0):
        isPresent = True
    time.sleep(2)
#here is the code to make the reservation. I was able to determine the xpaths by going through the process of making a rez on a day that wasn't fully booked

browser.find_element_by_xpath('//*[@id="root"]/div/div/main/section[2]/div/div[2]/div[3]/div[1]/div[2]/div/div[4]/button[1]').click()
time.sleep(3)
browser.find_element_by_xpath('//*[@id="root"]/div/div/main/section[2]/div/div[2]/div[3]/div[2]/button').click()
time.sleep(3)
browser.find_element_by_xpath('//*[@id="root"]/div/div/main/section[2]/div/div[2]/div[4]/div/div[4]/label/input').click()
time.sleep(3)
browser.find_element_by_xpath('//*[@id="root"]/div/div/main/section[2]/div/div[2]/div[4]/div/div[5]/button').click()
time.sleep(3)
browser.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')
#it opens celebrate good times when a reservation is found, so that you can leave it running and when it works this will pop up :)
browser.get('https://www.youtube.com/watch?v=3GwjfUFyY6M&ab_channel=KoolAndTheGangVEVO')