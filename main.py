from controller import *
from bs4 import BeautifulSoup
from lxml import etree
import time
import json
from lxml import html
import re
from app import *
from model import *
from datetime import datetime
import random
import asyncio
import threading


def find_inner_divs(element):
  for child in element.children:
      yield child

def find_all_games(html_code, is_cs):
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
                    new1 = j
                    try:
                        try:
                            new = new.findChildren("div" , recursive=False)[2]
                            timee = new.findChildren("div" , recursive=False)[1].text
                            datee= new.findChildren("div" , recursive=False)[2].text
                            datee =  str(datetime.now().strftime("%d.%m.%Y")) if datee == "СЕГОДНЯ" else datee
                                
                        except Exception as e:
                            # print(1, e)
                            try:
                                new = new1.findChildren("div" , recursive=False)[2]
                                timee = new.findChildren("div" , recursive=False)[0].text
                                datee= new.findChildren("div" , recursive=False)[1].text
                                datee =  str(datetime.now().strftime("%d.%m.%Y")) if datee == "СЕГОДНЯ" else datee
                                
                            except Exception as e:
                                print("1111", new)
                                print(2, e)
                                timee = "10:10"
                                datee = "10.10.1010"
                        k = j
                        k = k.findChildren("div" , recursive=False)[6]
                        k = k.findChildren("div" , recursive=False)[0]
                        k1 = k.findChildren("div" , recursive=False)[0]
                        k2 = k.findChildren("div" , recursive=False)[-1]
                        try:
                            kdraw = k.findChildren("div" , recursive=False)[1]
                            scoredraw = kdraw.findChildren("div" , recursive=False)[0].text
                        except Exception as e:
                            kdraw = scoredraw = 0
                        score1 = k1.findChildren("div" , recursive=False)[0].text
                        score2 = k2.findChildren("div" , recursive=False)[0].text
                        scoredraw = 0 if score2 == scoredraw else scoredraw
                        j = j.findChildren("div" , recursive=False)[4] 
                        j = j.findChildren("div" , recursive=False)[0]
                        
                        name1 = j.findChildren("div" , recursive=False)[0].text
                        if name1 == "":
                            name1 = j.findChildren("div" , recursive=False)[1].text
                        draw = j.findChildren("div" , recursive=False)[-2].text
                        
                        name2 = j.findChildren("div" , recursive=False)[-1].text
                        list_small.append((name1, name2,score1, score2,timee, datee, draw, scoredraw))
                    except Exception as e:
                        print(3, e)
                        pass
                dict_big[nameofgames] = list_small
            except Exception as e:
                print(4, e)
                pass
        for key, values in dict_big.items():
            for value in values:
                add_game(key, value[0], value[1], value[2], value[3], value[4], value[5],value[6],value[7], is_cs)
        return dict_big
    except Exception as e:
        print(5, e)
        return None



def open_url(driver, url, is_cs=False):
    try:
    # if True:
        driver.get(url)
        html_code = driver.page_source 
        driver.switch_to.frame(0)
        while True: 
            # send_massage_new_parsing(url) 
            time.sleep(10)
            random_element = random.choice([1,2])
            # random_element = 2
            if random_element==1:
                driver.execute_script("window.scrollTo(0, 0);")
            else:
                screen_height =driver.execute_script("return window.innerHeight;")
                scroll_height = driver.execute_script("return document.body.scrollHeight;")

                # # Прокручиваем до 50%
                # driver.execute_script("window.scrollTo(0, {0});".format(scroll_height * 0.5))
                # time.sleep(4)

                # Прокручиваем до 60%
                driver.execute_script("window.scrollTo(0, {0});".format(scroll_height * 0.6))
                time.sleep(4)

                # # Прокручиваем до 70%
                driver.execute_script("window.scrollTo(0, {0});".format(scroll_height * 0.7))
                time.sleep(4)

                # Прокручиваем до 80%
                driver.execute_script("window.scrollTo(0, {0});".format(scroll_height* 0.8))
                time.sleep(4)


            time.sleep(3)
            html_code = driver.page_source
            find_all_games(html_code, is_cs)
            time.sleep(10)
        # driver.quit()
    except Exception as e:
        pass
    #     send_message_error_to_channel(url)

async def main():

    url1 = 'https://betboom.ru/esport?pageRoute=timeline&type=upcoming&sportId=3'
    url2 = 'https://betboom.ru/esport?pageRoute=timeline&type=upcoming&sportId=2'
    thread1 = threading.Thread(target=open_url, args=(driver1, url1, url1[-1] == "3"))
    thread2 = threading.Thread(target=open_url, args=(driver2, url2, url2[-1] == "3"))

    # await asyncio.gather(
    #     open_url(driver1, url1, url1[-1]=="3"),
    #     open_url(driver2, url2, url2[-1]=="3")
    # )
    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()


    
    
if __name__ == "__main__":
    asyncio.run(main())
    # try:
    #     driver.get('https://betboom.ru/esport?pageRoute=timeline&type=upcoming&sportId=3')
    #     html_code = driver.page_source 
    #     driver.switch_to.frame(0)
    #     while True:  
    #         time.sleep(10)
    #         html_code = driver.page_source
    #         find_all_games(html_code)
            
    #         time.sleep(10)
    #     # driver.quit()
    # except Exception as e:
    #     send_message_error_to_channel()
