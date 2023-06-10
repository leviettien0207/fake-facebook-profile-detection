from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
import config as cf
from time import sleep
from selenium.webdriver.common.keys import Keys
import os


def new_file():
    i = 0
    while os.path.isfile('out_data\\result_{}.json'.format(i)):
        i += 1

    return 'out_data\\result_{}.json'.format(i)


def sleep_abit():
    sleep(2.6)


def get_all(browser, uid):
    """
    Claimed that facebook logged in
    Notice the tab opening before execute this function
    """
    return {
        'id': uid,
        'name': get_name(browser),
        'ava': get_ava(browser),
        'cover': get_cover(browser),
        'introduction': get_introduction(browser),
        'nums_of_friend': get_nums_of_friend(browser),
        # 'post': get_post(browser),
        'sex': get_sex(browser, uid),
        'age': get_age(browser, uid),
        # 'nums_nested_link': get_nums_nested_link(browser),

        # 'about': get_about(browser),

        'nums_of_images': get_nums_of_images(browser, uid),
        'nums_of_videos': get_nums_of_videos(browser, uid),
        'nums_of_albums': get_nums_of_albums(browser, uid),

        # 'nums_of_checkins': get_nums_of_checkins(browser),

        'countryside': get_countryside(browser, uid),
        'address': get_address(browser, uid),
        'rela': get_rela(browser, uid)
    }


def get_name(browser: WebDriver):
    return browser.find_element(By.XPATH, cf.xpath_name).text


def get_ava(browser: WebDriver):
    info = (
        browser.find_elements(By.XPATH, cf.xpath_ava)[1]
        .find_element(By.XPATH, "./child::*").get_attribute("xlink:href")
    )
    return info


def get_cover(browser: WebDriver):
    try:
        info = (
            browser.find_elements(By.XPATH, cf.xpath_cover)[2]
            .find_element(By.XPATH, "./child::*").get_attribute("src")
        )
    except:
        info = None
    return info


def get_introduction(browser: WebDriver):
    try:
        info = (
            browser.find_elements(By.XPATH, cf.xpath_introduction_p)[0]
            .find_elements(By.XPATH, ".//*")[0].text.replace("\n", "")
        )
    except:
        info = None
    return info


def get_nums_of_friend(browser: WebDriver):
    try:
        info = browser.find_element(By.XPATH, cf.xpath_nums_friend).text.split()[0]
        if 'K' in info:
            info = float(info[:-1]) * 1000
        elif info is not None:
            info = float(info)
    except:
        info = None
    return info


def get_about(browser: WebDriver):
    return None


def get_nums_of_images(browser: WebDriver, uid):
    browser.get(cf.photos_url.format(uid))

    while not browser.find_elements(By.XPATH, cf.xpath_check_ins):
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep_abit()

    return len(browser.find_elements(By.XPATH, cf.xpath_photos))


def get_nums_of_albums(browser: WebDriver, uid):
    browser.get(cf.albums_url.format(uid))

    while not browser.find_elements(By.XPATH, cf.xpath_check_ins):
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep_abit()

    return len(browser.find_elements(By.XPATH, cf.xpath_albums))


def get_nums_of_videos(browser: WebDriver, uid):
    # browser.get(cf.videos_url.format(uid))

    # while not browser.find_elements(By.XPATH, cf.xpath_check_ins):
    #     browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #     sleep_abit()

    return len(browser.find_elements(By.XPATH, cf.xpath_albums))


def get_nums_of_checkins(browser: WebDriver):
    return None


