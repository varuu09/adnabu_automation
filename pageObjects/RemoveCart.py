from selenium.webdriver.common.by import By

class RemoveCart:
    button_second_item_xpath='//*[@id="product-grid"]/li[2]/div'
    button_remove_cart_id='Remove-1'

    def __init__(self,driver):
        self.driver=driver

    def secondItem(self):
        self.driver.find_element(By.XPATH,self.button_second_item_xpath).click()

    def remove_cart(self):
        self.driver.find_element(By.ID,self.button_remove_cart_id).click()

