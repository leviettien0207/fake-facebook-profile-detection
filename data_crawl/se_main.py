from selenium import webdriver
from login_fb import login
from sleep import sleep_3
import logging
import os
from new_file_result_txt import new_file_2
from se_crawl_data import get_all
import json
from isExist import is_exist

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

    # open each main profile
    logging.info('Open list id to crawl detail')
    file_id_list = os.listdir('out')

    try:
        file_id_list.remove('example.txt')
    except ValueError:
        pass  # do nothing!

    list_data = []
    for file in file_id_list:
        logging.info(f'Open file {file}')
        id_list = open(f'out\{file}')
        for uid in id_list:

            uid = uid.replace('\n','')
            # open group member page
            logging.info(f'Open member page link {uid}')
            browser.get("https://www.facebook.com/" + uid)
            sleep_3()

            # check exist
            if is_exist(browser):
                # get data
                list_data.append(get_all(browser, uid))
                logging.info(f'Done page link {uid}')

            # open file
            if len(list_data) == 200:
                dictionary = {
                    "list_users": list_data
                }

                json_object = json.dumps(dictionary, indent=4, ensure_ascii=False)

                with open(new_file_2(), "w", encoding='utf-8') as outfile:
                    outfile.write(json_object)

                list_data.clear()

    # close browser
    browser.close()
    
if __name__ == '__main__':
    main()