from selenium import webdriver

#Open Edge webdriver and navigate to the page
driver = webdriver.PhantomJS()
driver.get('http://econpy.pythonanywhere.com/ex/001.html')

#Extract the data
buyers = driver.find_elements_by_xpath('//div[@title="buyer-name"]')
prices = driver.find_elements_by_xpath('//span[@class="item-price"]')

#Print buyers and prices
num_page_items = len(buyers)
for i in range(num_page_items):
    print(buyers[i].text + " : " + prices[i].text)

#close driver
driver.quit()
