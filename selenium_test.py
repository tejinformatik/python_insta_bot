from selenium import webdriver
from time import sleep

if __name__ == '__main__':
    browser = webdriver.Chrome (executable_path =".\\chromedriver.exe")
    browser.get("https://www.instagram.com/")
    cookies = browser.find_element_by_xpath(("//button[class= \"aOOlW  bIiDR  \"]"))
    cookies.click()
    
