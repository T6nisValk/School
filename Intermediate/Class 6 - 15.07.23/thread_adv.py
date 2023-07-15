# Download example
import time
import threading
# Pip install requests.
import requests

urls = [
    "https://www.google.com",
    "https://www.amazon.com",
    "https://www.microsoft.com",
    "https://www.facebook.com"
]


def fetch_url(url):
    response = requests.get(url)
    print(f"{response.status_code}: {url}")


def procedural():
    start = time.time()
    for url in urls:
        fetch_url(url)
    end = time.time()
    print(f"Procedural took: {end - start} secs")


def using_threads():
    start = time.time()
    threads = []
    for url in urls:
        thread = threading.Thread(target=fetch_url, args=(url,))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
    end = time.time()
    print(f"Using threads took: {end - start} secs")


procedural()
using_threads()
