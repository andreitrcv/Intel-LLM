# 1. ask for a website
# 2. compose string
# 3. search for the string on Google
# 4. fetch files
# 5. ask LLM to filter them to get the best ones
# prompt ChatGPT

import google.generativeai as genai
from googlesearch import search
import os
import requests
import time

genai.configure(api_key=os.environ["API_KEY"])
model = genai.GenerativeModel("gemini-1.5-flash")

def get_country_target():
    target = input("\
1.  English documents\n\
2.  Italian documents\n\
3.  French documents\n\
4.  Russian documents\n\
5.  Chinese documents\n\
6.  German documents\n\
7.  Arabic documents\n\
8.  Hebrew (Israel) documents\n\
9.  Polish documents\n\
10. Romanian documents\n\
11. Hungarian documents\n\
Choose [1-11]: ")

    with open("queries.txt") as file:
        lines = [line.rstrip() for line in file]
    return lines[int(target)-1]

def get_number_of_docs():
    number = input("How many documents you want to search for? (They will be filtered and only the most suitable ones will be downloaded): ")
    return int(number)

def get_user_inputs():
    target = get_country_target()
    number = get_number_of_docs()
    return target, number

def google_search(query, number_of_docs):
    search_results = list(search(query, num_results=number_of_docs, safe=None))
    return search_results

def get_system_prompt():
    with open("system-prompt.txt", 'r') as content_file:
        sys_prompt = content_file.read()
    return sys_prompt

def filter_files(files):
    system_prompt = get_system_prompt()
    final_prompt = system_prompt + "\n" + " ".join(str(file) for file in files)
    response = model.generate_content(final_prompt)
    indexes = [int(x.strip()) for x in response.text.split(',') if x.strip().isdigit()]
    return indexes


def download_file(url):
    local_filename = url.split('/')[-1]
    # NOTE the stream=True parameter below
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                #if chunk: 
                f.write(chunk)
    return local_filename

def download_files(files, indexes):
    print("\n")
    for index, file in enumerate(files, start=1):
        if index in indexes:
            print(f'Downloading {file}')
            download_file(file)

def main():
    country_query, number_of_docs = get_user_inputs()
    results = google_search(country_query, number_of_docs)
    indexes = filter_files(results)
    download_files(results, indexes)

if __name__ == "__main__":
    main()

