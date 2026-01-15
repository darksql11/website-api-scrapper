from seleniumwire import webdriver
import time
from urllib.parse import urlparse

options = {
    'request_storage_base_dir': 'requests'
}

driver = webdriver.Chrome(seleniumwire_options=options)

target_url = 'https://www.bershka.com/'
driver.get(target_url)

time.sleep(10)

endpoints = set()

for request in driver.requests:
    if request.response and request.url.startswith("http"):
        parsed = urlparse(request.url)
        if "api" in parsed.path.lower():
            endpoints.add(request.url)

driver.quit()

with open("api_endpoints.txt", "w", encoding="utf-8") as f:
    for url in endpoints:
        f.write(url + "\n")

print("API endpoints saved.")
