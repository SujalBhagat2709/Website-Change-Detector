import requests

def fetch_page(url):

    response = requests.get(url)

    return response.text


if __name__ == "__main__":

    url = input(
        "Enter Website URL: "
    )

    content = fetch_page(url)

    print(
        f"Downloaded "
        f"{len(content)} characters"
    )