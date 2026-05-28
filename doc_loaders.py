from dotenv import load_dotenv
import os
from langchain_community.document_loaders import TextLoader,WebBaseLoader


load_dotenv()

def load_text_file(file_path:str)->str:
    try:
      loader = TextLoader(file_path)
      documents = loader.load()
      return documents
    except Exception as e:
      print(f"Error loading text file: {e}")

def webBaseLoader(url:str):
   try:
     loader = WebBaseLoader(url)
     documents = loader.load()
     return documents
   except Exception as e:
     print(f"Error loading web page: {e}")

    
if __name__ == "__main__":
    file_path = "movie.txt"  
    documents = load_text_file(file_path)
    documents = documents[0].page_content
    print(documents)

    url = "something"
    li = webBaseLoader(url)
    li = li[0].page_content
    print(li)