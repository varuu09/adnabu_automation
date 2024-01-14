from selenium.webdriver.common.by import By

class Search:

    button_search_xpath= '//*[@id="shopify-section-sections--14768207790177__header"]/div/header/details-modal/details/summary'
    textbox_search_id= 'Search-In-Modal-1'
    result_id= 'predictive-search-option-product-1'
    button_search_result_xpath='//*[@id="shopify-section-sections--14768207790177__header"]/div/header/details-modal/details/div/div[2]/predictive-search/form/div[1]/button[2]'
    text_no_result_xpath='//*[@id="shopify-section-template--14768207462497__main"]/div/div[1]/p'


    def __init__(self,driver):
        self.driver=driver

    def searchClick(self):
        self.driver.find_element(By.XPATH,self.button_search_xpath).click()

    def inputbox(self,validInput):
        self.driver.find_element(By.ID,self.textbox_search_id).send_keys(validInput)

    def result(self):
        self.driver.find_element(By.ID,self.result_id).click()

    def searchButtonClick(self):
        self.driver.find_element(By.XPATH,self.button_search_result_xpath).click()

    def noResult(self):
        a= self.driver.find_element(By.XPATH,self.text_no_result_xpath).text
        return a
