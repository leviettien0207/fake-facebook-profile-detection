from selenium import webdriver
from login_fb import login

def main():
    # open browser and disable notification
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications" : 2}
    chrome_options.add_experimental_option("prefs",prefs)

    browser = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=chrome_options)

    # đăng nhập
    login(browser)


    # close browser
    browser.close()
    
if __name__ == '__main__':
    main()