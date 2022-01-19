import wikipedia
import os
import io

ProjectPath = io.open(".\\ProjectPath.txt", "r", encoding="utf-8").read()

site_content = ProjectPath+"\\out\\wikipedia-content.txt"
output = ProjectPath+"\\out\\wikipedia-output.txt"

def set_lang(code):
    wikipedia.set_lang(code[:2])

def save_content(search_query):
    print("Saving Wikipedia page content...")
    with io.open(site_content, "w", encoding="utf-8") as file:
        try:
            file.write(wikipedia.page(search_query).content)
            file.close()
            print("Page content saved.")
        except wikipedia.exceptions.PageError:
            print("Article not found on Wikipedia.")

def process_content(paragraphs):
    with io.open(output, "w", encoding="utf-8") as file:
        file.write("")
        file.close()
    write_counter = 0
    i = 0
    print("Processing content...")
    while True:
        try:
            line = io.open(site_content, "r", encoding="utf-8").readlines()[i]
        except IndexError:
            print("No more lines.")
            break
        if line != "\n" and "=" not in line:
            with io.open(output, "a", encoding="utf-8") as file:
                file.write(line)
                file.close()
                write_counter = write_counter + 1
        if write_counter >= paragraphs:
            break
        i = i + 1
    print("Content processed.")

def clean_source_files():
    print("Cleaning source files...")
    os.remove(site_content)
    print("Source files cleaned.")
