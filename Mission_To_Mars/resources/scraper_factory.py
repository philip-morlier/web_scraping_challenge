from bs4 import BeautifulSoup as bs
import requests as rq
from splinter import Browser
import pandas as pd
import time

class ScraperFactory():
    
    def __init__(self):
        self.scraper=None

    def mars_news(self):
        executable_path={'executable_path': 'chromedriver.exe'}
        browser=Browser('chrome', **executable_path, headless=False)
        url='https://mars.nasa.gov/news/'
        self.url=url
        browser.visit(url)
        time.sleep(5)
        html=browser.html
        soup=bs(html, 'html.parser')
        title=list(soup.find_all('div',class_='content_title'))
        test=list(soup.find_all('div',class_='article_teaser_body'))
        titl=[]
        for i in range(1,41,1):
            titl.append(title[i].text)
        dict_={}
        for i in range(0,40,1):
            dict_.setdefault(title[i+1].text,test[i].text)
        browser.quit()
        return dict_
        
    def mars_facts(self):
        url='https://space-facts.com/mars/'
        self.url=url
        tables=pd.read_html(url)
        df=tables[0]
        return df
    
    def mars_weather(self):
        url = 'https://twitter.com/marswxreport?lang=en'
        html = rq.get(url) 
        soup = bs(html.text, 'html.parser')
        tweet=soup.find('p',class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").getText()
        return tweet
    
    def mars_image(self):
        executable_path={'executable_path': 'chromedriver.exe'}
        browser=Browser('chrome', **executable_path, headless=False)
        url='https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
        browser.visit(url)
        time.sleep(5)
        html=browser.html
        soup=bs(html, 'html.parser')
        image = (soup.find_all('div', class_='carousel_items')[0].a.get('data-fancybox-href'))
        featured = 'https://www.jpl.nasa.gov'+ image
        browser.quit()
        return featured
    
    def mars_hemispheres(self,name):
        self.name=name
        executable_path={'executable_path': 'chromedriver.exe'}
        browser=Browser('chrome', **executable_path, headless=False)
        url='https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
        browser.visit(url)
        time.sleep(5)
        button=browser.find_by_text(name)
        button.click()
        html=browser.html
        browser.quit()
        soup=bs(html, 'html.parser')
        image=soup.find_all('img')
        target=image[5]['src']
        hemisphere='https://astrogeology.usgs.gov/'+target
        return(hemisphere)

