from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
from selenium import webdriver


# options = webdriver.ChromeOptions()
# options.add_argument('--ignore-certificate-errors')
# options.add_argument("--test-type")
# options.binary_location = "/usr/lib/chromium-browser/chromedriver"
driver = webdriver.Firefox("/usr/local/bin/")
driver.get('https://techcrunch.com/')


# def send_request(url):
#     """sends get request to url and checks to see if the conten is html"""

#     try:
#         with closing(get(url, stream=True)) as resp:
#             if is_good_response(resp):
#                 python_button = driver.find_element_by_class_name(
#                     "load-more ")
#                 python_button.click()
#             return resp.content

#     except RequestException as e:
#         print(f'{url}:{str(e)}')
#         return None

def send_request(url):

    driver.get('https://techcrunch.com/')
    python_button = driver.find_element_by_class_name("load-more ")
    python_button.click()

    return driver.page_source


def is_good_response(resp):
    """returns true if response is html"""
    conten_type = resp.headers['content-Type'].lower()
    return (resp.status_code == 200
            and conten_type is not None
            and conten_type.find('html') > -1)


def get_url(html):
    soup = BeautifulSoup(html)
    urls = []

    data = soup.findAll('a', attrs={'class': 'post-block__title__link'})
    for a in data:
        links = a.get("href")
        urls.append(links)
    return urls


def save_to_file(urls):
    """Save html to a file named index.html"""
    try:
        with open('url.txt', 'w') as file:
            for url in urls:
                file.write(url + "\n")
    except:
        print("ERROR SAVING FILE")


if __name__ == "__main__":
    raw_html = send_request("https://techcrunch.com/")
    print(f"lengh of raw html{len(raw_html)}")
    urls = get_url(raw_html)
    save_to_file(urls)
