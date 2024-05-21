from playwright.sync_api import sync_playwright


def extract(base_url, page_nr):
    url = base_url + "?page=" + str(page_nr)
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(url, wait_until="networkidle")
        # if (url != page.url) & (base_url != page.url & page_nr!=1):
        #     return None
        # else:
        #     return page.content()
        if (page.url == url) | (page_nr == 1):
            return page.content()
        else:
            return None