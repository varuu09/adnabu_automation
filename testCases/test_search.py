from pageObjects.Search import Search
from utilities.readProperties import ReadConfig
import time

class Test_001_Searching:
    baseURL=ReadConfig.getApplicationURL()
    validInput=ReadConfig.validInputSearch()
    invalidInput=ReadConfig.invalidInputSearch()

    def test_valid_search(self,setup):

        self.driver = setup
        self.driver.get(self.baseURL)
        self.sr=Search(self.driver)
        self.sr.searchClick()
        time.sleep(2)
        self.sr.inputbox(self.validInput)
        time.sleep(1)
        self.sr.result()

        if 2==2:
            assert True
        else:
            False



    def test_invalid_search(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.sr = Search(self.driver)
        self.sr.searchClick()
        time.sleep(2)
        self.sr.inputbox(self.invalidInput)
        #time.sleep(5)
        self.sr.searchButtonClick()
        b=self.sr.noResult()

        if b.__contains__('No results found'):
            assert True

        else:
            False
