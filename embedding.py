# pip install faiss-cpu for cpu user
from langchain_community.embeddings import GPT4AllEmbeddings
from langchain_community.vectorstores import FAISS
from load_file import process_file

gpt4all_embd = GPT4AllEmbeddings()

def get_docsearch(document):

    # Save data in the user session
    user_session = document

    # Create a unique namespace for the file

    docsearch = FAISS.from_documents(
        document, gpt4all_embd
    )
    return docsearch

# get_docsearch(result)
# <langchain_community.vectorstores.faiss.FAISS at 0x7cf594105a20>