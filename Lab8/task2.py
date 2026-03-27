import agentql
from playwright.sync_api import sync_playwright
import pandas as pd


data = []
url = "https://scrapeme.live/shop/"



with sync_playwright() as playwright, playwright.chromium.launch(headless=True) as browser:
    page = agentql.wrap(browser.new_page())

    while url:

        page.goto(url)

        QUERY = """
        {
            products[] {
                name
                price
            }
        }
        """
        response = page.query_data(QUERY)

        for product in response['products']:
            data.append(product)

        
        res =page.query_data("{next_page}")
        url=res['next_page']
        print(url)

df = pd.DataFrame(data)
df.to_csv("products_Agentql.csv",index=False)
df.to_excel("products_Agentql.xlsx",index=False)



