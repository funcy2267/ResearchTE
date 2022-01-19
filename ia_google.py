import requests
import os
import io

ProjectPath = io.open(".\\ProjectPath.txt", "r", encoding="utf-8").read()

site_source = ProjectPath+"\\out\\ia_google-site-source.html"
site_cleaned = ProjectPath+"\\out\\ia_google-site-cleaned.html"
site_tidy = ProjectPath+"\\out\\ia_google-site-tidy.html"
result_source = ProjectPath+"\\out\\ia_google-result-source.txt"
output = ProjectPath+"\\out\\ia_google-output.txt"

def set_lang(code):
    global lang_code
    lang_code = code

def save_source(search_query):
    print("Saving Google search results...")
    with io.open(site_source, "w", encoding="utf-8") as file:
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
                   "Accept-Language": lang_code}
        file.write(requests.get("http://www.google.com/search?q="+search_query.replace(" ", "+"), headers=headers).text)
        file.close()
    print("Search results saved.")

def clean_source():
    print("Cleaning search results...")
    delete_list = ["<g-", "<title-with-lhs-icon>"]
    with io.open(site_source, "r", encoding="utf-8") as f_in, io.open(site_cleaned, "w", encoding="utf-8") as f_out:
        for line in f_in:
            for word in delete_list:
                line = line.replace(word, "")
            f_out.write(line)
    os.system(ProjectPath+"\\bin\\tidy.exe -o "+site_tidy+" "+site_cleaned)
    print("Search results cleaned.")

def extract_result():
    for line_count, l in enumerate(io.open(site_tidy, "r", encoding="utf-8")):
        pass
    print("Searching Google results for zero-click answer...")
    found_ia = 0
    for i in range(line_count+1):
        line = io.open(site_tidy, "r", encoding="utf-8").readlines()[i]
        if '<span class="hgKElc">' in line:
            print("Answer found.")
            found_ia = 1
            write_result(i)
            break
    if found_ia != 1:
        print("Zero-click answer cannot be found. Aborting...")
        clean_source_files()

def write_result(i):
    print("Processing answer...")
    with io.open(result_source, "w", encoding="utf-8") as file:
       file.write("")
       file.close()
    while True:
        line = io.open(site_tidy, "r", encoding="utf-8").readlines()[i]
        with io.open(result_source, "a", encoding="utf-8") as file:
            file.write(line)
            file.close()
        i = i + 1
        if '/span' in line:
            break
    print("Answer processed.")

def clean_result():
    print("Cleaning source answer...")
    delete_list = ['"kX21rb">', "<span class=", '"ILfuVd">', '"hgKElc">', "<b>", "</b>", "</span>", "</div>"]
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
    os.remove(site_cleaned)
    os.remove(site_tidy)
    os.remove(result_source)
    print("Source files cleaned.")
