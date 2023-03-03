from behave import *
from hamcrest import *


from datafile import ExcelUtils
from features.Pages.LandingPageClass import LandingPageClass
from features.Pages.PersonalCarePageClass import PersonalCarePageClass
from features.utility.ConfigClass import ConfigClass


@given(u'Chrome is opened and  Apollo 24/7 app is opened.')
def step_impl(context):
    context.driver.implicitly_wait(10)
    expectedTitle = "Apollo 247 - Online Doctor Consultation & Book Lab Tests at Home"
    actualTitle = context.driver.title
    print("Page title is " + actualTitle)
    assert_that(expectedTitle, equal_to(actualTitle))



@when(u'user clicks on later button')
def step_impl(context):
    context.driver.implicitly_wait(10)
    LaterButton = LandingPageClass(context.driver)
    LaterButton.click_Later_button()



@when(u'user clicks on  Pharmacy')
def step_impl(context):
    context.driver.implicitly_wait(10)
    Pharamacylink = LandingPageClass(context.driver)
    Pharamacylink.click_Pharmacy_Link()



@when(u'User clicks on Apollo Products')
def step_impl(context):
    context.driver.implicitly_wait(10)
    Apollo = LandingPageClass(context.driver)
    Apollo.mouse_hover()


@when(u'user click on personal care and navigates to the landing page.')
def step_impl(context):
    context.driver.implicitly_wait(10)
    PersonalCare = LandingPageClass(context.driver)
    PersonalCare.click_PersonalCare()

@when(u'user click on Select your location button.')
def step_impl(context):
    context.driver.implicitly_wait(10)
    Selectlocation = PersonalCarePageClass(context.driver)
    Selectlocation.click_SelectLocation()


@when(u'User  click on delivery pincode.')
def step_impl(context):
    context.driver.implicitly_wait(10)
    deliveryCode = PersonalCarePageClass(context.driver)
    deliveryCode.click_deliveryPincode()


@when(u'User enter "{upincode}"')
def step_impl(context,upincode):
    context.driver.implicitly_wait(10)
    ExcelUtils.get_row_count(ConfigClass.datafilepath, "Sheet1")
    data = ExcelUtils.read_data(ConfigClass.datafilepath, "Sheet1", 2, 1)
    Enterpincodenum = PersonalCarePageClass(context.driver)
    Enterpincodenum.enter_pincode(data)


@when(u'User to click on Submit button')
def step_impl(context):
    context.driver.implicitly_wait(10)
    submitbutton = PersonalCarePageClass(context.driver)
    submitbutton.click_submitbutton()



@then(u'It shows the  delivery pincode1 dataset')
def step_impl(context):
    context.driver.implicitly_wait(10)
    pin = PersonalCarePageClass(context.driver)
    expectedusernameText = "Uppalapadu 518002"
    actualusernameText = pin.check_User_pincode()
    print(actualusernameText)
    assert_that(expectedusernameText, equal_to(actualusernameText))
    context.driver.implicitly_wait(10)
    try:        
         if(expectedusernameText == actualusernameText ):
             assert True
             print("Test is passed")
             ExcelUtils.write_data(ConfigClass.datafilepath, "Sheet1", 2, 2, "Passed")
             context.driver.implicitly_wait(10)
         else:         
             print("Test is failed")
             ExcelUtils.write_data(ConfigClass.datafilepath, "Sheet1", 2, 2, "Failed")
             assert False
         context.driver.implicitly_wait(10)
    finally:        
        context.driver.implicitly_wait(10)
        locupdate = PersonalCarePageClass(context.driver)
        locupdate.click_loaction_update()







