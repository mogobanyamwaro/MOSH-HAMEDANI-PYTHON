from selenium import webdriver


browser = webdriver.Chrome()
browser.get("https://github.com")
signin_link=browser.find_element_by_link_text("sign in")
signin_link.click();


username_box = browser.find_element_by_id("login_field")
username_box.send_keys("ninjacoder22")

password_box = browser.find_element_by_id("password")
password_box.send_keys("1234578")
password_box.submit()

assert "ninjacoder22" in browser.page_source

profile_link = browser.find_element_by_class_name('user-profile-link')
link_label = profile_link.get_attribute("innerHTML")
assert "ninjacoder22" in link_label




browser.quit()



