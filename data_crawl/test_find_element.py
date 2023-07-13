from selenium import webdriver
from selenium.webdriver.common.by import By
from login_fb import login
from sleep import sleep_3


def main():
    # open browser and disable notification
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_argument('--headless=new')

    browser = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=chrome_options)

    login(browser)
    sleep_3()

    browser.get('https://www.facebook.com/DucDaiFool/about_contact_and_basic_info')

    if is_no_info(browser):
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
            result_1 = (
                feature.find_element(By.XPATH, './child::*')
                .find_element(By.XPATH, './child::*')
                .find_elements(By.XPATH, './child::*')
            )

            filter = result_1[0].find_element(By.XPATH, './child::*').get_attribute("src")

            # birthday
            if filter == "https://static.xx.fbcdn.net/rsrc.php/v3/yH/r/8h5bbU4i43W.png":
                age = (
                    result_1[1].find_elements(By.XPATH, './child::*')[1]
                    .find_element(By.XPATH, './child::*')
                    .find_element(By.XPATH, './child::*')
                    .find_element(By.XPATH, './child::*')
                    .find_element(By.XPATH, './child::*')
                    .find_element(By.XPATH, './child::*').text
                )
            # sex
            elif filter == "https://static.xx.fbcdn.net/rsrc.php/v3/yo/r/wfYa2HPiNGU.png" or filter == "https://static.xx.fbcdn.net/rsrc.php/v3/yi/r/rodGQv9jZg5.png":
                sex = (
                    result_1[1].find_element(By.XPATH, './child::*')
                    .find_element(By.XPATH, './child::*')
                    .find_element(By.XPATH, './child::*')
                    .find_element(By.XPATH, './child::*')
                    .find_element(By.XPATH, './child::*')
                    .find_element(By.XPATH, './child::*').text
                )

    print(sex)
    print(2023 - int(age))

    # close browser
    browser.close()


def info(browser):
    result = browser.find_element(By.XPATH, '//div[@class="xyamay9 xqmdsaz x1gan7if x1swvt13"]')
    result = result.find_elements(By.XPATH, './child::*')[-1]  # 3 out
    result = result.find_element(By.XPATH, './child::*')  # div class
    result = result.find_elements(By.XPATH, './child::*')[1]  # div
    result = result.find_element(By.XPATH, './child::*')  # x13faqbe
    result = result.find_element(By.XPATH, './child::*')

    result = result.find_elements(By.XPATH, './child::*')
    filter = result[0].find_element(By.XPATH, './child::*').get_attribute("src")

    # birthday
    if filter == "https://static.xx.fbcdn.net/rsrc.php/v3/yH/r/8h5bbU4i43W.png":
        bod = result[1].find_elements(By.XPATH, './child::*')[1]
        bod = result.find_element(By.XPATH, './child::*')
        bod = result.find_element(By.XPATH, './child::*')
        bod = result.find_element(By.XPATH, './child::*')
        bod = result.find_element(By.XPATH, './child::*')
        bod = result.find_element(By.XPATH, './child::*').text
    # sex
    if filter == "https://static.xx.fbcdn.net/rsrc.php/v3/yo/r/wfYa2HPiNGU.png" or filter == "https://static.xx.fbcdn.net/rsrc.php/v3/yi/r/rodGQv9jZg5.png":
        sex = result[1].find_element(By.XPATH, './child::*')
        sex = result.find_element(By.XPATH, './child::*')
        sex = result.find_element(By.XPATH, './child::*')
        sex = result.find_element(By.XPATH, './child::*')
        sex = result.find_element(By.XPATH, './child::*')
        sex = result.find_element(By.XPATH, './child::*').text

    return {
        "sex": sex,
        "bod": bod
    }


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


if __name__ == '__main__':
    main()
