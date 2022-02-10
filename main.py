import io
import os
import research

ProjectPath = os.getcwd()
PlansPath = '.\\plans\\'
OutputPath = '.\\out\\'

markdown_output = OutputPath+'output.md'
word_output = OutputPath+'output.docx'

def md_gen(plan_name):
    print("Generating Markdown file...")
    plan = io.open(PlansPath+plan_name, "r", encoding="utf-8").read()
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
    print("Converting Markdown to docx...")
    os.system(ProjectPath+'\\bin\\pandoc.exe -f gfm -t docx '+markdown_output+" -o "+word_output)
    print("Converted.")

md_gen(input("Plan name: "))
md_to_docx()
os.system('start '+word_output)
