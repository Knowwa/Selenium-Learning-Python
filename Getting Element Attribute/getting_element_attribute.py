from cmd import IDENTCHARS
import pdb
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('http:Demostore.supersqa.com')

#example 1 (place holder)
search_field = driver.find_element(By.ID, ("woocommerce-product-search-field-0"))
place_holder = search_field.get_attribute('placeholder')

if place_holder != 'Search products…':
    print("Placeholder for search field is not as expected.")
else:
    print("PASS!")

#use pdb to search find attributes in search field. <dir(search_field)> shows all available methods and use it to find get_attribute method.
#Now use search_field.get_attribute('class')

#Example 2 (See which tab is selected)
#first click on myaccount
# my_acct = driver.find_element(By.CSS_SELECTOR,("#site-navigation > div:nth-child(2) > ul > li.page_item.page-item-9 > a"))
# my_acct.click()
# nav_items = driver.find_elements(By.CSS_SELECTOR,("ul.nav-menu li"))

# for items in nav_items:
#     item_class = items.get_attribute('class')
#     if 'current_page_item' in item_class:
#         print(f"Current Tab: {items.text}")


#example_get link URL
product_link = driver.find_element(By.CSS_SELECTOR, ("#main > ul > li.product.type-product.post-24.status-publish.first.instock.product_cat-music.has-post-thumbnail.downloadable.virtual.purchasable.product-type-simple a"))
product_url = product_link.get_attribute('href')
print(f"The URL for product: {product_url}")
