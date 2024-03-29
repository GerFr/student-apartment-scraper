from bs4 import BeautifulSoup
import requests

def get_dates(soup):
    data = soup.find("div", {"class":"card-body"}).find_all("p")[:2]
    return {"start": str(data[0]).replace("<p>Mietbeginn:<br/> ","").replace("</p>",""), 
            "end": str(data[1]).replace("<p>Mietende:<br/> ","").replace("</p>","")}


URL = "https://www.urban-living-hamburg.de/mieten"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
stages = soup.find_all("div", {"class":"panel panel-default apartment-object-group apartment-object-group-0"})
dates = get_dates(soup)
print(f"start: {dates['start']}\nend:   {dates['end']}")

filtered_stages = []
for stage in stages:
    apartments = stage.find_all("a", {"data-trigger":"click"})
    data=[]
    for apartment in apartments:
        status = BeautifulSoup(apartment["data-text"], "html.parser").find("span")["class"][0]
        title = apartment["title"]
        data.append({"title":title,"status":status})
    filtered_stages.append(data)

for stage in filtered_stages:
    for room in stage:
        if room["status"] != "unit_occupied":
            print(f"{room["title"]:30} {room["status"]}")





