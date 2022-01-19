import requests
import re
import json
import wikipedia

def set_lang(code):
    global lang_code
    lang_code = code

def search_google(query):
    try:
        os.remove(site_cleaned)
        os.remove(site_tidy)
    except:
        pass
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
               "Accept-Language": lang_code}
    source = requests.get("http://www.google.com/search?q="+query.replace(" ", "+"), headers=headers).text.split('<')
    result = ""
    for i in range(len(source)):
        if 'span class="hgKElc">' in source[i]:
            while '/span' not in source[i]:
                result = result + source[i]
                delete_list = ['/b>', 'b>', 'span class="hgKElc">']
                for word in delete_list:
                    result = result.replace(word, "")
                i=i+1
            result = result.replace('\n', " ").strip()
            break
    return(result)

def search_duckduckgo(query):
    r = requests.get("https://api.duckduckgo.com",
        params = {
            "q": query,
            "format": "json"
        },
        headers = {
            "Accept-Language": lang_code
        })
    data = r.json()
    return(data["Abstract"])

#Credits: https://github.com/deepanprabhu/duckduckgo-images-api/blob/master/duckduckgo_images_api/api.py
def search_duckduckgo_img(keywords, load_results):
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

    print("Writing images URLs from DuckDuckGo...")
    result = []
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
                result = result + [format(obj["image"])]
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
    return(result)

def search_wikipedia(query, paragraphs):
    wikipedia.set_lang(lang_code[:2])
    print("Saving Wikipedia page content...")
    source = wikipedia.page(query).content.split('\n')
    result = []
    i = 0
    for line in source:
        if line != '\n' and line != "" and "=" not in line:
            result = result + [line.strip()]
            i=i+1
        if line != '\n' and line != "" and "=" in line[0]:
            result = result + ["# "+line.replace("=", "").strip()]
        if i >= paragraphs:
            break
    return(result)
