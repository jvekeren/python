# dynamic webpages

import asyncio
from bs4 import BeautifulSoup
from pyppeteer import launch
import os


async def main():
    # Launch the browser
    browser = await launch()

    # Open a new browser page
    page = await browser.newPage()

    # Create a URI for our test file
    page_path = "file://" + os.getcwd() + "/test.html"

    # Open our test file in the opened page
    await page.goto(page_path)
    page_content = await page.content()

    # Process extracted content with BeautifulSoup
    soup = BeautifulSoup(page_content)
    print(soup.find(id="test").get_text())

    # Close browser
    await browser.close()


asyncio.get_event_loop().run_until_complete(main())