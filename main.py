import myPkgs.Scraper

# scraping data and save pickle

scraper=myPkgs.Scraper.Scraper()
scraper.setSubscriptionsPage()
scraper.getInfoFromSubScriptions()

# create mailHtml