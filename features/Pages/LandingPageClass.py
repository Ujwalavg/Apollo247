from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class LandingPageClass:

 def __init__(self, driver):
    self.driver = driver
    # Element Locators Values
    self.Laterbutton = "//*[@id='wzrk-cancel']"
    self.PharmacyLink = "//*[text()='Medicines & other products']"
    self.ApolloProduct = "//a[@href='/shop-by-category/apollo-products']"
    self.PersonalCare = "//a[@href='/shop-by-category/apollo-personal-care']"

 # Creating Element Methods
 def click_Later_button(self):
    Later_button=self.driver.find_element(By.XPATH, self.Laterbutton)
    Later_button.click()

 def click_Pharmacy_Link(self):
        Pharamacy_Link=self.driver.find_element(By.XPATH,self.PharmacyLink)
        Pharamacy_Link.click()

 def mouse_hover(self):
     mousehover = self.driver.find_element(By.XPATH, self.ApolloProduct)
     action = ActionChains(self.driver)
     action.move_to_element(mousehover)
     action.perform()


 def click_PersonalCare(self):
        PersonalCare=self.driver.find_element(By.XPATH,self.PersonalCare)
        PersonalCare.click()

