from pageObjects.Filters import Filter
from pageObjects.AddCart import AddCart
from utilities.readProperties import ReadConfig
import time

class Test_001_AddCart:
    baseURL=ReadConfig.getApplicationURL()

    def test_add_cart(self,setup):

        self.driver = setup
        self.driver.get(self.baseURL)
        self.fl=Filter(self.driver)
        self.ac=AddCart(self.driver)
        self.fl.clickCatalog()
        self.fl.clickFilter()
        self.fl.selectInstock()
        self.fl.selectOutside()
        time.sleep(2)
        self.ac.firstItem()
        self.ac.add_cart()
        time.sleep(2)
        self.ac.view_cart()
        time.sleep(5)
        current_url=self.driver.current_url
        if current_url==self.baseURL+'/cart':
            assert True

        else:
            assert False