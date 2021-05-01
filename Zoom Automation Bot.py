from selenium import webdriver
import time
import keyboard
import datetime

x = datetime.datetime.now()
            
# Change <BROWSER NAME> according to your browser
driver_path = r"Your_Driver_Path"
browser = webdriver.<BROWSER NAME>(executable_path=driver_path)

# Days (Not change) 
day1 = "Monday"
day2 = "Tuesday"
day3 = "Wednesday"
day4 = "Thursday"
day5 = "Friday"

# Lesson Times (You can Add or Remove according to your lessons)
lesson1 = "xx:xx:xx"
lesson2 = "xx:xx:xx"
lesson3 = "xx:xx:xx"
lesson4 = "xx:xx:xx"
lesson5 = "xx:xx:xx"
lesson6 = "xx:xx:xx"
lesson7 = "xx:xx:xx"
lesson8 = "xx:xx:xx"

# Lesson Names and Links (You can Add or Remove according to your lessons)
lesname1 = ("Zoom-link")
lesname2 = ("Zoom-link")
lesname3 = ("Zoom-link")
lesname4 = ("Zoom-link")
lesname5 = ("Zoom-link")
lesname6 = ("Zoom-link")
lesname7 = ("Zoom-link")
lesname8 = ("Zoom-link")

def open_lesson():
        time.sleep(2)
        keyboard.press_and_release('esc')
        time.sleep(8)
        log_in = browser.find_element_by_xpath("//*[@id='zoom-ui-frame']/div[2]/div/div[1]/div/div")
        log_in.click()
        time.sleep(1)
        keyboard.press_and_release('left')
        keyboard.press_and_release('enter')
        time.sleep(8)
        browser.close()  

# Customize "lesnameX" according to your lesson time table
while True:
    an = datetime.datetime.now()
    hour = datetime.datetime.strftime(an, '%X')
    if hour == lesson1 and day1 == x.strftime("%A"):
            browser.get(lesnameX)
            open_lesson()
            break

    elif hour == lesson2 and day1 == x.strftime("%A"):
            browser.get(lesnameX)
            open_lesson()
            break

    elif hour == lesson3 and day1 == x.strftime("%A"):
            browser.get(lesnameX)
            open_lesson()
            break

    elif hour == lesson4 and day1 == x.strftime("%A"):
            browser.get(lesnameX)
            open_lesson()
            break

    elif hour == lesson5 and day1 == x.strftime("%A"):
            browser.get(lesnameX)
            open_lesson()
            break

    elif hour == lesson6 and day1 == x.strftime("%A"):
            browser.get(lesnameX)
            open_lesson()
            break

    elif hour == lesson7 and day1 == x.strftime("%A"):
            browser.get(lesnameX)
            open_lesson()
            break

    elif hour == lesson8 and day1 == x.strftime("%A"):
            browser.get(lesnameX)
            open_lesson()
            break

    elif hour == lesson1 and day2 == x.strftime("%A"):
            browser.get(lesnameX)
            open_lesson()
            break

    elif hour == lesson2 and day2 == x.strftime("%A"):
            browser.get(lesnameX)
            open_lesson()
            break

    elif hour == lesson3 and day2 == x.strftime("%A"):
            browser.get(lesnameX)
            open_lesson()
            break

    elif hour == lesson4 and day2 == x.strftime("%A"):
            browser.get(lesnameX)
            open_lesson()
            break

    elif hour == lesson5 and day2 == x.strftime("%A"):
            browser.get(lesnameX)
            open_lesson()
            break

    elif hour == lesson6 and day2 == x.strftime("%A"):
            browser.get(lesnameX)
            open_lesson()
            break

    elif hour == lesson7 and day2 == x.strftime("%A"):
            browser.get(lesnameX)
            open_lesson()
            break

    elif hour == lesson8 and day2 == x.strftime("%A"):
            browser.get(lesnameX)
            open_lesson()
            break

    elif hour == lesson1 and day3 == x.strftime("%A"):
            browser.get(lesnameX)
            open_lesson()
            break

    elif hour == lesson2 and day3 == x.strftime("%A"):
            browser.get(lesnameX)
            open_lesson()
            break

    elif hour == lesson3 and day3 == x.strftime("%A"):
            browser.get(lesnameX)
            open_lesson()
            break

    elif hour == lesson4 and day3 == x.strftime("%A"):
            browser.get(lesnameX)
            open_lesson()
            break

    elif hour == lesson5 and day3 == x.strftime("%A"):
            browser.get(lesnameX)
            open_lesson()
            break

    elif hour == lesson6 and day3 == x.strftime("%A"):
            browser.get(lesnameX)
            open_lesson()
            break

    elif hour == lesson7 and day3 == x.strftime("%A"):
            browser.get(lesnameX)
            open_lesson()
            break

    elif hour == lesson8 and day3 == x.strftime("%A"):
            browser.get(lesnameX)
            open_lesson()
            break

    elif hour == lesson1 and day4 == x.strftime("%A"):
            browser.get(lesnameX)
            open_lesson()
            break

    elif hour == lesson2 and day4 == x.strftime("%A"):
            browser.get(lesnameX)
            open_lesson()
            break

    elif hour == lesson3 and day4 == x.strftime("%A"):
            browser.get(lesnameX)
            open_lesson()
            break

    elif hour == lesson4 and day4 == x.strftime("%A"):
            browser.get(lesnameX)
            open_lesson()
            break

    elif hour == lesson5 and day4 == x.strftime("%A"):
            browser.get(lesnameX)
            open_lesson()
            break

    elif hour == lesson6 and day4 == x.strftime("%A"):
            browser.get(lesnameX)
            open_lesson()
            break

    elif hour == lesson7 and day4 == x.strftime("%A"):
            browser.get(lesnameX)
            open_lesson()
            break

    elif hour == lesson8 and day4 == x.strftime("%A"):
            browser.get(lesnameX)
            open_lesson()
            break

    elif hour == lesson1 and day5 == x.strftime("%A"):
            browser.get(lesnameX)
            open_lesson()
            break

    elif hour == lesson2 and day5 == x.strftime("%A"):
            browser.get(lesnameX)
            open_lesson()
            break

    elif hour == lesson3 and day5 == x.strftime("%A"):
            browser.get(lesnameX)
            open_lesson()
            break

    elif hour == lesson4 and day5 == x.strftime("%A"):
            browser.get(lesnameX)
            open_lesson()
            break

    elif hour == lesson5 and day5 == x.strftime("%A"):
            browser.get(lesnameX)
            open_lesson()
            break

    elif hour == lesson6 and day5 == x.strftime("%A"):
            browser.get(lesnameX)
            open_lesson()
            break

    elif hour == lesson7 and day5 == x.strftime("%A"):
            browser.get(lesnameX)
            open_lesson()
            break

    elif hour == lesson8 and day5 == x.strftime("%A"):
            browser.get(lesnameX)
            open_lesson()
            break
    else:
        pass
