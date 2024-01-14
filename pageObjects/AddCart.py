from selenium.webdriver.common.by import By

class AddCart:
    button_first_item_xpath= '//*[@id="product-grid"]/li[1]/div'
    button_add_to_cart_id= 'ProductSubmitButton-template--14768207495265__main'
    button_view_cart_id = 'cart-icon-bubble'

    def __init__(self,driver):
        self.driver=driver

    def firstItem(self):
        self.driver.find_element(By.XPATH,self.button_first_item_xpath).click()

    def add_cart(self):
        self.driver.find_element(By.ID,self.button_add_to_cart_id).click()

    def view_cart(self):
        self.driver.find_element(By.ID, self.button_view_cart_id).click()