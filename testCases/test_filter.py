import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.Filters import Filter
from utilities.readProperties import ReadConfig

import time

class Test_001_Filter:
    baseURL = ReadConfig.getApplicationURL()

    def test_filter(self,setup):

        self.driver = setup
        self.driver.get(self.baseURL)
        self.fl=Filter(self.driver)
        self.fl.clickCatalog()
        self.fl.clickFilter()
        self.fl.selectInstock()
        self.fl.selectOutside()
        time.sleep(2)

        current_url=self.driver.current_url
        if current_url==self.baseURL+'/collections/all?filter.v.availability=1&sort_by=title-ascending':
            assert True

        else:
            assert False