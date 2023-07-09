from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from time import sleep

BASE_URL = "https://www.facebook.com/"


def get_data_from_url(url):
    # open browser and disable notification
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_argument('--headless=new')
    browser = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=chrome_options)

    # login fb
    browser.get("https://www.facebook.com/")
    txtUser = browser.find_element(By.ID, "email")
    txtUser.send_keys('lvt.ip8s@gmail.com')
    txtPass = browser.find_element(By.ID, "pass")
    txtPass.send_keys('Lvt@2022')
    txtPass.send_keys(Keys.ENTER)

    # open page
    browser.get(url)

    # CRAWL RANGE START
    name = browser.find_element(By.XPATH, "//h1[@class='x1heor9g x1qlqyl8 x1pd3egz x1a2a7pz']").text
    ava = (
        browser.find_elements(By.XPATH,
                              '//div[@class="x1rg5ohu x1n2onr6 x3ajldb x1ja2u2z"]/*[name()="svg"]/*[name()="g"]')[1]
        .find_element(By.XPATH, "./child::*").get_attribute("xlink:href")
    )
    cover = (
        browser.find_elements(By.XPATH,
                              '//div[@class="x1qjc9v5 x1q0q8m5 x1qhh985 xu3j5b3 xcfux6l x26u7qi xm0m39n x13fuv20 x972fbf x1ey2m1c x9f619 x78zum5 xds687c xdt5ytf x1iyjqo2 xs83m0k x1qughib xat24cr x11i5rnm x1mh8g0r xdj266r x2lwn1j xeuugli x18d9i69 x4uap5 xkhd6sd xexx8yu x10l6tqk x17qophe x13vifvy x1ja2u2z"]')[
            2]
        .find_element(By.XPATH, "./child::*").get_attribute("src")
    )
    introduction = (
        browser.find_elements(By.XPATH, "//div[@class='x2b8uid xdppsyt x1l90r2v']")[0]
        .find_elements(By.XPATH, ".//*")[0].text.replace("\n", "")
    )
    try:
        nums_of_friend = browser.find_element(By.XPATH,
                                              "//a[@class='x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz xt0b8zv xi81zsa x1s688f']").text.split()[
            0]
        if 'K' in nums_of_friend:
            nums_of_friend = float(nums_of_friend[:-1]) * 1000
        elif nums_of_friend is not None:
            nums_of_friend = float(nums_of_friend)
    except:
        nums_of_friend = None

    nums_of_images = get_nums_of_images(browser, url)
    nums_of_videos = get_nums_of_videos(browser, url)
    nums_of_albums = get_nums_of_albums(browser, url)
    countryside = get_countryside(browser, url)
    address = get_address(browser, url)
    rela = get_rela(browser, url)

    return {
        'name': name,
        'ava': ava,
        'cover': cover,
        'introduction': introduction,
        'nums_of_friend': nums_of_friend,
        'nums_of_images': nums_of_images,
        'nums_of_videos': nums_of_videos,
        'nums_of_albums': nums_of_albums,
        'countryside': countryside,
        'address': address,
        'rela': rela,
    }


def get_nums_of_images(browser, url):
    browser.get("/".join([url.rstrip("/"), "photos"]))

    last_height = browser.execute_script("return document.body.scrollHeight")

    while not browser.find_elements(By.XPATH, '//div[@data-pagelet="ProfileAppSection_0"]'):
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(3)

        new_height = browser.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    return len(browser.find_elements(By.XPATH,
                                     '//a[@class="x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz x1heor9g xt0b8zv x1lliihq x5yr21d x1n2onr6 xh8yej3"]'))


def get_nums_of_videos(browser, url):
    browser.get("/".join([url.rstrip("/"), "videos"]))

    last_height = browser.execute_script("return document.body.scrollHeight")

    while not browser.find_elements(By.XPATH, '//div[@data-pagelet="ProfileAppSection_0"]'):
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(3)

        new_height = browser.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    return len(browser.find_elements(By.XPATH, '//div[@class="x1n2onr6"]'))


def get_nums_of_albums(browser, url):
    browser.get("/".join([url.rstrip("/"), "photos_albums"]))

    last_height = browser.execute_script("return document.body.scrollHeight")

    while not browser.find_elements(By.XPATH, '//div[@data-pagelet="ProfileAppSection_0"]'):
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(3)

        new_height = browser.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    return len(browser.find_elements(By.XPATH, '//div[@class="x1n2onr6"]'))


def get_countryside(browser, url):
    browser.get("/".join([url.rstrip("/"), "about_overview"]))
    sleep(3)

    try:
        info = browser.find_elements(By.XPATH,
                                     '//span[@class="x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xudqn12 x3x7a5m x6prxxf xvq8zen xo1l8bm xzsf02u"] | //span[@class="x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xudqn12 x3x7a5m x6prxxf xvq8zen xk50ysn xi81zsa"]')[
            -2].text
        if info in ('No places to show',):
            info = None
        # browser.back()
    except:
        info = 'protected'
    return info


def get_address(browser, url):
    # browser.get("/".join([url.rstrip("/"), "about_overview"]))
    # sleep(3)

    try:
        info = browser.find_elements(By.XPATH,
                                     '//span[@class="x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xudqn12 x3x7a5m x6prxxf xvq8zen xo1l8bm xzsf02u"] | //span[@class="x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xudqn12 x3x7a5m x6prxxf xvq8zen xk50ysn xi81zsa"]')

        if len(info) == 5:
            info = info[2].text
        else:
            info = None
    # browser.back()
    except:
        info = 'protected'
    return info


def get_rela(browser, url):
    # browser.get("/".join([url.rstrip("/"), "about_overview"]))
    # sleep(3)

    try:
        info = browser.find_elements(By.XPATH,
                                     '//span[@class="x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xudqn12 x3x7a5m x6prxxf xvq8zen xo1l8bm xzsf02u"] | //span[@class="x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xudqn12 x3x7a5m x6prxxf xvq8zen xk50ysn xi81zsa"]')[
            -1].text
    except:
        info = 'protected'
    if info in ('No relationship info to show',):
        info = 0
    elif info != 'protected':
        info = 1
    # browser.back()
    return info
