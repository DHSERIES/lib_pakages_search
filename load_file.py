import os

#pip install pypdf
#export HNSWLIB_NO_NATIVE = 1

from langchain.document_loaders import PyPDFLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os

# import multiprocessing

# def multi_process(func):
#     def wrapper(*args, **kwargs):
#         num_cores = os.cpu_count()
#         if num_cores > 1:
#             pool = multiprocessing.Pool(num_cores)
#             try:
#                 result = pool.map(func, *args, **kwargs)
#             except Exception as e:
#                 print(f"An error occurred: {e}")
#                 result = None
#             finally:
#                 pool.close()
#                 pool.join()
#             return result
#         else:
#             return func(*args, **kwargs)
#     return wrapper

# @multi_process
def process_file(file_path):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)

    try:
        file_path = os.path.abspath(file_path)
        file_extension = os.path.splitext(file_path)[1].lower()
        if file_extension == ".txt":
            Loader = TextLoader
        elif file_extension == ".pdf":
            Loader = PyPDFLoader
        else:
            print(f"Unsupported file format: {file_extension}")
            return None
        loader = Loader(file_path)
        documents = loader.load()
        docs = text_splitter.split_documents(documents)
        for i, doc in enumerate(docs):
            doc.metadata["source"] = f"source_{i}"
        return docs
    except Exception as e:
        print(f"Error processing file {file_path}: {e}")
        # You can choose to log the error, skip the file, or take other action
        # For example, you can return None or raise an exception
        return None


def test_load_file(file_name):
    try:
        file_paths = file_name  # List of file paths to process
        result = load_file(file_paths)
        print(result)
    except Exception as e:
        raise f"Error processing file {file_path}: {e}"