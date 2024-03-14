
from llama_index import VectorStoreIndex,download_loader, VectorStoreIndex, ServiceContext, StorageContext, load_index_from_storage
from pathlib import Path
import os
import shutil
import openai
import gradio as gr

from pathlib import Path
from llama_index import download_loader

"""# Github Configeration"""

openai.api_key = "key"

# username = 'Akhil-Sharma30'


"""# Reading the Files for LLM Model"""


# Specify the path to the repository
repo_dir = "/content/Akhil-Sharma30.github.io"

# Check if the repository exists and delete it if it does
if os.path.exists(repo_dir):
    shutil.rmtree(repo_dir)


# def combine_md_files(folder_path):
#     MarkdownReader = download_loader("MarkdownReader")
#     loader = MarkdownReader()

#     md_files = [file for file in folder_path.glob('*.md')]
#     documents = None

#     for file_path in md_files:
#         document = loader.load_data(file=file_path)
#         documents += document

#     return documents

# folder_path = Path('/content/Akhil-Sharma30.github.io/content')
#combined_documents = combine_md_files(folder_path)

# combined_documents will be a list containing the contents of all .md files in the folder

RemoteReader = download_loader("RemoteReader")

loader = RemoteReader()

document1 = loader.load_data(url="https://raw.githubusercontent.com/Akhil-Sharma30/Akhil-Sharma30.github.io/main/assets/README.md")
document2 = loader.load_data(url="https://raw.githubusercontent.com/Akhil-Sharma30/Akhil-Sharma30.github.io/main/content/about.md")
document3 = loader.load_data(url="https://raw.githubusercontent.com/Akhil-Sharma30/Akhil-Sharma30.github.io/main/content/cv.md")
document4 = loader.load_data(url="https://raw.githubusercontent.com/Akhil-Sharma30/Akhil-Sharma30.github.io/main/content/post.md")
document5 = loader.load_data(url="https://raw.githubusercontent.com/Akhil-Sharma30/Akhil-Sharma30.github.io/main/content/opensource.md")
document6 = loader.load_data(url="https://raw.githubusercontent.com/Akhil-Sharma30/Akhil-Sharma30.github.io/main/content/supervised.md")

data = document1+ document2 + document3+ document4 + document5+document6


"""# Vector Embedding"""

index = VectorStoreIndex.from_documents(data)
system=''''''
query_engine = index.as_query_engine()
response = query_engine.query(system+"user prompt")
print(response)
print("####################################")
response = query_engine.query("what is name of the person?")
print(response)
