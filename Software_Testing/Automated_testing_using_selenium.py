from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())


driver.get("https://www.opencart.com/index.php?route=account/login")  


username_field = driver.find_element(By.NAME, "username")  
password_field = driver.find_element(By.NAME, "password")  


username_field.send_keys("test_user")  
password_field.send_keys("test_pass")    


username = username_field.get_attribute('value')
password = password_field.get_attribute('value')

print(f"Username: {username}")
print(f"Password: {password}")


driver.quit()