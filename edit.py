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

passInput = driver.find_element_by_xpath('//*[@id="customer_email"]')
passInput.send_keys(email)

passInput = driver.find_element_by_xpath('//*[@id="customer_password"]')
passInput.send_keys(password)

passInput = driver.find_element_by_xpath('//*[@id="customer_login"]/div[3]/input')
passInput.send_keys(Keys.RETURN)

driver.get("https://store.unionlosangeles.com/account/addresses")

passInput = driver.find_element_by_xpath('//*[@id="action"]/a')
passInput.send_keys(Keys.RETURN)

passInput = driver.find_element_by_xpath('//*[@id="address_first_name_new"]')
passInput.send_keys(first_name)

passInput = driver.find_element_by_xpath('//*[@id="address_last_name_new"]')
passInput.send_keys(last_name)

passInput = driver.find_element_by_xpath('//*[@id="address_address1_new"]')
passInput.send_keys(address)

passInput = driver.find_element_by_xpath('//*[@id="address_city_new"]')
passInput.send_keys(city)

passInput = driver.find_element_by_xpath('//*[@id="address_province_new"]')
passInput.send_keys(province)

passInput = driver.find_element_by_xpath('//*[@id="address_zip_new"]')
passInput.send_keys(zip_code)

passInput = driver.find_element_by_xpath('//*[@id="address_phone_new"]')
passInput.send_keys(phone)

passInput = driver.find_element_by_xpath('//*[@id="address_default_address_new"]')
passInput.click()

passInput = driver.find_element_by_xpath('//*[@id="address_form_new"]/div/input')
passInput.send_keys(Keys.RETURN)