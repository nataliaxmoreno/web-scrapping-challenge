from bs4 import BeautifulSoup as bs
import requests
import pymongo
from splinter import Browser
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
import time
from datetime import datetime as dt
from dateutil.parser import parse


def scrape():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    # URL of page to be scraped
    url = 'https://redplanetscience.com/'
    browser.visit(url)
    html = browser.html
    soup = bs(html, 'html.parser')
    # Retrieve the parent divs for all articles
    results = soup.find_all('div', class_='col-md-8')
    mars1=[]
    # loop over results to get the data
    for result in results:
        # scrape the titles and previews 
        
        news_title = result.find('div', class_='content_title').text
        news_p= result.find('div', class_='article_teaser_body').text

        mars = {
            'title': news_title,
            'preview': news_p}
        mars1.append(mars)

    image_url = 'https://spaceimages-mars.com/'
    browser.visit(image_url)
    time.sleep(2)
    html2 = browser.html
    soup = bs(html2, 'html.parser')
    results = soup.find_all('div', class_='header')
    # loop over results to get the data
    for result in results:
        image_address = image_url + result.find('img', class_='headerimage fade-in')['src']
        print(image_address)
        url = 'https://galaxyfacts-mars.com/'
    tables = pd.read_html(url)
    table= tables[0]
    table1=table.rename(columns=table.iloc[0]).drop(table.index[0]) 
    html_table1 = table1.to_html().replace('\n', '')
    #html_table1
    Table2= tables[1]
    table2=Table2.rename(columns=Table2.iloc[0]).drop(Table2.index[0]) 
    html_table2 = table2.to_html().replace('\n', '')
    #html_table2
    Marsurl = 'https://marshemispheres.com/'
    browser.visit(Marsurl)
    time.sleep(2)
    html = browser.html
    soup = bs(html, 'html.parser')
    mars_hemispheres = soup.find_all('div', class_='item')

    hemisphere_image_urls = []

    # Iterate through each hemisphere data
    for hemisphere in mars_hemispheres:
        title=hemisphere.find('h3').text.strip()
        image_url = [Marsurl+hemisphere.find('a')['href']]
        for image in image_url:
            browser.visit(image)
            time.sleep(2)
            html = browser.html
            soup = bs(html, 'html.parser')
            lastlink =Marsurl+soup.find('img', class_='wide-image')['src']

        # Create Dictionary to store title and url info
        image_dict = {
            'title': title,
            'img_url': lastlink}
        
        hemisphere_image_urls.append(image_dict)


    # FINAL DICTIONARY FOR MONGO
    marsfinal={'marsnews': mars1[0],
    'table1': html_table1,
    'table2':html_table2,
    'image1':image_address,
    'hemispheres':hemisphere_image_urls
    }
    browser.quit()

    return marsfinal 

#test=scrape()
#print(test)