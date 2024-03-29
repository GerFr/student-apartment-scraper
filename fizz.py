from bs4 import BeautifulSoup
import time
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

def rooms_available(url:str):
    chrome_options = Options()  
    chrome_options.add_argument("--headless") # Opens the browser up in background

    with Chrome(options=chrome_options) as browser:
        browser.get(url)
        diff = 0
        start = time.time()
        while diff<10:
            soup = BeautifulSoup(browser.page_source, 'html.parser')
            applet = soup.find("div", {"class":"parameter-not-found alert alert-warning"})
            end = time.time()
            diff = end-start
            if applet:
                break
    if applet:
        return not bool(applet), applet.contents[0]
    else:
        return not bool(applet), "unoccupied"

if __name__ == "__main__":
    URL = "https://www.the-fizz.com/search/?searchcriteria=BUILDING:THE_FIZZ_HAMBURG_STUDENTS;AREA:HAMBURG" 
    print(rooms_available(URL))