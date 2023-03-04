Feature: PersonalCare
Background:Personal Care Navigation
    Given Chrome is opened and  Apollo 24/7 is opened.
       When User click on later button
       And User click on  Pharmacy
       When User click on later button
       And User click on Apollo Products
       When Click on personal care and navigates to the landing page.

    Scenario:To Validate that Special Offers link is clickable

       When User click on Special offers link
       Then It shows Special offers landing page

    Scenario: To validate that product image is clickable

       When User click on productImage
       Then It shows In Stock


    Scenario: To validate that Add to cart is clickable

       When User click on productImage
       Then It shows In Stock
       When User click on Add to cart
       Then It should display 1 pack in cart.


  Scenario Outline: To Validate  delivery Pincode is valid.

       When user clicks on Select your location button.
       And User  Click on delivery pincode on the  top of th personal care page.
       And  User enters  <Valid pincode number>
       And  User click on Submit button
       Then It shows the  delivery pincode Uppalapadu 518002
      Examples:
      | Valid pincode number|
      |518002       |

  Scenario Outline: To Validate delivery pincode is invalid.

      When user clicks on Select your location button.
      When User  Click on delivery pincode on the  top of th personal care page.
      And  User enters   <Invalid pincode number>
      When  User click on Submit button
      Then It shows the error messageerror message like"Sorry, we are not servicing in your area currently. Call 1860 500 0101 for pharmacy store nearby."

      Examples:
      |Invalid pincode number|
      |000000         |
      |111111         |
















