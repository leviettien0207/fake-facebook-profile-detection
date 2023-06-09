import requests
from share.extensions.exception import ErrorCode1001

format_link_fb_1 = 'https://www.facebook.com/'
format_link_fb_2 = 'www.facebook.com/'
format_link_fb_3 = 'facebook.com/'
def check_link_fb(url):
    if (not url.startswith(format_link_fb_1) 
        and not url.startswith(format_link_fb_2) 
        and not url.startswith(format_link_fb_3)):
        raise ErrorCode1001()
    return 
   