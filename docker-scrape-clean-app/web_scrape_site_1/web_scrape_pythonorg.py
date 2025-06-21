import requests
from bs4 import BeautifulSoup

base_url = "https://www.python.org/jobs/?page={}"
headers = {"User-Agent": "Mozilla/5.0"}

page = 1
all_jobs = []

while True:
    url = base_url.format(page)
    response = requests.get(url, headers=headers)
    print(f"Scraping page {page}...")

    if response.status_code != 200:
        print(f"Failed to fetch page {page}. Status code: {response.status_code}")
        break

    soup = BeautifulSoup(response.text, "html.parser")
    listings = soup.select("ol.list-recent-jobs li")

    if not listings:
        print("No more jobs found. Stopping.")
        break

    for job in listings:
        title_tag = job.select_one("h2.listing-company a")
        company_tag = job.select_one("span.listing-company-name")
        location_tag = job.select_one("span.listing-location")

        title = title_tag.text.strip() if title_tag else "N/A"
        company = company_tag.text.strip() if company_tag else "N/A"
        location = location_tag.text.strip() if location_tag else "N/A"
        link = "https://www.python.org" + title_tag["href"] if title_tag else "N/A"

        job_data = {
            "company": company,
            "title": title,
            "location": location,
            "link": link
        }

        all_jobs.append(job_data)

    page += 1  # move to next page

# 👇 show sample
for job in all_jobs:
    print(job)
    print("-" * 50)

