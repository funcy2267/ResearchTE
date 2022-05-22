import io
import os
import platform
import research

PlatformName = platform.system()
PlansPath = 'plans/'
OutputPath = 'output/'

markdown_output = OutputPath+"output.md"
word_output = OutputPath+"output.docx"

def md_gen(plan_file):
    print("Generating Markdown file...")
    plan = io.open(PlansPath+plan_file, "r", encoding="utf-8").read()
    md_endl = '  '
    output = []
    for line in plan.split('\n'):
        try:
            action = line.split(';')[0]
            value1 = line.split(';')[1]
            value2 = int(line.split(';')[2])
        except IndexError:
            pass
        if action == "lang_code":
            research.set_lang(value1)
        if action == "ggl":
            output = output + ["# " + value1]
            output = output + [research.search_google(value1) + md_endl]
        if action == "ddg":
            output = output + ["# " + value1]
            output = output + [research.search_duckduckgo(value1) + md_endl]
        if action == "ddgimg":
            output = output + ["# " + value1]
            for image in research.search_duckduckgo_img(value1, value2):
                output = output + ["![](" + image + ")" + md_endl]
        if action == "wiki":
            output = output + ["# " + value1]
            for paragraph in research.search_wikipedia(value1, value2):
                output = output + [paragraph + md_endl]
    with io.open(markdown_output, "w", encoding="utf-8") as f:
        f.write('\n'.join(output))
        f.close()
    print("Markdown file generated.")

def md_to_docx():
    if PlatformName == "Linux":
        PANDOC_BIN = 'pandoc'
    if PlatformName == "Windows":
        PANDOC_BIN = 'bin/pandoc.exe'
    print("Converting Markdown to docx...")
    subprocess.call([PANDOC_BIN, '-f', 'gfm', '-t', 'docx', markdown_output, '-o', word_output])
    print("Converted.")

def open_result():
    if PlatformName == "Linux":
        subprocess.call(['xdg-open', word_output])
    if PlatformName == "Windows":
        subprocess.call(['start', word_output])

md_gen(input("Plan file: "))
md_to_docx()
open_result()