def get_post(browser: WebDriver):
    last_height = browser.execute_script("return document.body.scrollHeight")
    result = browser.find_element(By.XPATH, '//div[@data-pagelet="ProfileTimeline"]')
    result = result.find_elements(By.XPATH, './child::*')
    if len(result) == 2:
        result = result[-1]
        result = result.find_elements(By.XPATH, './child::*')
        result = result[1:-3]
    else:
        result = result[:-3]

    while len(result) < 6 or not check_enough_posts(result):
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep_abit()

        result = browser.find_element(By.XPATH, '//div[@data-pagelet="ProfileTimeline"]')
        result = result.find_elements(By.XPATH, './child::*')[-1]
        result = result.find_elements(By.XPATH, './child::*')
        result = result[1:-3]

        new_height = browser.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    posts = []
    for post in result:
        leng = (
            post.find_element(By.XPATH, "./child::*")
            .find_element(By.XPATH, "./child::*")
            .find_element(By.XPATH, "./child::*")
            .find_element(By.XPATH, "./child::*")
            .find_element(By.XPATH, "./child::*")
            .find_element(By.XPATH, "./child::*")
            .find_element(By.XPATH, "./child::*")
            .find_element(By.XPATH, "./child::*")
            .find_element(By.XPATH, "./child::*")
            .find_element(By.XPATH, "./child::*")
            .find_elements(By.XPATH, "./child::*")[-1]
            .find_element(By.XPATH, "./child::*")
        )
        ac = leng.find_element(By.XPATH, "./child::*")
        leng = ac.find_elements(By.XPATH, "./child::*")

        if len(leng) != 2:
            posts.append(ac)
        if len(posts) == 3:
            break

    output = []
    for post in posts:
        captions, reacts = post.find_elements(By.XPATH, "./child::*")[2:4]

        captions = (
            captions.find_element(By.XPATH, "./child::*")
            .find_element(By.XPATH, "./child::*")
            .find_element(By.XPATH, "./child::*")
            .find_element(By.XPATH, "./child::*")
            .find_element(By.XPATH, "./child::*")
            .find_element(By.XPATH, "./child::*")
            .find_element(By.XPATH, "./child::*").text
        )

        reacts = (
            reacts.find_element(By.XPATH, "./child::*")
            .find_element(By.XPATH, "./child::*")
            .find_element(By.XPATH, "./child::*")
            .find_element(By.XPATH, "./child::*")
            .find_element(By.XPATH, "./child::*")
            .find_element(By.XPATH, "./child::*")
            .find_element(By.XPATH, "./child::*")
            .find_elements(By.XPATH, "./child::*")[-1]
            .find_element(By.XPATH, "./child::*")
            .find_element(By.XPATH, "./child::*")
        )

        try:
            reacts = (
                reacts.find_elements(By.XPATH, "./child::*")[1]
                .find_element(By.XPATH, "./child::*")
                .find_element(By.XPATH, "./child::*").text
            )

            if 'K' in reacts:
                reacts = float(reacts[:-1]) * 1000
        except:
            reacts = -2

        output.append({
            "caption": captions,
            "reaction": reacts
        })
    return output


def get_sex(browser: WebDriver, uid):
    browser.get(cf.sex_age_url.format(uid))
    sleep_abit()

    # no element at all --> protected
    try:
        protected = (
            browser.find_element(By.XPATH, '//div[@class="xyamay9 xqmdsaz x1gan7if x1swvt13"]')
            .find_elements(By.XPATH, './child::*')
        )
        sex = None

        if len(protected) == 0:
            sex = -1
        elif is_no_info(browser):
            pass
        else:
            result = (
                protected[-1]  # 3 out
                .find_element(By.XPATH, './child::*')  # div class
                .find_elements(By.XPATH, './child::*')
            )

            for feature in result[1:]:
                result_1 = (
                    feature.find_element(By.XPATH, './child::*')
                    .find_element(By.XPATH, './child::*')
                    .find_elements(By.XPATH, './child::*')
                )

                tpe = result_1[0].find_element(By.XPATH, './child::*').get_attribute("src")

                # sex
                if tpe in cf.sex_icon:
                    sex = (
                        result_1[1].find_element(By.XPATH, './child::*')
                        .find_element(By.XPATH, './child::*')
                        .find_element(By.XPATH, './child::*')
                        .find_element(By.XPATH, './child::*')
                        .find_element(By.XPATH, './child::*')
                        .find_element(By.XPATH, './child::*').text
                    )
                    break
    except:
        sex = cf.no_info_icon
    return sex


