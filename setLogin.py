import myPkgs.Scraper as Sc

# ChromeOptionsを設定
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

scraper = Sc.Scraper()

XPathLogout = '//*[@id="Nav"]/nav/div/div[3]/ul[2]/li/div/div/a[4]'

scraper.getPage("https://mangasee123.com/user/subscription.php")


print("please login.")

try:
    element = WebDriverWait(scraper.driver, 60*15).until(
        EC.presence_of_element_located((By.XPATH, XPathLogout))
    )
finally:

    scraper.driver.quit()
