from selenium import webdriver
from login_fb import login
from find import *
from sleep import sleep_3

def main():
    # open browser and disable notification
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications" : 2}
    chrome_options.add_experimental_option("prefs",prefs)

    browser = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=chrome_options)

    # login facebook
    login(browser)

    # open each group
    group_list = open('in\group.txt')
    for link in group_list:

        # open group member page
        browser.get(link)
        sleep_3()

        # find recent
        find_recent_user(browser)

        # find by name
        find_user_by_name(browser)


    # close browser
    browser.close()
    
if __name__ == '__main__':
    main()