from controller import driver, dolphin
from bs4 import BeautifulSoup
from lxml import etree
import time
import json
from lxml import html
import re
from app import *
from model import *
from datetime import datetime

def find_inner_divs(element):
  for child in element.children:
      yield child

def find_all_games(html_code):
    try:
        soup = BeautifulSoup(html_code, 'html.parser')
        
        tree = html.fromstring(str(soup))

        result = tree.xpath('//*[@id="__next"]/div[3]/div[2]/div/div[3]/div')
        html_strings = html.tostring(result[0]).decode() 
        soup = BeautifulSoup(html_strings, 'html.parser')
        elements = list(find_inner_divs(soup.div))
        dict_big = {}
        for i in elements:
            try:
                soup = i
                # the name
                i = i.findChildren("div" , recursive=False)[0]
                i = i.findChildren("div" , recursive=False)[0]
                i = i.findChildren("div" , recursive=False)[1]
                nameofgames = i.text 
                list_small = []
                # all info
                lst = soup.find_all('div', attrs={'class': re.compile(r'mt-2.*rounded.*border.*border-timeline/card/border.*bg-timeline/card/background.*p-2')})
                for j in lst:
                    j = j.findChildren("div" , recursive=False)[0]
                    new = j
                    try:
                        try:
                            new = new.findChildren("div" , recursive=False)[2]
                            timee = new.findChildren("div" , recursive=False)[1].text
                            datee= new.findChildren("div" , recursive=False)[2].text
                            datee =  str(datetime.now().strftime("%d.%m.%Y")) if datee == "СЕГОДНЯ" else datee
                                
                        except Exception as e:
                            print(1, e)
                            try:
                                new = new.findChildren("div" , recursive=False)[2]
                                timee = new.findChildren("div" , recursive=False)[0].text
                                datee= new.findChildren("div" , recursive=False)[1].text
                                datee =  str(datetime.now().strftime("%d.%m.%Y")) if datee == "СЕГОДНЯ" else datee
                                
                            except Exception as e:
                                print(2, e)
                                timee = "10:10"
                                datee = "10.10.1010"
                        k = j
                        k = k.findChildren("div" , recursive=False)[6]
                        k = k.findChildren("div" , recursive=False)[0]
                        k1 = k.findChildren("div" , recursive=False)[0]
                        k2 = k.findChildren("div" , recursive=False)[1]
                        score1 = k1.findChildren("div" , recursive=False)[0].text
                        score2 = k2.findChildren("div" , recursive=False)[0].text
                        j = j.findChildren("div" , recursive=False)[4] 
                        j = j.findChildren("div" , recursive=False)[0]
                        name1 = j.findChildren("div" , recursive=False)[0].text
                        name2 = j.findChildren("div" , recursive=False)[1].text
                        list_small.append((name1, name2,score1, score2,timee, datee))
                    except Exception as e:
                        print(3, e)
                        pass
                dict_big[nameofgames] = list_small
            except Exception as e:
                print(4, e)
                pass
        for key, values in dict_big.items():
            for value in values:
                add_game(key, value[0], value[1], value[2], value[3], value[4], value[5])
        return dict_big
    except Exception as e:
        print(5, e)
        return None


if __name__ == "__main__":
    try:
        driver.get('https://betboom.ru/esport?pageRoute=timeline&type=upcoming&sportId=3')
        html_code = driver.page_source 
        driver.switch_to.frame(0)
        while True:  
            time.sleep(10)
            html_code = driver.page_source
            find_all_games(html_code)
            
            time.sleep(10)
        # driver.quit()
    except Exception as e:
        send_message_error_to_channel()
