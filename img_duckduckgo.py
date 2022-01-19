# Credits: https://github.com/deepanprabhu/duckduckgo-images-api/blob/master/duckduckgo_images_api/api.py
import requests
import re
import json
import time
import io

ProjectPath = io.open(".\\ProjectPath.txt", "r", encoding="utf-8").read()

output = ProjectPath+"\\out\\img_duckduckgo-output.txt"

def set_lang(code):
    global lang_code
    lang_code = code

def search(keywords, load_results):
    url = 'https://duckduckgo.com/'
    params = {
    	'q': keywords
    }

    #   First make a request to above URL, and parse out the 'vqd'
    #   This is a special token, which should be used in the subsequent request
    res = requests.post(url, data=params)
    searchObj = re.search(r'vqd=([\d-]+)\&', res.text, re.M|re.I)

    if not searchObj:
        return -1

    headers = {
        'authority': 'duckduckgo.com',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'sec-fetch-dest': 'empty',
        'x-requested-with': 'XMLHttpRequest',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'referer': 'https://duckduckgo.com/',
        'accept-language': lang_code,
    }

    params = (
        ('l', lang_code),
        ('o', 'json'),
        ('q', keywords),
        ('vqd', searchObj.group(1)),
        ('f', ',,,'),
        ('p', '1'),
        ('v7exp', 'a'),
    )

    requestUrl = url + "i.js"

    i = 0
    stop = 0

    with io.open(output, "w", encoding="utf-8") as file:
        file.write("")
        file.close()
    print("Writing images URLs from DuckDuckGo...")
    while True:
        res = requests.get(requestUrl, headers=headers, params=params)
        data = json.loads(res.text)

        #printJson(data["results"], load_results)
        for obj in data["results"]:
            if i < load_results:
                #print(i)
                #print("Width {0}, Height {1}".format(obj["width"], obj["height"]))
                #print("Thumbnail {0}".format(obj["thumbnail"]))
                #print("Url {0}".format(obj["url"]))
                #print("Title {0}".format(obj["title"].encode('utf-8')))
                #print("Image {0}".format(obj["image"]))
                #print("__________")
                write_url(format(obj["image"]))
                i = i + 1
            else:
                stop = 1
        
        if stop == 1:
            break
        
        if "next" not in data:
            print("No more images found.")
            break

        requestUrl = url + data["next"]
    print("Done.")

def write_url(url):
    with io.open(output, "a", encoding="utf-8") as file:
        file.write(url)
        file.write("\n")
        file.close()
