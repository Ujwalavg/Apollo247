from selenium.webdriver.common.by import By

class ProductPageClass:

    def __init__(self, driver):
        # Element Locators Values
        self.driver = driver
        self.Apollowipeslink = "//*[text()='Apollo Life Premium Citrus Refreshing Wet Wipes, 90 Count (3x 30 Wipes)']"
        self.stocktext = "// *[text() = 'In Stock']"
        self.Addtocartbutton="//*[@id='__next']/div/div/div[2]/div/div[3]/div/div[2]/div/div/div[1]/div[2]/button"
        self.Carttext="//*[text()='1 Pack in Cart']"

    # Creating Element Methods
    def click_productimage(self):
            Category = self.driver.find_element(By.XPATH, self.Apollowipeslink)
            Category.click()

    def click_Add_To_Cart(self):
            AddToCart = self.driver.find_element(By.XPATH, self.Addtocartbutton)
            AddToCart.click()

    def text_cart(self):
            Cart = self.driver.find_element(By.XPATH, self.Carttext).text
            return Cart

    def text_stock(self):
            Stock = self.driver.find_element(By.XPATH, self.stocktext).text
            return Stock