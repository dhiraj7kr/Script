from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def get_google_results(query):
    # Setup Chrome driver
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    try:
        # Open Google
        driver.get("https://www.google.com")

        time.sleep(2)

        # Accept cookies (may appear in some regions)
        try:
            accept_btn = driver.find_element(By.XPATH, "//button[contains(text(),'I agree') or contains(text(),'Accept all')]")
            accept_btn.click()
        except:
            pass

        # Find search box
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys(query)
        search_box.send_keys(Keys.RETURN)

        time.sleep(2)

        results = []

        # Google result containers
        boxes = driver.find_elements(By.CSS_SELECTOR, "div.tF2Cxc")

        for box in boxes:
            try:
                title_element = box.find_element(By.TAG_NAME, "h3")
                link_element = box.find_element(By.TAG_NAME, "a")

                title = title_element.text
                link = link_element.get_attribute("href")

                # Snippet (may vary)
                try:
                    snippet = box.find_element(By.CSS_SELECTOR, "div.VwiC3b").text
                except:
                    snippet = ""

                results.append({
                    "title": title,
                    "link": link,
                    "snippet": snippet
                })

            except:
                continue

        return results

    finally:
        driver.quit()


if __name__ == "__main__":
    query = input("Enter search query: ")
    results = get_google_results(query)

    print("\n===== SEARCH RESULTS =====\n")

    for i, r in enumerate(results, start=1):
        print(f"{i}. {r['title']}")
        print(r["link"])
        print(r["snippet"])
        print("-" * 60)
