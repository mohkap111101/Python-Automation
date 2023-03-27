from selenium import webdriver

driver = webdriver.Chrome()
url = 'https://www.seleniumeasy.com/test/basic-first-form-demo.html'
driver.get(url)

messageField = driver.find_element_by_xpath('//*[@id="user-message"]')
messageField.send_keys('This is a test message')

showMessageButton = driver.find_element_by_xpath('//*[@id="get-input"]/button')
showMessageButton.click()
