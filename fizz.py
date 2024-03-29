from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

URL = "https://www.the-fizz.com/search/?searchcriteria=BUILDING:THE_FIZZ_HAMBURG_STUDENTS;AREA:HAMBURG"


chrome_options = Options()  
chrome_options.add_argument("--headless") # Opens the browser up in background

with Chrome(options=chrome_options) as browser:
     browser.get(URL)
     found = False
     while not found:
        soup = BeautifulSoup(browser.page_source, 'html.parser')
        applet = soup.find_all("div", {"class":"parameter-not-found alert alert-warning"})
        found = bool(applet)

with open("out/out.html", "w") as f:
    f.write(applet[0].prettify())
