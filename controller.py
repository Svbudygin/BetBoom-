import random
import selenium_dolphin as dolphin
from selenium_dolphin import DolphinAPI, STABLE_CHROME_VERSION
from selenium.webdriver.chrome.options import Options
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


service = Service(executable_path='/Users/sergeybudygin/bet_boom_parser/chromedriver')
driver1 = webdriver.Chrome(service=service)
driver2 = webdriver.Chrome(service=service)
# driver.get("https://www.google.com")