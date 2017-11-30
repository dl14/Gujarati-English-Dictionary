# -*- coding: utf-8 -*-
from selenium import webdriver
from bs4 import BeautifulSoup

#import unittest, time, re
import urllib
#import mechanize

def scrape_lexicon(searchword):
    definitions = []
    if not searchword:
        print("empty search word")
    else:
        base_url = "http://www.gujaratilexicon.com/dictionary/gujarati-to-english/"
        new_url = base_url+searchword

        htmlGL = urllib.urlopen(new_url.encode('utf-8')).read()
        soupGL = BeautifulSoup(htmlGL, "html.parser")
        defs = ''
        for meaning in soupGL.find_all("div", class_="meaning"):
            defs += meaning.text
        definitions = defs.split(";")
    return definitions

def scrape_shabdakosh(searchword):
    definitions = []
    if not searchword:
        print("empty search word")
    else:

        base_url = "http://www.shabdkosh.com/gu/translate?e="
        new_url = base_url+searchword+"&l=gu"
        
        #driver = webdriver.Firefox()
        #driver.get(new_url)
        #time.sleep(10)

        htmlSK = urllib.urlopen(new_url.encode('utf-8')).read()
        soupSK = BeautifulSoup(htmlSK, "html.parser")
        #soupSK = BeautifulSoup(driver.page_source)
        for meaning in soupSK.find_all("a", class_="l"):
            u_meaning = meaning.encode('unicode-escape')
            if "\u" in u_meaning:
                break
            definitions.append(meaning.text)
    return definitions

    '''
    base_url = "http://translate.google.com/#auto/en/"
    new_url = base_url+searchword

    browser = mechanize.Browser()
    browser.set_handle_robots(False)
    browser.addheaders = [('user-agent', 'Chrome')]

    htmlT = browser.open(new_url.encode('utf-8')).read()
    print htmlT
    soupT = BeautifulSoup(htmlT, "html.parser")

    definitions.append("Google Translate:")
    print "Google Translate: "
    for meaning in soupT.find_all("div", class_="gt-baf-cell"):
        print meaning
        #f.write(meaning.text)
        #print meaning.text
        definitions.append(meaning.text)
    '''
