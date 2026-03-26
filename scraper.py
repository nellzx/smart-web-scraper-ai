import requests
from bs4 import BeautifulSoup


def scrape_website(url):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
    except Exception as e:
        return f"Request Error: {str(e)}"

    if response.status_code != 200:
        return f"Failed to retrieve the webpage. Status code: {response.status_code}"

    soup = BeautifulSoup(response.text, "html.parser")

    # Remove useless elements
    for tag in soup(["script", "style", "nav", "footer", "header", "button", "aside"]):
        tag.extract()

    # Extract only meaningful text tags
    elements = soup.find_all(["h1", "h2", "h3", "p", "li"])

    text_content = []

    for el in elements:
        text = el.get_text(strip=True)
        if text:
            text_content.append(text)

    clean_text = "\n".join(text_content)

    return clean_text