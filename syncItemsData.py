import requests
from bs4 import BeautifulSoup as bs

DATA_BASE_FILE_NAME = "items.json"
FACTORIO_MAIN_PAGE_URL = "https://wiki.factorio.com/Main_Page"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 YaBrowser/24.4.0.0 Safari/537.36"}

def syncItemsData(path: str):
    session = requests.session()
    mainPage = requests.get(FACTORIO_MAIN_PAGE_URL, headers=headers)
    
    if mainPage.status_code != 200:
        raise requests.ConnectionError("Can't connect to factorio main page")
    
    soup = bs(mainPage.text, "html.parser")
    inventory = soup.find("div", class_="inventory")
    tabs = inventory.find_all("div", class_="tab")
    for tab in tabs:
        # process tab
        pass

syncItemsData(".")
