Feature: Personal Care
     Scenario: To Validate  delivery Pincode is valid.
       Given Chrome is opened and  Apollo 24/7 app is opened.
       When user clicks on later button
       When user clicks on  Pharmacy
       When user clicks on later button
       When User clicks on Apollo Products
       When user click on personal care and navigates to the landing page.
       When user click on Select your location button.
       When User  click on delivery pincode.
       And  User enter "Valid pincode number"
       And  User to click on Submit button
       Then It shows the  delivery pincode1 dataset
