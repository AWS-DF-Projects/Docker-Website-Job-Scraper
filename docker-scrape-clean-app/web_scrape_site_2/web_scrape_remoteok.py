import requests
from bs4 import BeautifulSoup

url = "https://remoteok.com/remote-dev+aws+python-jobs"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.91 Safari/537.36"
}

job_listings = []

response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    jobs = soup.find_all("tr", class_="job")  # This is the key change

    for job in jobs:
        title_tag    = job.find("h2")
        company_tag  = job.find("h3")
        location_tag = job.find("div", class_="location")
        link         = job.get("data-href")

        job_data = {
            "title": title_tag.text.strip() if title_tag else "N/A",
            "company": company_tag.text.strip() if company_tag else "N/A",
            "location": location_tag.text.strip() if location_tag else "N/A",
            "link": f"https://remoteok.com{link}" if link else "N/A"
        }

        job_listings.append(job_data)

    for job in job_listings:
        print(job)
        print("-" * 50)

else:
    print(f"Failed to fetch page. Status code: {response.status_code}")
