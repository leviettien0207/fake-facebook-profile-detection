from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


def is_exist(browser: WebDriver):
    try:
        flag = browser.find_element(By.XPATH,
                                    "//div[@class='x1n2onr6 x1ja2u2z x78zum5 x2lah0s xl56j7k x6s0dn4 xozqiw3 x1q0g3np xi112ho x17zwfj4 x585lrc x1403ito x972fbf xcfux6l x1qhh985 xm0m39n x9f619 xbxaen2 x1u72gb5 xtvsq51 x1fq8qgq']")
        flag = False
    except:
        flag = True
    return flag
