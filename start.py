__author__ = 'sacharya'
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def main():
    driver = webdriver.Chrome()
    driver.get("https://www.linkedin.com")
    assert "LinkedIn" in driver.title

    login(driver)
    end = input("Hit Y to close.")
    while end.capitalize() != 'Y':
        end = input("Hit Y to close.")
    close(driver)


# TODO : this is for test remove
def login(driver):
    username = os.environ['LIN_USER']
    if username is not None:
        elem = driver.find_element_by_name("session_key")
        elem.send_keys(username)
        elem = driver.find_element_by_name("session_password")
        elem.send_keys(os.environ['LIN_PWD'])
        elem.send_keys(Keys.RETURN)
        print(driver.title)
        assert "LinkedIn" in driver.title


def close(driver):
    driver.close()


if __name__ == "__main__":
    # execute only if run as a script
    main()
