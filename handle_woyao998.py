import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
test_webdriver = webdriver.Chrome(chrome_options=chrome_options)
test_webdriver.maximize_window()
test_webdriver.get('http://old.woyao998.com/')
test_webdriver.find_element_by_xpath('//input[@id="username"]').send_keys('youcom')
test_webdriver.find_element_by_xpath('//input[@id="password"]').send_keys('0591chen')
test_webdriver.find_element_by_xpath('//img[@class="captcha"]')
captcha = input('请输入验证码：')
test_webdriver.find_element_by_xpath('//input[@id="verify"]').send_keys(captcha)
time.sleep(5)
test_webdriver.find_element_by_xpath('//div[@class="form-group"]//button[@type="submit"]').click()
time.sleep(5)
test_webdriver.get('http://www.woyao998.com/surf.html')
time.sleep(5)
i = 0
while True:
    try:
        el = test_webdriver.find_element_by_xpath('//tr[1]//a[@class="task_detail"]')
        if el:
            i += 1
            el.click()
            print(i)
            time.sleep(50)
            test_webdriver.get('http://www.woyao998.com/surf.html')
            time.sleep(5)
            continue
        else:
            break
    except Exception as e:
        print(e)
        break
test_webdriver.quit()