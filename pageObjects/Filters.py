import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

class Filter:

    button_catalog_id= 'HeaderMenu-catalog'
    button_filter_id= 'Details-1-template--14768207265889__main-collection-product-grid'
    dropdown_instock_xpath= '//*[@id="Facet-1-template--14768207265889__main-collection-product-grid"]/fieldset/ul[1]/li[1]'
    button_availability_id= 'Details-1-template--14768207265889__main-collection-product-grid'

    def __init__(self,driver):
        self.driver=driver

    def clickCatalog(self):
        self.driver.find_element(By.ID,self.button_catalog_id).click()

    def clickFilter(self):
        self.driver.find_element(By.ID,self.button_filter_id).click()

    def selectInstock(self):
        self.driver.find_element(By.XPATH,self.dropdown_instock_xpath).click()

    def selectOutside(self):
        self.driver.find_element(By.ID,self.button_availability_id).click()




