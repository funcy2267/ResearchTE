import io
import os
import def_apis

ProjectPath = io.open(".\\ProjectPath.txt", "r", encoding="utf-8").read()

plan = ProjectPath+"\\plan.txt"
ia_google_output = ProjectPath+"\\out\\ia_google-output.txt"
ia_duckduckgo_output = ProjectPath+"\\out\\ia_duckduckgo-output.txt"
img_duckduckgo_output = ProjectPath+"\\out\\img_duckduckgo-output.txt"
wikipedia_output = ProjectPath+"\\out\\wikipedia-output.txt"
markdown_output = ProjectPath+"\\out\\output.md"
word_output = ProjectPath+"\\out\\output.docx"

def markdown_generator():
    print("Generating Markdown file...")
    with io.open(markdown_output, "w", encoding="utf-8") as file:
        file.write("")
        file.close()
    for line_count, l in enumerate(io.open(plan, "r", encoding="utf-8")):
        pass
    for i in range(line_count+1):
        line = io.open(plan, "r", encoding="utf-8").readlines()[i].split(",")
        if line[0] == "lang_code":
            lang_code = line[1].replace("\n", "")
            print("Setting language to: "+lang_code)
            def_apis.set_lang(lang_code)
        if line[0] == "1":
            def_apis.search_google(line[1])
            with io.open(markdown_output, "a", encoding="utf-8") as file:
                try:
                    file.write("\n# "+line[1].replace('"', "").replace("\n", "")+"  \n")
                    file.write(io.open(ia_google_output, "r", encoding="utf-8").read()+"  \n")
                    file.close()
                except FileNotFoundError:
                    pass
        if line[0] == "2":
            def_apis.search_duckduckgo(line[1])
            with io.open(markdown_output, "a", encoding="utf-8") as file:
                try:
                    file.write("\n# "+line[1].replace('"', "").replace("\n", "")+"  \n")
                    file.write(io.open(ia_duckduckgo_output, "r", encoding="utf-8").read()+"  \n")
                    file.close()
                except FileNotFoundError:
                    pass
        if line[0] == "3":
            def_apis.search_duckduckgo_img(line[1],int(line[2]))
            for img_duckduckgo_line_count, l in enumerate(io.open(img_duckduckgo_output, "r", encoding="utf-8")):
                pass
            with io.open(markdown_output, "a", encoding="utf-8") as file:
                try:
                    for i in range(img_duckduckgo_line_count+1):
                        file.write("![]("+io.open(img_duckduckgo_output, "r", encoding="utf-8").readlines()[i].replace("\n", "")+")  \n")
                    file.write("*"+line[1].replace('"', "")+"*"+"  \n")
                    file.close()
                except (UnboundLocalError, FileNotFoundError):
                    pass
        if line[0] == "4":
            def_apis.search_wikipedia(line[1],int(line[2]))
            for wikipedia_line_count, l in enumerate(io.open(wikipedia_output, "r", encoding="utf-8")):
                pass
            with io.open(markdown_output, "a", encoding="utf-8") as file:
                try:
                    file.write("\n# "+line[1].replace('"', "").replace("\n", "")+"  \n")
                    for i in range(wikipedia_line_count+1):
                        file.write(io.open(wikipedia_output, "r", encoding="utf-8").readlines()[i].replace("\n", "")+"  \n")
                    file.close()
                except (UnboundLocalError, FileNotFoundError):
                    pass
    print("Markdown file generated.")

def convert_md_to_docx():
    print("Converting Markdown to docx...")
    os.system(ProjectPath+"\\bin\\pandoc.exe -f markdown -t docx "+markdown_output+" -o "+word_output)
    print("Converted.")

def clean_source_files():
    print("Cleaning source files...")
    try:
        os.remove(ia_google_output)
    except FileNotFoundError:
        pass
    try:
        os.remove(ia_duckduckgo_output)
    except FileNotFoundError:
        pass
    try:
        os.remove(img_duckduckgo_output)
    except FileNotFoundError:
        pass
    try:
        os.remove(wikipedia_output)
    except FileNotFoundError:
        pass
    try:
        os.remove(markdown_output)
    except FileNotFoundError:
        pass
    print("Source files cleaned.")

markdown_generator()
convert_md_to_docx()
clean_source_files()
