from new_file_result_txt import new_file
from sleep import sleep_3
from selenium.webdriver.common.by import By

def find_recent_user(browser):
    """
    Claimed that facebook logged in
    Notice the tab openning before execute this function
    """
    # Get scroll height
    last_height = browser.execute_script("return document.body.scrollHeight")

    # set chứa id
    id_set = list()

    # mở file
    fhandle = open(new_file(), "a+")

    while True:
        # Scroll down to bottom
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep_3()
        
        # thu thập 10 thằng cuối
        list_users = browser.find_elements(By.XPATH, "//div[@class='x1oo3vh0 x1rdy4ex']")[0].find_elements(By.XPATH, "//a[@aria-hidden='true']")[-10:]
        sleep_3()

        for user in list_users:
            id_set.append(user.get_attribute("href")[-16:-1])

            if len(id_set) == 200:
                for uid in id_set:
                    fhandle.write(uid + "\n")
                id_set.clear()

        # Calculate new scroll height and compare with last scroll height
        new_height = browser.execute_script("return document.body.scrollHeight")
        sleep_3()

        if new_height == last_height:
            break
        last_height = new_height

    fhandle.close()


def find_user_by_name(browser):
    """
    Claimed that facebook logged in
    Notice the tab openning before execute this function
    """
    # Get scroll height
    last_height = browser.execute_script("return document.body.scrollHeight")

    # set chứa id
    id_set = list()

    # mở file
    fhandle = open(new_file(), "a+")

    # loop each name
    name_list = open('in\str_name.txt')
    for uname in name_list:
        
        # input name
        element = browser.find_elements(By.XPATH, "//input[@dir='ltr']")[-1]
        element.clear()
        element.send_keys(uname)
        sleep_3()

        while True:
            # Scroll down to bottom
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep_3()
            
            # thu thập 10 thằng cuối
            list_users = browser.find_elements(By.XPATH, "//div[@class='x1oo3vh0 x1rdy4ex']")[0].find_elements(By.XPATH, "//a[@aria-hidden='true']")[-10:]
            sleep_3()

            for user in list_users:
                id_set.append(user.get_attribute("href")[-16:-1])

                if len(id_set) == 200:
                    for uid in id_set:
                        fhandle.write(uid + "\n")
                    id_set.clear()

            # Calculate new scroll height and compare with last scroll height
            new_height = browser.execute_script("return document.body.scrollHeight")
            sleep_3()

            if new_height == last_height:
                break
            last_height = new_height

    fhandle.close()