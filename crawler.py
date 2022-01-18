from selenium import webdriver
import time
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup 
import requests
import re
import copy


class LinkedInData:
    """Crawl data from LinkedIn webpage
    
    jobKeyword:   job type name
    timeCrawl:    time for scrolling down the webpages
    headers:      default
    url:          corresponding LinkedIn url for job crawling
    wd:           use Safari webdriver
    linkdf:       dataframe for storing basic information of crawled data
    
    Method:
    getBasic():   crawl job basic information: tile, company, postdate, joblink for further information crawling
    """
    def __init__(self, jobKeyword, timeCrawl=600):
        self.jobKeyword = jobKeyword
        self.timeCrawl = timeCrawl
        self.headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
        'Connection': 'close'}
        self.url = 'https://www.linkedin.com/jobs/search/?keywords='+jobKeyword+'&location=Hong+Kong'
        self.wd = webdriver.Safari()
        self.linkdf = pd.DataFrame()
    
    
    def getBasic(self):
        wd = self.wd
        wd.get(self.url)
        start = time.time()

        
        initialScroll = 0
        finalScroll = 1000
        height = []
        while True:
            wd.execute_script(f"window.scrollTo({initialScroll},{finalScroll})")
            initialScroll = finalScroll
            # not scroll too fast, for better web loading
            finalScroll += 3000
            # record the html page height for judge whether to scroll further
            height.append(wd.execute_script("return document.body.scrollHeight"))

            # stop for 5 secods to wait for data loading and pretend like a human
            time.sleep(5)
            end = time.time()

            # waiting the scrolling, and handle the events: a button for new data loading,
            # or break when all data are loaded to end the crawling
            if len(height)>4:
                if height[-1] == height[-4]: 
                    try: wd.find_element_by_xpath("//button[contains(text(), 'See more jobs')]").click()
                    except: break
            
            # check whether we scroll enough long time as set before
            if round(end - start) > self.timeCrawl:
                break

        job_lists = wd.find_element_by_class_name('jobs-search__results-list')
        jobs = job_lists.find_elements_by_tag_name('li')

        #get job title
        job_title = [job.find_element_by_css_selector('h3').get_attribute('innerText') for job in jobs]
        #get company name
        company_name = [job.find_element_by_css_selector('h4').get_attribute('innerText') for job in jobs]
        #get job location
        location = [job.find_element_by_css_selector('[class="job-search-card__location"]').get_attribute('innerText') for job in jobs]
        #get posted date
        date = [job.find_element_by_css_selector('div>div>time').get_attribute('datetime') for job in jobs]
        #get joblink
        job_link = [job.find_element_by_css_selector('a').get_attribute('href') for job in jobs]

        #quit the webdriver
        wd.quit()

        job_data = pd.DataFrame({'Titile':job_title,
                                 'Company': company_name,
                                 'Location': location,
                                 'Date': date,
                                 'Link': job_link
                                })
        #get the inetgrated information dataframe
        self.linkdf = job_data
        job_data.to_csv(f'{self.jobKeyword}_links.csv')
        print(f'{self.jobKeyword} finished crawling')
        return self.linkdf