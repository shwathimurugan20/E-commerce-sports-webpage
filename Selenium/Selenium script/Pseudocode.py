from selenium import webdriver


driver = webdriver.Chrome()


driver.get("file:///C:/Users/Shwa/OneDrive/Desktop/for%20you/web/trial%20website/index.html")


try:
   
    heading = driver.find_element_by_css_selector("h1")
    assert heading.text == "Welcome to My E-commerce webpage"

    name_input = driver.find_element_by_id("name")
    name_input.send_keys("John Doe")

    email_input = driver.find_element_by_id("email")
    email_input.send_keys("john.doe@example.com")

    submit_button = driver.find_element_by_id("submit")
    submit_button.click()

 
    success_message = driver.find_element_by_id("success-message")
    assert success_message.text == "Form submitted successfully!"

   

except Exception as e:
    print("Test failed:", str(e))

# Close the web browser
driver.quit()
