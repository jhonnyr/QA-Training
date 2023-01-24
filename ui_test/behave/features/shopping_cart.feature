Feature: Login


Scenario: Login to the site
	  Given As user login to the admin application in the environment
	  When Select the "Samsung galaxy s7" item and add it to the shopping cart
	  Then Go to the shopping car and buy the item
	  |name|country|city|credit_card|month|year|
	  |Test User|Colombia|Cali |112233445566778899|03|2025|

