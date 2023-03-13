**test_automation**
Testing framework for Hudl take home test


**Setup**
Install python
Install python packages
Set environment variables


**Usage**
Project structure
Running tests


**Install Python**
Windows:
For windows, get the latest 3.x version of python from [here](https://www.python.org/downloads/windows/)

Follow the steps in the installer to install python. This will python.exe and IDLE (python editor) programs to your pc.

Mac:
You should install python via [Homebrew](https://brew.sh/), and then:

    brew install python3

You can assert successful installation by running the following:
    
    python3 -V                                                                                              
    > Python 3.8.9

Environment Variables
Environment variables are used in some of these tests. For security purposes, please add your own user credentials to log in to Hudl's portal. This will need to be set for the following variables:
HUDL_USERNAME
HUDL_PASSWORD
HUDL_ORG_USERNAME

Get browsers/webdrivers
In order to run our tests we need a browser to run them on and the webdriver for that browser. 

To run all tests:

pytest -k "test_login.py" 

To run selective tests:

pytest -k "nameoftest"
