from selenium import webdriver
import time
import sys
import requests
chrome_path = r'//usr/local/bin/chromedriver'
stringToMatch = 'input id'
browser = webdriver.Chrome()
type(browser)
file = open("source_output.txt", "r+")
file.truncate(0)
file = open("extract.txt", "r+")
file.truncate(0)
file = open("final.txt", "r+")
file.truncate(0)
file.close()
browser.get('https://knowmax3.ultimatix.net/sites/it_is-hsd/RIO/Lists/RiO%20Pledge%20%20SBWS%20Mode/NewForm.aspx')

time.sleep(20)
html = browser.page_source
sys.stdout = open('source_output.txt', 'w')
print(html)


stringToMatch = 'input id'
with open('source_output.txt', 'r') as file:
    for line in file:
        if stringToMatch in line:
            #print(line)
            firstdelimit = line.find("id=")
            lastdelimit  = line.find("type")
            extract = line[firstdelimit+4:lastdelimit-2]
            #print(extract)
            sys.stdout = open('extract.txt', 'a')
            print(extract)

with open('extract.txt', 'r')  as file:
  for line in file:
    format_line = line.strip()
    sys.stdout = open('final.txt', 'a')
    browser.find_element_by_xpath(f"//input[@id='{format_line}']").click()
    browser.find_element_by_xpath("//input[@value='Finish']").click()
