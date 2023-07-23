#!/usr/bin/env python
# coding: utf-8

# In[35]:


import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, NoSuchWindowException
from webdriver_manager.chrome import ChromeDriverManager


# In[36]:


def extract_info(driver, xpath):
    try:
        return driver.find_element(By.XPATH, xpath).text
    except NoSuchElementException:
        return 'N/A'


# In[37]:


app_data = []

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://apps.apple.com/us/genre/ios/id36')
time.sleep(10)

try:
    # Select the first category
    first_category = driver.find_element(By.XPATH, '//div[@id="genre-nav"]//li/a')
    first_category.click()
    time.sleep(10)

    # Iterate over all apps on page
    while True:
        try:
            app_elements = driver.find_elements(By.XPATH, "//div[@id ='selectedcontent']//a[@href]")
        except (StaleElementReferenceException, NoSuchWindowException):
            break

        for app_element in app_elements:
            try:
                app_url = app_element.get_attribute("href")
                driver.get(app_url)
                time.sleep(5)

                # Extract necessary information
                name = extract_info(driver, '//h1[@class="product-header__title app-header__title"]')
                price = extract_info(driver, '//li[@class="inline-list__item inline-list__item--bulleted app-header__list__item--price"]')
                rating = extract_info(driver, '//li[@class="product-header__list__item app-header__list__item--user-rating"]')
                quantity =extract_info(driver, '//li[@class="product-header__list__item"]')

                app_data.append([name, price, rating,quantity])
                
                # Navigate back and wait for the page to load
                driver.back()
                time.sleep(5)
            except (StaleElementReferenceException, NoSuchWindowException):
                break
        else:
            break
finally:
    # Write to csv file
    with open('app_store_data.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Price", "Ratings", "Quantity"])
        writer.writerows(app_data)
        


# In[31]:


# first_category = driver.find_element(By.XPATH, '//div[@id="genre-nav"]//li/a')
# first_category.click()
# time.sleep(10)

# app_data = []
# # Iterate over all apps on page
# app_elements = driver.find_elements(By.XPATH, "//div[@id ='selectedcontent']//a[@href]")
# for app_element in app_elements:
#     app_url = app_element.get_attribute("href")
#     driver.get(app_url)
#     time.sleep(10)

#     # Extract necessary information
#     name = extract_info(driver, '//h1[@class="product-header__title app-header__title"]')
#     price_quantity = extract_info(driver, '//li[@class="product-header__list__item"]')
#     rating = extract_info(driver, '//li[@class="product-header__list__item app-header__list__item--user-rating"]')

#     app_data.append([name, price_quantity, rating])

# # Write to csv file
# with open('app_store_data.csv', 'w', newline='', encoding='utf-8') as file:
#     writer = csv.writer(file)
#     writer.writerow(["Name", "Price and Quantity", "Ratings"])
#     writer.writerows(app_data)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


# App store applications
# https://apps.apple.com/us/genre/ios/id36
# Main div
# //div[@id ='genre-nav']

# name
# //h1[@class = 'product-header__title app-header__title']
# price and quantity
# //li[@class="product-header__list__item"]

# rating
# //li[@class="product-header__list__item app-header__list__item--user-rating"]


