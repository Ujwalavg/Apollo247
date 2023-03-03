from selenium.webdriver.common.by import By


class PersonalCarePageClass:


    def __init__(self, driver):
        self.driver = driver
        # Element Locators Values
        self.SpecialOffersbutton="//p[@class='CategoryListing_txt__A9aqn']"
        self.SelectLocation="//div[@id='__next']/header/div/div/div/div/div/div"
        self.deliveryPincode="//*[@id='fixedHeaderCT']/div/div/div[1]/div/div/div[2]/div[3]/p"
        self.enterpincodeplaceholder="//input[@placeholder='Enter pincode here']"
        self.Submitbutton="//div[@class='LocationSearch_bottomActions__oWEfA']/button"
        self.showsthedeliverycode="//*[text()='Uppalapadu 518002']"
        self.errormessage="//*[text()='Sorry, we are not servicing in your area currently. Call 1860 500 0101 for pharmacy store nearby.']"
        self.specialofferelement="//*[text()='25% Flat Discount on first three purchase on medicine Order of Rs.800 & above']"
        self.location="//*[@id='fixedHeaderCT']/div/div/div[1]/div/div"

    #creating elements

    def click_SpecialOffers(self):
        SpecialOffers=self.driver.find_element(By.XPATH,self.SpecialOffersbutton)
        SpecialOffers.click()


    def click_SelectLocation(self):
        SelectLocation=self.driver.find_element(By.XPATH,self.SelectLocation)
        SelectLocation.click()

    def click_deliveryPincode(self):
        deliveryPincode=self.driver.find_element(By.XPATH,self.deliveryPincode)
        deliveryPincode.click()
    def enter_pincode(self,upincode):
        enterpincode=self.driver.find_element(By.XPATH,self.enterpincodeplaceholder)
        enterpincode.send_keys(upincode)

    def click_submitbutton(self):
        submitbutton=self.driver.find_element(By.XPATH,self.Submitbutton)
        submitbutton.click()

    def check_User_pincode(self):
        showpincode=self.driver.find_element(By.XPATH,self.showsthedeliverycode).text
        return showpincode
    def check_error_message(self):
        showerror=self.driver.find_element(By.XPATH,self.errormessage).text
        return showerror
    def check_specialoff_text(self):
        specialofferstext=self.driver.find_element(By.XPATH,self.specialofferelement).text
        return specialofferstext

    def click_loaction_update(self):
        locationupadate=self.driver.find_element(By.XPATH,self.location)
        locationupadate.click()




