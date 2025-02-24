# dynamic webpages

from selenium import webdriver 
from selenium.webdriver.chrome.service import Service as ChromeService 
from webdriver_manager.chrome import ChromeDriverManager 
 
url = 'https://angular.io/' 
#url = "https://www.vattenfall.nl/service/mijn-vattenfall/vf/verbruik"

driver = webdriver.Chrome(service=ChromeService( 
	ChromeDriverManager().install())) 
 
driver.get(url) 
 
print(driver.page_source)