def get_age(browser: WebDriver, uid):
    # browser.get(cf.sex_age_url.format(uid))
    # sleep_abit()

    # no element at all --> protected
    try:
        protected = (
            browser.find_element(By.XPATH, '//div[@class="xyamay9 xqmdsaz x1gan7if x1swvt13"]')
            .find_elements(By.XPATH, './child::*')
        )
        age = None

        if len(protected) == 0:
            age = -1
        elif is_no_info(browser):
            pass
        else:
            result = (
                protected[-1]  # 3 out
                .find_element(By.XPATH, './child::*')  # div class
                .find_elements(By.XPATH, './child::*')
            )

            for feature in result[1:]:
                result_1 = (
                    feature.find_element(By.XPATH, './child::*')
                    .find_element(By.XPATH, './child::*')
                    .find_elements(By.XPATH, './child::*')
                )

                tpe = result_1[0].find_element(By.XPATH, './child::*').get_attribute("src")

                # birthday
                if tpe == cf.bod_icon:
                    age = (
                        result_1[1].find_elements(By.XPATH, './child::*')[1]
                        .find_element(By.XPATH, './child::*')
                        .find_element(By.XPATH, './child::*')
                        .find_element(By.XPATH, './child::*')
                        .find_element(By.XPATH, './child::*')
                        .find_element(By.XPATH, './child::*').text
                    )
                    break
            age = 2023 - int(age)
    except:
        age = cf.data_protected
    return age


def get_nums_nested_link(browser: WebDriver):
    # info = browser.find_elements(By.XPATH, cf.xpath_sex)
    # if info:
    #     info = info[0].text
    # else:
    #     info = None
    # # browser.back()
    return None


def get_countryside(browser: WebDriver, uid):
    browser.get(cf.about_url.format(uid))
    sleep_abit()

    try:
        info = browser.find_elements(By.XPATH, cf.xpath_about)[-2].text
        if info in ('No places to show',):
            info = None
        # browser.back()
    except:
        info = cf.data_protected
    return info


def get_address(browser: WebDriver, uid):
    browser.get(cf.about_url.format(uid))
    sleep_abit()

    try:
        info = browser.find_elements(By.XPATH, cf.xpath_about)

        if len(info) == 5:
            info = info[2].text
        else:
            info = None
    # browser.back()
    except:
        info = cf.data_protected
    return info


def get_rela(browser: WebDriver, uid):
    browser.get(cf.about_url.format(uid))
    sleep_abit()

    try:
        info = browser.find_elements(By.XPATH, cf.xpath_about)[-1].text
    except:
        info = cf.data_protected
    if info in ('No relationship info to show',):
        info = 0
    elif info != cf.data_protected:
        info = 1
    # browser.back()
    return info


def check_enough_posts(lst):
    check = 0
    for post in lst:
        length = (
            post.find_element(By.XPATH, "./child::*")
            .find_element(By.XPATH, "./child::*")
            .find_element(By.XPATH, "./child::*")
            .find_element(By.XPATH, "./child::*")
            .find_element(By.XPATH, "./child::*")
            .find_element(By.XPATH, "./child::*")
            .find_element(By.XPATH, "./child::*")
            .find_element(By.XPATH, "./child::*")
            .find_element(By.XPATH, "./child::*")
            .find_element(By.XPATH, "./child::*")
            .find_elements(By.XPATH, "./child::*")[-1]
            .find_element(By.XPATH, "./child::*")
            .find_element(By.XPATH, "./child::*")
            .find_elements(By.XPATH, "./child::*")
        )
        if len(length) == 4:
            check += 1

    if check >= 3:
        return True
    else:
        return False


def is_no_info(browser):
    result = (
        browser.find_element(By.XPATH, '//div[@class="xyamay9 xqmdsaz x1gan7if x1swvt13"]')
        .find_elements(By.XPATH, './child::*')[-1]  # 3 out
        .find_element(By.XPATH, './child::*')  # div class
        .find_elements(By.XPATH, './child::*')[1]  # div
        .find_element(By.XPATH, './child::*')  # x13faqbe
        .find_element(By.XPATH, './child::*')
        .find_elements(By.XPATH, './child::*')[0]
        .find_element(By.XPATH, './child::*').get_attribute("src")
    )
    if result == cf.no_info_icon:
        return True
    else:
        return False


def new_file():
    i = 0
    while os.path.isfile('out_data\\result_{}.json'.format(i)):
        i += 1

    return 'out_data\\result_{}.json'.format(i)


def is_exist(browser: WebDriver):
    try:
        browser.find_element(By.XPATH, cf.xpath_exist_page)
        flag = False
    except:
        flag = True
    return flag


def login(browser):
    browser.get("https://www.facebook.com/")

    txtUser = browser.find_element(By.ID, "email")
    txtUser.send_keys("lvt.ip8s@gmail.com")

    txtPass = browser.find_element(By.ID, "pass")
    txtPass.send_keys("Lvt@2022")

    txtPass.send_keys(Keys.ENTER)
