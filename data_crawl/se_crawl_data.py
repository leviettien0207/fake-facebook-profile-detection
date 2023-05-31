from sleep import sleep_3
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

def get_all(browser, uid):
    """
    Claimed that facebook logged in
    Notice the tab openning before execute this function
    """
    return {
        'id': uid,
        'name': get_name(browser),
        # 'ava': get_ava(browser),
        # 'cover': get_cover(browser),
        'introduction': get_introduction(browser),
        # 'nums_of_friend': get_nums_of_friend(browser),
        # 'about': get_about(browser),
        # 'nums_of_images': get_nums_of_images(browser),
        # 'nums_of_albums': get_nums_of_albums(browser),
        # 'nums_of_videos': get_nums_of_videos(browser),
        # 'nums_of_checkins': get_nums_of_checkins(browser),
        # 'post': get_post(browser),
        # 'sex': get_sex(browser),
        # 'countryside': get_countryside(browser),
        # 'address': get_address(browser),
        # 'nums_nested_link': get_nums_nested_link(browser),
        # 'rela': get_rela(browser)
    }

def get_name(browser: WebDriver):
    return browser.find_element(By.XPATH, "//h1[@class='x1heor9g x1qlqyl8 x1pd3egz x1a2a7pz']").text

# todo
def get_ava(browser: WebDriver):
    return None
    head = browser.find_element(By.XPATH, "//div[@class='x1rg5ohu x1n2onr6 x3ajldb x1ja2u2z']")
    # return head.find_element(By.XPATH, "//image[@style='height:168px;width:168px']").get_attribute("href")
    return head.find_element(By.XPATH, '//*[@id="mount_0_0_SI"]').get_attribute("href")

def get_cover(browser: WebDriver):
    pass

def get_introduction(browser: WebDriver):
    try:
        intro = browser.find_element(By.XPATH, "//span[@class='x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xudqn12 x3x7a5m x6prxxf xvq8zen xo1l8bm xzsf02u']").text
    except:
        intro = None
    return intro

def get_nums_of_friend(browser: WebDriver):
    pass

def get_about(browser: WebDriver):
    pass

def get_nums_of_images(browser: WebDriver):
    pass

def get_nums_of_albums(browser: WebDriver):
    pass

def get_nums_of_videos(browser: WebDriver):
    pass

def get_nums_of_checkins(browser: WebDriver):
    pass

def get_post(browser: WebDriver):
    pass

def get_sex(browser: WebDriver):
    pass

def get_countryside(browser: WebDriver):
    pass

def get_address(browser: WebDriver):
    pass

def get_nums_nested_link(browser: WebDriver):
    pass

def get_rela(browser: WebDriver):
    pass