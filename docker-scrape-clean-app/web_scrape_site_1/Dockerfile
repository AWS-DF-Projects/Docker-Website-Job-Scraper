# 1. Use a lightweight base image with Python pre-installed
FROM python:3.11-slim

# 2. Set the working directory INSIDE the container
WORKDIR /app

# 3. Copy your local project files INTO the container
COPY . .

# 4. (Optional) Install dependencies like BeautifulSoup or Requests
RUN pip install -r requirements.txt

# 5. Command to run when container starts (your scraper)
CMD ["python", "web_scrape_pythonorg.py"]
