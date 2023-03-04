Feature: Personal Care
     Scenario: To Validate  delivery Pincode is valid.
       Given Chrome is opened and  Apollo 24/7 app is opened.
       When User clicks on later button
       And User clicks on  Pharmacy
       When User clicks on later button
       And User clicks on Apollo Products
       When User click on personal care and navigates to the landing page.
       And User click on Select your location button.
       When User  click on delivery pincode.
       And  User enter "Valid pincode number"
       When  User to click on Submit button
       Then It shows the  delivery pincode1 dataset
