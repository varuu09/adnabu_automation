# Roadmap/Documentation of AdNabu Automation Framework


Framework:
> Pytest (Python UnitTest Framework) using Page object model (POM)

### Installing Packages:

####Python
> pip install python

####Selenium
Selenium libraries
> pip install selenium

####Pytest
Python unittest framework
> pip install pytest

####Pytest-html
HTML Reports
> pip install pytest-html

####Pytest-xdist
 Run Test case parallelly 
> pip install pytest-xdist

###Folders Structure-
- pageObjects
- testCases
- utilities
- Configurations

####pageObjects
- Creating pageObject class
- Adding Locators of every element
 
####testCases
- Implementing test case of Page Object Class
- Conftest File- Adding common Fixture for all Test Cases (Webdriver)

####utilities
- readProperties utility file to read common data  (login credentials, URL etc)

####Configurations
- ini file- config.ini for Common value (login credentials, URL etc)

####Reports-
>–html=Reports.html 

####Run Test case parallelly-
>-n 3 (3= no of execution)

####Running Test case-
>pytest -v -s -n 3 --html=Report.html /testCases 

###Future scope- 
- Run Test case on any browser
- Adding Logs
- Adding screenshot
- Signup (random function for email)
- Login
- Checkout
- Allure Reports


Cases- https://docs.google.com/document/d/1LiLD1qZSJyfGSLRZIEzqrNScMNQeFDG7cbuu5TesbLQ/edit?usp=sharing