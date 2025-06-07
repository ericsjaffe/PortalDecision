import requests
from bs4 import BeautifulSoup

def get_transfer_updates():
    url = "https://www.on3.com/transfer-portal/"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    updates = []
    for row in soup.select("article"):
        name = row.select_one("h3")
        school = row.select_one("span")
        if name and school:
            updates.append(f"{name.text.strip()} – {school.text.strip()}")
        if len(updates) >= 10:
            break
    return updates
