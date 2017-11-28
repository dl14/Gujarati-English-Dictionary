# -*- coding: utf-8 -*-
from selenium import webdriver
from bs4 import BeautifulSoup

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException

#import unittest, time, re
import urllib
#import mechanize

def scrape_definition(searchword):
    definitions = []
    if not searchword:
        print("empty search word")
    else:
        #f = open('def.txt', 'w')
        base_url = "http://www.gujaratilexicon.com/dictionary/gujarati-to-english/"
        new_url = base_url+searchword

        htmlGL = urllib.urlopen(new_url.encode('utf-8')).read()
        soupGL = BeautifulSoup(htmlGL, "html.parser")
        definitions.append("Lexicon:")
        print("Lexicon: ")
        for meaning in soupGL.find_all("div", class_="meaning"):
            definitions.append(meaning.text)

        base_url = "http://www.shabdkosh.com/gu/translate?e="
        new_url = base_url+searchword+"&l=gu"

        htmlSK = urllib.urlopen(new_url.encode('utf-8')).read()
        soupSK = BeautifulSoup(htmlSK, "html.parser")
        definitions.append("\nShabdakosh:\n")
        print("Shabdakosh: ")
        for meaning in soupSK.find_all("a", class_="l"):
            u_meaning = meaning.encode('unicode-escape')
            if "\u" in u_meaning:
                break
            definitions.append(meaning.text)

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
    return definitions
    '''
        #print "INSIDE GLEXI"
        driver = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')
        driver.implicitly_wait(30)
        base_url = "http://www.gujaratilexicon.com/"
        base_url2 = "http://www.gujaratilexicon.com/dictionary/gujarati-to-english/"
        new_url = base_url2+searchword
        print new_url
        content = urllib.urlopen(new_url.encode('utf-8')).read()

        verificationErrors = []
        accept_next_alert = True

        #driver = self.driver
        driver.get(base_url + "/")
        Select(driver.find_element_by_id("selectdictionary")).select_by_visible_text("Gujarati - English")
        driver.find_element_by_id("sbtext").clear()
        driver.find_element_by_id("sbtext").send_keys(searchword)
        driver.find_element_by_id("sbsubmit").click()

        time.sleep(2)

        htmlGL = driver.page_source
        soupGL = BeautifulSoup(htmlGL, "html.parser")
        definitions.append("Lexicon:")
        print "Lexicon: "
        for meaning in soupGL.find_all("div", class_="meaning"):
            definitions.append(meaning.text)
            #f.write(meaning.text)
            #print meaning.text

        driver.get("http://www.shabdkosh.com/gu/")
        driver.find_element_by_id("e").clear()
        driver.find_element_by_id("e").send_keys(searchword)
        driver.find_element_by_xpath("//button[@type='submit']").click()

        time.sleep(2)

        htmlSK = driver.page_source
        soupSK = BeautifulSoup(htmlSK, "html.parser")

        definitions.append("Shabdakosh:")
        print "Shabdakosh: "
        for meaning in soupSK.find_all("a", class_="l"):
            if "%" in meaning.get('href'):
                break
            #f.write(meaning.text)
            #print meaning.text
            definitions.append(meaning.text)

        driver.get("https://www.translate.com/")
        driver.find_element_by_id("detect_button").click()
        time.sleep(2)
        driver.find_element_by_id("source_text").clear()
        time.sleep(2)
        driver.find_element_by_id("source_text").send_keys(searchword)
        time.sleep(2)
        driver.find_element_by_id("translate_button").click()
        time.sleep(2)

        htmlT = driver.page_source
        soupT = BeautifulSoup(htmlT, "html.parser")

        definitions.append("Google Translate:")
        print "Google Translate: "
        for meaning in soupT.find_all("div", {"id": "translation_text"}):
            #f.write(meaning.text)
            #print meaning.text
            definitions.append(meaning.text)

    return definitions
        #print definitions
        #f.close()
    #if __name__ == "__main__":
        #scrape_definition(u"દેવ")
    '''
