from selenium import webdriver
from selenium.webdriver.common.by import By
from login_fb import login
from sleep import sleep_3
import logging
import config as cf
import json
from new_file import new_file_3

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')


def is_no_info(browser):
    result = browser.find_element(By.XPATH, '//div[@class="xyamay9 xqmdsaz x1gan7if x1swvt13"]')
    result = result.find_elements(By.XPATH, './child::*')[-1]  # 3 out
    result = result.find_element(By.XPATH, './child::*')  # div class
    result = result.find_elements(By.XPATH, './child::*')[1]  # div
    result = result.find_element(By.XPATH, './child::*')  # x13faqbe
    result = result.find_element(By.XPATH, './child::*')

    result = result.find_elements(By.XPATH, './child::*')
    filter = result[0].find_element(By.XPATH, './child::*').get_attribute("src")

    # birthday
    if filter == "https://static.xx.fbcdn.net/rsrc.php/v3/yA/r/4YyyTqCEtie.png":
        return True
    else:
        return False


def main():
    # open browser and disable notification
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_argument('--headless=new')

    browser = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=chrome_options)

    # login facebook
    logging.info('Logging in FB')
    login(browser)
    sleep_3()

    # open each main profile
    logging.info('Open list user')
    total = list()

    with open("combined.json", encoding='utf-8') as fh:
        data = json.load(fh)

        for user in data['list_users']:
            uid = user.get("id")
            logging.info(f'Open member page link {uid}')

            # open page
            browser.get(cf.sex_age_url.format(uid))
            sleep_3()

            try:
                protected = (
                    browser.find_element(By.XPATH, '//div[@class="xyamay9 xqmdsaz x1gan7if x1swvt13"]')
                    .find_elements(By.XPATH, './child::*')
                )

                if len(protected) == 0:
                    sex = cf.data_protected
                    age = -1
                elif is_no_info(browser):
                    sex = None
                    age = None
                else:
                    result = (
                        browser.find_element(By.XPATH, '//div[@class="xyamay9 xqmdsaz x1gan7if x1swvt13"]')
                        .find_elements(By.XPATH, './child::*')[-1]  # 3 out
                        .find_element(By.XPATH, './child::*')  # div class
                        .find_elements(By.XPATH, './child::*')
                    )

                    age = None
                    sex = None
                    # bod or sex?
                    for feature in result[1:]:
                        result = (
                            feature.find_element(By.XPATH, './child::*')
                            .find_element(By.XPATH, './child::*')
                            .find_elements(By.XPATH, './child::*')
                        )

                        filter = result[0].find_element(By.XPATH, './child::*').get_attribute("src")

                        # birthday
                        if filter == "https://static.xx.fbcdn.net/rsrc.php/v3/yH/r/8h5bbU4i43W.png":
                            age = (
                                result[1].find_elements(By.XPATH, './child::*')[1]
                                .find_element(By.XPATH, './child::*')
                                .find_element(By.XPATH, './child::*')
                                .find_element(By.XPATH, './child::*')
                                .find_element(By.XPATH, './child::*')
                                .find_element(By.XPATH, './child::*').text
                            )

                        # sex
                        elif filter == "https://static.xx.fbcdn.net/rsrc.php/v3/yo/r/wfYa2HPiNGU.png" or filter == "https://static.xx.fbcdn.net/rsrc.php/v3/yi/r/rodGQv9jZg5.png":
                            sex = (
                                result[1].find_element(By.XPATH, './child::*')
                                .find_element(By.XPATH, './child::*')
                                .find_element(By.XPATH, './child::*')
                                .find_element(By.XPATH, './child::*')
                                .find_element(By.XPATH, './child::*')
                                .find_element(By.XPATH, './child::*').text
                            )

            except:
                sex = None
                age = None

            user["sex"] = sex
            if age is not None and age != -1:
                user["age"] = 2023 - int(age)
            else:
                user["age"] = age

            total.append(user)
            logging.info(f'Add to list {len(total)}/200')

            if len(total) == 200:
                logging.info(f'write file')
                dictionary = {"list_users": total}

                json_object = json.dumps(dictionary, indent=4, ensure_ascii=False)

                with open(new_file_3(), "w", encoding='utf-8') as outfile:
                    outfile.write(json_object)

                total.clear()

    # close browser
    browser.close()


if __name__ == '__main__':
    main()
