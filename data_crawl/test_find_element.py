from selenium import webdriver
from selenium.webdriver.common.by import By
from login_fb import login
from sleep import sleep_3

def main():
    # open browser and disable notification
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications" : 2}
    chrome_options.add_experimental_option("prefs",prefs)

    browser = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=chrome_options)

    login(browser)
    sleep_3()

    browser.get('https://www.facebook.com/Tratri.nss')
    # nodes = self.driver.find_elements(By.XPATH, "//div[@id='d3_tree']/*/*[name()='g']")

    # result = browser.find_elements(By.XPATH, '//div[@class="x1rg5ohu x1n2onr6 x3ajldb x1ja2u2z"]')
    # result = browser.find_elements(By.XPATH, '//div[@class="xu06os2 x1ok221b"]')
    result = browser.find_element(By.XPATH, '//div[@data-pagelet="ProfileTimeline"]')
    result = result.find_elements(By.XPATH, './child::*')[-1]
    result = result.find_elements(By.XPATH, './child::*')
    result = result[1:-3]

    while len(result) < 6 or not check_enough_posts(browser, result) :
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep_3()

        result = browser.find_element(By.XPATH, '//div[@data-pagelet="ProfileTimeline"]')
        result = result.find_elements(By.XPATH, './child::*')[-1]
        result = result.find_elements(By.XPATH, './child::*')
        result = result[1:-3]
    
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


    
        if len(leng) == 4:
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
        reacts = reacts.find_elements(By.XPATH, "./child::*")[1]
        reacts = reacts.find_element(By.XPATH, "./child::*")
        reacts = reacts.find_element(By.XPATH, "./child::*").text

        if 'K' in reacts:
            reacts = float(reacts[:-1]) * 1000

        output.append({
            "caption": captions,
            "reaction": reacts
        })
    
    print(output)
    # print(len(result))
    # del result[0]
    # del result[-3:]
    # print(len(result))



    # result = result.find_elements(By.XPATH, '//*//*//*div[@class="xu06os2 x1ok221b"]')
    # result = result.find_elements(By.XPATH, '/*/*')
    # result = result.find_element(By.XPATH, "./child::*").get_attribute("src")
    # # print(result)
    # print(len(result))

    # close browser
    browser.close()

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
        # print(leng)



if __name__ == '__main__':
    main()