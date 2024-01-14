import configparser

config=configparser.RawConfigParser()
config.read('/Users/varuntanwar/PycharmProjects/adnabu/Configurations/config.ini')

class ReadConfig:

    @staticmethod
    def getApplicationURL():
        url=config.get("common info", "baseURL")
        return url

    @staticmethod
    def validInputSearch():
        validInput=config.get("common info","validInput")
        return validInput

    @staticmethod
    def invalidInputSearch():
        invalidInput=config.get("common info", "invalidInput")
        return invalidInput
