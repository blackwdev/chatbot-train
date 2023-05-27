from llama_index import GPTVectorStoreIndex , SimpleDirectoryReader, StorageContext, load_index_from_storage
import os

os.environ["OPENAI_API_KEY"] = ''

documents = SimpleDirectoryReader('data').load_data()
index = GPTVectorStoreIndex.from_documents(documents)

# # rebuild storage context
# storage_context = StorageContext.from_defaults(persist_dir='./storage')
# # load index
# index = load_index_from_storage(storage_context)

# index.storage_context.persist()
query_engine = index.as_query_engine()
response = query_engine.query("What did the author do growing up?")
print(response)