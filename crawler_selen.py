
from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome('/Users/SKTelecom/Documents/GitHub/RM_ChatBot/chromedriver_win32/chromedriver.exe')
driver.implicitly_wait(3)
driver.get('https://nid.naver.com/nidlogin.login')
driver.find_element_by_name('id').send_keys('1996yyk')
driver.find_element_by_name('pw').send_keys('-')
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
driver.get('https://order.pay.naver.com/home')

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
notices = soup.select('div.p_inr > div.p_info > a > span')

for n in notices:
    print(n.text.strip())