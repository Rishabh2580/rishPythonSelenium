Web UI Automation with Selenium for Beginners


Objective -:

1.Cover Web UI automation (parabank website)using Selenium with a focus on the Python programming language.
2.Learn how to easily gather Web UI information, record their actions and play them back via Selenium IDE 
3.Write Python code to perform the same actions interactively
Run  code with py.test
4.Use SauceLabs to execute automated tests on multiple types of operating systems and web browser combinations.



Using Pycharm-:
 See this helpfull document explaining now to use a virtualenv in a Pycharm

1.Install the pycharm .
2.Download selenium through cmd (pip install selenium)
3.also download pip install (pip install pytest)



Using Pycharm IDE-:

1.Firefox plugin ONLY
2.Easy to set the path of drivers.
3.Requires Chrome Version 108.0.5359.125
4.Records all interactions with browser
5.GREAT IDE with tons of useful features
6.Exports test cases into Python code (and other formats)
7.Requires creativity to ensure that playing back activities will wait for web elements to be present







Install web driver-:
You will need to install a valid webdriver:

Chrome: https://sites.google.com/a/chromium.org/chromedriver/downloads
Firefox: https://github.com/mozilla/geckodriver/releases



Running All Tests Simultaneously-:Just Right click on test directory or just simply select the test run option and perform the action.



Note: I have used the pages and inside the pages I have putted all the locators and in my config file i have putting all my baseurl or drivers location.

python -m pytest (use this command to run simultaneously).It can be also run through batch file  also.

Those one or two test cases are not run through cmd run these test cases through pyhton file.

if Some of the test cases will not run then it may be  website is dynamic in nature.










