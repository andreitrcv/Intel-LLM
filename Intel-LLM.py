# 1. ask for a website
# 2. compose string
# 3. search for the string on Google
# 4. fetch files
# 5. ask LLM to filter them to get the best ones
# prompt ChatGPT

import requests
from googlesearch import search

template = "site:*.{0} (ext:doc OR ext:docx OR ext:pdf OR ext:rtf OR ext:ppt OR ext:pptx OR ext:csv OR ext:xls OR ext:xlsx OR ext:txt OR ext:xml OR ext:json OR ext:zip OR ext:rar OR ext:log OR ext:bak OR ext:conf OR ext:sql)"

def get_target():
    target = input("Enter target: ")
    return target

def compose_query(target):
    final_query = template.format(target)
    return final_query

def google_search(query):
    search_results = search(query, num_results=10)
    return search_results

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

def download_files(files):
    for _, file in enumerate(files, start=1):
        download_file(file)

def main():
    target = get_target()
    final_query = compose_query(target)
    results = google_search(final_query)
    download_files(results)

if __name__ == "__main__":
    main()


