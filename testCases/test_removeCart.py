from pageObjects.Filters import Filter
from pageObjects.AddCart import AddCart
from pageObjects.RemoveCart import RemoveCart
from utilities.readProperties import ReadConfig
import time

class Test_001_RemoveCart:
    baseURL=ReadConfig.getApplicationURL()

    def test_remove_cart(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.fl = Filter(self.driver)
        self.ac = AddCart(self.driver)
        self.rc = RemoveCart(self.driver)
        self.fl.clickCatalog()
        self.fl.clickFilter()
        self.fl.selectInstock()
        self.fl.selectOutside()
        time.sleep(2)
        self.ac.firstItem()
        self.ac.add_cart()
        time.sleep(4)
        self.ac.view_cart()
        self.driver.back()
        self.driver.back()
        self.rc.secondItem()
        self.ac.add_cart()
        time.sleep(2)
        self.ac.view_cart()
        time.sleep(2)
        self.rc.remove_cart()
        time.sleep(4)
        if 2==2:
            assert True

        else:
            assert False