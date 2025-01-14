import requests
from bs4 import BeautifulSoup
import json

def scrape_links(base_url, doc_url):
    response = requests.get(doc_url)
    soup = BeautifulSoup(response.content, "html.parser")
    
    links = []
    for a in soup.find_all("a", href=True):
        href = a["href"]
        text = a.text.strip()
        
        # Ensure the link is complete
        if href.startswith("/"):
            href = base_url + href
        
        links.append({"title": text, "url": href})
    return links

if __name__ == "__main__":
    # mParticle Documentation
    mparticle_base = "https://docs.mparticle.com"
    mparticle_docs = "https://docs.mparticle.com/"
    mparticle_links = scrape_links(mparticle_base, mparticle_docs)

    with open("mparticle_links.json", "w") as f:
        json.dump(mparticle_links, f, indent=4)
    print(f"mParticle: {len(mparticle_links)} links saved.")

    # Lytics Documentation
    lytics_base = "https://docs.lytics.com"
    lytics_docs = "https://docs.lytics.com/"
    lytics_links = scrape_links(lytics_base, lytics_docs)

    with open("lytics_links.json", "w") as f:
        json.dump(lytics_links, f, indent=4)
    print(f"Lytics: {len(lytics_links)} links saved.")
