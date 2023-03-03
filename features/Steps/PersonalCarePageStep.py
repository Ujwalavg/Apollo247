from behave import*
from hamcrest import assert_that, equal_to
from features.Pages.LandingPageClass import LandingPageClass
from features.Pages.PersonalCarePageClass import PersonalCarePageClass
from features.Pages.ProductPageClass import ProductPageClass


@given(u'Chrome is opened and  Apollo 24/7 is opened.')
def step_impl(context):
    context.driver.implicitly_wait(10)
    expectedTitle = "Apollo 247 - Online Doctor Consultation & Book Lab Tests at Home"
    actualTitle = context.driver.title
    print("Page title is " + actualTitle)
    assert_that(expectedTitle, equal_to(actualTitle))

@when(u'user click on later button')
def step_impl(context):
    context.driver.implicitly_wait(10)
    LaterButton=LandingPageClass(context.driver)
    LaterButton.click_Later_button()


@when(u'user click on  Pharmacy')
def step_impl(context):
    context.driver.implicitly_wait(10)
    Pharamacylink=LandingPageClass(context.driver)
    Pharamacylink.click_Pharmacy_Link()


@when(u'User click on Apollo Products')
def step_impl(context):
    context.driver.implicitly_wait(10)
    Apollo =LandingPageClass(context.driver)
    Apollo.mouse_hover()


@when(u'click on personal care and navigates to the landing page.')
def step_impl(context):
    context.driver.implicitly_wait(10)
    PersonalCare=LandingPageClass(context.driver)
    PersonalCare.click_PersonalCare()

#Special offers
@when(u'User click on Special offers link')
def step_impl(context):
    context.driver.implicitly_wait(10)
    Specialoffers=PersonalCarePageClass(context.driver)
    Specialoffers.click_SpecialOffers()

@then(u'It shows Special offers landing page')
def step_impl(context):
    context.driver.implicitly_wait(10)
    specoff = PersonalCarePageClass(context.driver)
    expectedspecoffText = "25% Flat Discount on first three purchase on medicine Order of Rs.800 & above"
    actualspecoffText = specoff.check_specialoff_text()
    print(actualspecoffText)
    assert_that(expectedspecoffText, equal_to(actualspecoffText))
#ProductImage
@when(u'User click on productImage')
def step_impl(context):
    context.driver.implicitly_wait(10)
    Product = ProductPageClass(context.driver)
    Product.click_productimage()
    context.driver.implicitly_wait(10)


@then(u'It shows In Stock')
def step_impl(context):
    context.driver.implicitly_wait(10)
    Stock = ProductPageClass(context.driver)
    expectedstockText = "In Stock"
    actualstockText = Stock.text_stock()
    print(actualstockText)
    assert_that(expectedstockText, equal_to(actualstockText))
    context.driver.implicitly_wait(10)

#Add to cart
@when(u'User click on Add to cart')
def step_impl(context):
    context.driver.implicitly_wait(10)
    Addtocart=ProductPageClass(context.driver)
    Addtocart.click_Add_To_Cart()

@then(u'It should display 1 pack in cart.')
def step_impl(context):
        context.driver.implicitly_wait(10)
        pack = ProductPageClass(context.driver)
        expectedpackText = "1 PACK IN CART"
        actualpackText = pack.text_cart()
        print(actualpackText)
        assert_that(expectedpackText, equal_to(actualpackText))

#Valid pincode
@when(u'user clicks on Select your location button.')
def step_impl(context):
    context.driver.implicitly_wait(10)
    Selectlocation = PersonalCarePageClass(context.driver)
    Selectlocation.click_SelectLocation()



@when(u'User  Click on delivery pincode on the  top of th personal care page.')
def step_impl(context):
    context.driver.implicitly_wait(10)
    deliveryCode = PersonalCarePageClass(context.driver)
    deliveryCode.click_deliveryPincode()


@when(u'User enters  {upincode}')
def step_impl(context,upincode):
    context.driver.implicitly_wait(10)
    Enterpicncodenum=PersonalCarePageClass(context.driver)
    Enterpicncodenum.enter_pincode(upincode)

@when(u'User click on Submit button')
def step_impl(context):
    context.driver.implicitly_wait(10)
    submitbutton=PersonalCarePageClass(context.driver)
    submitbutton.click_submitbutton()


@then(u'It shows the  delivery pincode Uppalapadu 518002')
def step_impl(context):
    context.driver.implicitly_wait(10)
    username = PersonalCarePageClass(context.driver)
    expectedusernameText = "Uppalapadu 518002"
    actualusernameText = username.check_User_pincode()
    print(actualusernameText)
    assert_that(expectedusernameText, equal_to(actualusernameText))


#Inavalid pincode

@then(u'It shows the error messageerror message like"Sorry, we are not servicing in your area currently. Call 1860 500 0101 for pharmacy store nearby."')
def step_impl(context):
    context.driver.implicitly_wait(10)
    errorname = PersonalCarePageClass(context.driver)
    expectedusernameText = "Sorry, we are not servicing in your area currently. Call 1860 500 0101 for pharmacy store nearby."
    actualusernameText = errorname.check_error_message()
    print(actualusernameText)
    assert_that(expectedusernameText, equal_to(actualusernameText))





