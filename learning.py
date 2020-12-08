# -*- coding: utf-8 -*-
    
import re
from bs4 import BeautifulSoup  # pip install bs4 # parse web, obtain data 
import urllib.request, urllib.error # get webpage by URL 
#import xlwt # excel
import json
import sqlite3 

def start():

    print ("\t Instagram Hashtag Scrapper \n")
    tag_base_url = "https://www.instagram.com/explore/tags/"
    post_base_url = "https://www.instagram.com/p/"

    tag_name = input("Please Enter a Hashtag: ")

    tag_url = tag_base_url + tag_name
    
    print (tag_url) # for display only 

    # 1. get webpage sources, store in variable (object)

    html = get_content_url(tag_url)

    soup = BeautifulSoup(html, "html.parser") # parser object

    list_scrpit = soup.find_all("script", type="text/javascript")

    # "window._sharedData = "
    jsonstr = list_scrpit[3].string[20:-1]  # hard coded TODO

    # print (jsonstr)


    # 2. parsing

    infolist = json.loads(jsonstr) # python dict obj 

    #print (infolist)
    
    with open('raw_all.json', 'w', encoding='utf-8') as jsonfile:
        json.dump(infolist, jsonfile, indent=4, ensure_ascii=False)
        
    print(json.dumps(infolist, indent = 4, sort_keys=True)) # for display only 

    print(infolist["entry_data"]["TagPage"][0]["graphql"]["hashtag"]["edge_hashtag_to_media"]["count"])  # for displace only   # edge_hashtag_to_media
    # edge_hashtag_to_top_posts


    # 3. save data
    path = ""


def get_content_url(url): # return page source HTML

    data = bytes(urllib.parse.urlencode({'name': 'user'}), encoding = "utf-8")

    cookie = '''csrftoken=LqWwmIYutdVdjfZs19lC21UJxj328lHe; ds_user_id=145399310; rur=PRN; urlgen="{\"58.182.45.73\": 55430}:1kmHZR:gTUeuOkl2OpGz-awwXp_sjFVPXs"; shbid=9296; shbts=1607340966.1711164; sessionid=145399310%3AAgVenBkUyalwhw%3A24; ig_nrcb=1; ig_did=160650D6-C2A1-47CA-B84F-1CABBEDE7C6C; mid=X0zm8AAEAAEZtMalVoXXLUz_kkgL'''

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36", 
        "Cookie" : cookie 
    }

    request = urllib.request.Request(url=url, data=data, headers=headers, method="POST") # fine to be GET without data 
    
    html = ""

    try:
        response = urllib.request.urlopen(request, timeout = 3)
        html = response.read().decode("utf-8")
        #print(html) # For display only 
    except urllib.error.URLError as e:
        if hasattr(e, "code"): 
            print(e.code)
        if hasattr(e, "reason"): 
            print(e.reason)
    
    return html 
        


    # GET method
    '''
    try: 
        response = urllib.request.urlopen("https://www.instagram.com/p/CGH9G_iAvjN/", timeout = 13) #TODO: 3s timeout? 
        print(response.getheader("Server"))
    except urllib.error.URLError as e: # Exception 
        print ("request time out!")
    '''



if __name__ == "__main__":
    
    start()





'''
def sum (n): 
    if n == 0: 
        return 0
    else: 
        print (n)
        return n + sum (n - 1) 
        
print (sum (10))
'''
'''
list = ['a', 'b', 'c']

for i, k in enumerate(list):
    print ("%d: %s"%(i, k))
'''
