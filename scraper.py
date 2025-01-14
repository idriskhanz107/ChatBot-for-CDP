import requests
from bs4 import BeautifulSoup

def scrape_segment():
    url = "https://segment.com/docs/?ref=nav"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise HTTP errors
        soup = BeautifulSoup(response.content, "html.parser")
        links = [(a.text.strip(), a["href"]) for a in soup.find_all("a", href=True)]
        return links
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}")
        return []

if __name__ == "__main__":
    segment_links = scrape_segment()
    print(f"Found {len(segment_links)} links in Segment documentation")
