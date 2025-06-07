import requests
from bs4 import BeautifulSoup

def get_transfer_updates():
    url = "https://www.on3.com/transfer-portal/"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    updates = []

    for article in soup.select("article")[:10]:  # limit to 10 items
        name_el = article.select_one("h3")
        detail_el = article.select_one("span")
        link_el = article.find("a", href=True)

        name = name_el.text.strip() if name_el else "Unnamed Player"
        detail = detail_el.text.strip() if detail_el else ""
        link = link_el["href"] if link_el else "#"

        updates.append({
            "title": name,
            "sport": "Unknown",           # placeholder — update if you can parse sport
            "from_school": "Unknown",     # placeholder — update if info available
            "to_school": detail,
            "link": link
        })

    return updates
