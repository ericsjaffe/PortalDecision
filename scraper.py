import requests
from bs4 import BeautifulSoup
import re

def parse_transfer_info(headline):
    """
    Tries to extract from_school and to_school from a headline string.
    Returns a dictionary with inferred data.
    """
    # Example: "Virginia transfer pitcher Tomas Valincius commits to Mississippi State"
    to_school_match = re.search(r'commits? to ([\w\s\'\-]+)', headline, re.IGNORECASE)
    from_school_match = re.search(r'([A-Z][\w\s]+) transfer', headline)

    return {
        "from_school": from_school_match.group(1).strip() if from_school_match else "Unknown",
        "to_school": to_school_match.group(1).strip() if to_school_match else "Unknown"
    }

def get_transfer_updates():
    url = "https://www.on3.com/transfer-portal/"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    updates = []
    for article in soup.select("article")[:10]:  # limit to 10
        title_tag = article.select_one("h3")
        time_tag = article.select_one("span")
        link_tag = article.find("a", href=True)

        title = title_tag.text.strip() if title_tag else "Unnamed Player"
        link = link_tag["href"] if link_tag else "#"
        time_text = time_tag.text.strip() if time_tag else ""

        parsed = parse_transfer_info(title)

        updates.append({
            "title": title,
            "sport": "Unknown",  # still hard to pull reliably from On3
            "from_school": parsed["from_school"],
            "to_school": parsed["to_school"] or time_text,
            "link": link
        })

    return updates
