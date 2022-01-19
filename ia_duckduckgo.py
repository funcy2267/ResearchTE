import requests
import os
import io

ProjectPath = io.open(".\\ProjectPath.txt", "r", encoding="utf-8").read()

site_source = ProjectPath+"\\out\\ia_duckduckgo-site-source.xml"
result_source = ProjectPath+"\\out\\ia_duckduckgo-result-source.txt"
output = ProjectPath+"\\out\\ia_duckduckgo-output.txt"

def set_lang(code):
    global lang_code
    lang_code = code

def save_source(search_query):
    print("Saving DuckDuckGo search results...")
    with io.open(site_source, "w", encoding="utf-8") as file:
        headers = {"Accept-Language": lang_code}
        file.write(requests.get("http://api.duckduckgo.com/?q="+search_query.replace(" ", "+")+"&format=xml", headers=headers).text)
        file.close()
    print("Search results saved.")

def extract_result():
    print("Extracting result from API response...")
    for line_count, l in enumerate(io.open(site_source, "r", encoding="utf-8")):
        pass
    for i in range(line_count+1):
        line = io.open(site_source, "r", encoding="utf-8").readlines()[i]
        if 'AbstractText' in line:
            with io.open(result_source, "w", encoding="utf-8") as file:
                file.write(line)
                file.close()
    print("Result extracted.")

def clean_result():
    print("Cleaning source answer...")
    delete_list = ['<AbstractText>', '</AbstractText>']
    with io.open(result_source, "r", encoding="utf-8") as f_in, io.open(output, "w", encoding="utf-8") as f_out:
        for line in f_in:
            for word in delete_list:
                line = line.replace(word, "").strip()
            f_out.write(line)
            #print(line)
    print("Answer cleaned.")

def clean_source_files():
    print("Cleaning source files...")
    os.remove(site_source)
    os.remove(result_source)
    print("Source files cleaned.")
