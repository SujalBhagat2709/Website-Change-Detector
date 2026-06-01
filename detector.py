import time

from monitor import fetch_page

url = input(
    "Enter Website URL: "
)

print(
    "\nMonitoring Started..."
)

previous_content = fetch_page(url)

while True:

    time.sleep(30)

    current_content = fetch_page(url)

    if current_content != previous_content:

        print(
            "\n🚨 WEBSITE CHANGED!"
        )

        print(
            f"Detected at "
            f"{time.strftime('%H:%M:%S')}"
        )

        previous_content = current_content

    else:

        print(
            "No Change Detected"
        )