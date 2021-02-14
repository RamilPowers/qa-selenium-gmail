# Gmail QA test
#### This app test maded with Python + Selenium + Pytest + Allure

Description
-----------------------------------
What does this test do:
1. Opens the browser and goes to `https://mail.google.com`
2. Login in Google account with your own e-mail and password
3. Counts the number of letters from sender
4. Writes and send a new letter to that sender with data from point 3.

Installation
-----------------------------------
The app uses `Pipenv` as a virtual environment.  
Default test browser is Chrome.
1. Copy the project with  
`git clone https://github.com/RamilPowers/qa-selenium-gmail.git .`
2. Create `environment_variables.py` file in app direction. This file contains all secret variables.
2. Activate the Pipenv virtual environment with  
`pipenv shell`
3. Install packets with  
`pipenv install`
4. Set up Allure
4. Set up Selenium GRID (optional) 
5. Run the test with Allure with  
`pytest test.py --alluredir <name_of_the_dir_with_results>`
6. Check results with  
`allure serve <name_of_the_dir_with_results>`