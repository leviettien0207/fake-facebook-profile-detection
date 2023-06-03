from sleep import sleep_3
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
import config as cf

def get_all(browser, uid):
    """
    Claimed that facebook logged in
    Notice the tab openning before execute this function
    """
    return {
        'id': uid,
        'name': get_name(browser),
        'ava': get_ava(browser),
        'cover': get_cover(browser),
        'introduction': get_introduction(browser),
        'nums_of_friend': get_nums_of_friend(browser),
        # 'post': get_post(browser),

        # 'sex': get_sex(browser, uid),
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
    info = browser.find_elements(By.XPATH, cf.xpath_ava)[1]
    info = info.find_element(By.XPATH, "./child::*").get_attribute("xlink:href")
    return info

def get_cover(browser: WebDriver):
    try:
        info = browser.find_elements(By.XPATH, cf.xpath_cover)[2]
        info = info.find_element(By.XPATH, "./child::*").get_attribute("src")
    except:
        info = None
    return info

def get_introduction(browser: WebDriver):
    try:
        info = browser.find_elements(By.XPATH, cf.xpath_introduction_p)[0]
        info = info.find_elements(By.XPATH, ".//*")[0].text.replace("\n","")
    except:
        info = None
    return info

def get_nums_of_friend(browser: WebDriver):
    try:
        info = browser.find_element(By.XPATH, cf.xpath_nums_friend).text.split()[0]
        if 'K' in info:
            info = float(info[:-1]) * 1000
        else:
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
        sleep_3()

    return len(browser.find_elements(By.XPATH, cf.xpath_photos))

def get_nums_of_albums(browser: WebDriver, uid):
    browser.get(cf.albums_url.format(uid))

    while not browser.find_elements(By.XPATH, cf.xpath_check_ins):
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep_3()

    return len(browser.find_elements(By.XPATH, cf.xpath_albums))

def get_nums_of_videos(browser: WebDriver, uid):
    # browser.get(cf.videos_url.format(uid))

    # while not browser.find_elements(By.XPATH, cf.xpath_check_ins):
    #     browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #     sleep_3()

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

    while len(result) < 6 or not check_enough_posts(browser, result) :
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep_3()

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
        leng = post.find_element(By.XPATH, "./child::*")
        leng = leng.find_element(By.XPATH, "./child::*")
        leng = leng.find_element(By.XPATH, "./child::*")
        leng = leng.find_element(By.XPATH, "./child::*")
        leng = leng.find_element(By.XPATH, "./child::*")
        leng = leng.find_element(By.XPATH, "./child::*")
        leng = leng.find_element(By.XPATH, "./child::*")
        leng = leng.find_element(By.XPATH, "./child::*")
        leng = leng.find_element(By.XPATH, "./child::*")
        leng = leng.find_element(By.XPATH, "./child::*")
        leng = leng.find_elements(By.XPATH, "./child::*")[-1]
        leng = leng.find_element(By.XPATH, "./child::*")
        ac = leng.find_element(By.XPATH, "./child::*")
        leng = ac.find_elements(By.XPATH, "./child::*")

        if len(leng) != 2:
            posts.append(ac)
        if len(posts) == 3:
            break

    output = []
    for post in posts:
        captions, reacts = post.find_elements(By.XPATH, "./child::*")[2:4]
        
        captions = captions.find_element(By.XPATH, "./child::*")
        captions = captions.find_element(By.XPATH, "./child::*")
        captions = captions.find_element(By.XPATH, "./child::*")
        captions = captions.find_element(By.XPATH, "./child::*")
        captions = captions.find_element(By.XPATH, "./child::*")
        captions = captions.find_element(By.XPATH, "./child::*")
        captions = captions.find_element(By.XPATH, "./child::*").text

        reacts = reacts.find_element(By.XPATH, "./child::*")
        reacts = reacts.find_element(By.XPATH, "./child::*")
        reacts = reacts.find_element(By.XPATH, "./child::*")
        reacts = reacts.find_element(By.XPATH, "./child::*")
        reacts = reacts.find_element(By.XPATH, "./child::*")
        reacts = reacts.find_element(By.XPATH, "./child::*")
        reacts = reacts.find_element(By.XPATH, "./child::*")
        reacts = reacts.find_elements(By.XPATH, "./child::*")[-1]
        reacts = reacts.find_element(By.XPATH, "./child::*")
        reacts = reacts.find_element(By.XPATH, "./child::*")
        try:
            reacts = reacts.find_elements(By.XPATH, "./child::*")[1]
            reacts = reacts.find_element(By.XPATH, "./child::*")
            reacts = reacts.find_element(By.XPATH, "./child::*").text

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
    browser.get(cf.sex_url.format(uid))
    sleep_3()

    try:
        info = browser.find_elements(By.XPATH, cf.xpath_sex)
        if info:
            info = info[0].text
        else:
            info = None
    except:
        info = -1
    # browser.back()
    return info

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
    sleep_3()

    try:
        info = browser.find_elements(By.XPATH, cf.xpath_about)[-2].text
        if info in ('No places to show',):
            info = None
        # browser.back()
    except:
        info = "protected"
    return info

def get_address(browser: WebDriver, uid):
    browser.get(cf.about_url.format(uid))
    sleep_3()

    try:
        info = browser.find_elements(By.XPATH, cf.xpath_about)
            
        if len(info) == 5:
            info = info[2].text
        else:
            info = None
    # browser.back()
    except:
        info = "protected"
    return info

def get_rela(browser: WebDriver, uid):
    browser.get(cf.about_url.format(uid))
    sleep_3()

    try:
        info = browser.find_elements(By.XPATH, cf.xpath_about)[-1].text
    except:
        info = "protected"
    if info in ('No relationship info to show',):
        info = 0
    elif info != "protected":
        info = 1
    # browser.back()
    return info

def check_enough_posts(browser, lst):
    check = 0
    for post in lst:
        leng = post.find_element(By.XPATH, "./child::*")
        leng = leng.find_element(By.XPATH, "./child::*")
        leng = leng.find_element(By.XPATH, "./child::*")
        leng = leng.find_element(By.XPATH, "./child::*")
        leng = leng.find_element(By.XPATH, "./child::*")
        leng = leng.find_element(By.XPATH, "./child::*")
        leng = leng.find_element(By.XPATH, "./child::*")
        leng = leng.find_element(By.XPATH, "./child::*")
        leng = leng.find_element(By.XPATH, "./child::*")
        leng = leng.find_element(By.XPATH, "./child::*")
        leng = leng.find_elements(By.XPATH, "./child::*")[-1]
        leng = leng.find_element(By.XPATH, "./child::*")
        leng = leng.find_element(By.XPATH, "./child::*")
        leng = leng.find_elements(By.XPATH, "./child::*")

        if len(leng) == 4:
            check += 1
    
    if check >= 3:
        return True
    else:
        return False
