from selenium import webdriver
from login_fb import login
from find import *
from sleep import sleep_3
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

def main():
    # open browser and disable notification
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications" : 2}
    chrome_options.add_experimental_option("prefs",prefs)

    browser = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=chrome_options)

    # login facebook
    logging.info('Logging in FB')
    login(browser)
    sleep_3()

    # open each group
    logging.info('Open list group to crawl id')
    group_list = open('in\group.txt')
    for link in group_list:

        # open group member page
        logging.info(f'Open member page link {link}')
        browser.get(link)
        sleep_3()

        # find recent
        logging.info(f'Finding recent join group...')
        find_recent_user(browser)

        ## find by name.
        #logging.info(f'Finding by name...')
        #find_user_by_name(browser)

        logging.info(f'Done page link {link}')

    # close browser
    browser.close()
    
if __name__ == '__main__':
    main()
