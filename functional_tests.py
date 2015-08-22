#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

binary = FirefoxBinary('/usr/bin/firefox')
browser = webdriver.Firefox(firefox_binary=binary)
browser.get('http://localhost:8000')
assert 'Django' in browser.title


