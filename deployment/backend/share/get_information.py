import urllib.request
from urllib.parse import urlparse
from bs4 import BeautifulSoup

def get_information(url):
    response = urllib.request.urlopen(url)
    soup = BeautifulSoup(response,'html.parser',
                            from_encoding=response.info().get_param('charset'))
    information = []
    for img in soup.findAll('meta'):
        information.append(img.get('content'))
    return information[21], information[20]
   

