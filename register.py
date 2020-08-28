from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("chromedriver.exe")
driver.get("https://store.unionlosangeles.com/account/login")

first_name = "First"
last_name = "Last"
email = "email@gmail.com"
password = "Password"
address = "123 Test Lane"
city = "City"
province = "State"
zip_code = "12345"
phone = "1231231234"

passInput = driver.find_element_by_name('customer[first_name]')
passInput.send_keys(first_name)

passInput = driver.find_element_by_name('customer[last_name]')
passInput.send_keys(last_name)

passInput = driver.find_element_by_xpath('//*[@id="signup_email"]')
passInput.send_keys(email)

passInput = driver.find_element_by_xpath('//*[@id="signup_password"]')
passInput.send_keys(password)

passInput = driver.find_element_by_xpath('//*[@id="create_customer"]/div[5]/input')
passInput.send_keys(Keys.RETURN)
