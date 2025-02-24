# dynamic webpages

from bs4 import BeautifulSoup
import os


test_file = open(os.getcwd() + "/test.html")
soup = BeautifulSoup(test_file)
print(soup.find(id="test").get_text())