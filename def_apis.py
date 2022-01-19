import ia_google
import ia_duckduckgo
import img_duckduckgo
import wikipedia_api

def set_lang(code):
    ia_google.set_lang(code)
    ia_duckduckgo.set_lang(code)
    img_duckduckgo.set_lang(code)
    wikipedia_api.set_lang(code)

def search_google(topic):
    ia_google.save_source(topic)
    ia_google.clean_source()
    try:
        ia_google.extract_result()
        ia_google.clean_result()
        ia_google.clean_source_files()
    except FileNotFoundError:
        print("Aborted.")

def search_duckduckgo(topic):
    ia_duckduckgo.save_source(topic)
    ia_duckduckgo.extract_result()
    ia_duckduckgo.clean_result()
    ia_duckduckgo.clean_source_files()

def search_duckduckgo_img(topic, images):
    img_duckduckgo.search(topic, images)

def search_wikipedia(topic, paragraphs):
    wikipedia_api.save_content(topic)
    wikipedia_api.process_content(paragraphs)
    wikipedia_api.clean_source_files()
