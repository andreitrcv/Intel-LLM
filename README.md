# Intel-LLM: (Cyber-)Security Document Retrieval and Filtering

![Intel-LLM](https://github.com/user-attachments/assets/b324afa7-5d9a-4d6d-8938-b6015c6d1376)


**Intel-LLM** is a Python-based automation tool which goal is to identify and download relevant files from the Internet that cover topics such as cyber threat intelligence, Advanced Persistent Threats (APT), military and government-backed operations, cybersecurity research, cyber warfare, and related topics. It uses Google's search engine and a (Large) Language Model (LLM) to filter files and find the most pertinent results based on user-defined queries.

- The user can specify a target language or region to search for documents using government and military domains.
- The tool fetches search results from Google based on the query.
- The results are filtered by an LLM, which ranks files by relevance to cyber threat intelligence and other specified topics.
- The most relevant files are automatically downloaded for further analysis.

***
--- 

## Installation:

Environment Setup: Ensure you have Python 3.x installed. Install the required packages using pip:
-     pip install requests googlesearch-python google-generativeai



API Key Configuration: Set up the environment variable for the Google Generative AI (LLM) API key:


-     export API_KEY="your-google-api-key"
***
--- 

## Usage:

Run the Script: Start by running the main Python script:

-      python Intel-LLM.py

Select a Country Query: You will be prompted to choose from a list of languages and country-specific queries (e.g., English, German, Russian, Chinese...).

![image](https://github.com/user-attachments/assets/49b8b25c-d3ff-44db-8514-a968ea4baff1)

Choose how many documents you want to filter. All of them will be given to the LLM and filtered for downloading.
