from langchain.document_loaders import DirectoryLoader,PyPDFLoader
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEndpoint
from langchain.vectorstores import FAISS
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA

loader = DirectoryLoader('Drug_Discovery_Quntum/', glob="./*.pdf", loader_cls=PyPDFLoader)

docs = loader.load()


text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
texts = text_splitter.split_documents(docs)

db = FAISS.from_documents(texts, HuggingFaceEmbeddings(model_name='BAAI/bge-base-en-v1.5'))

#query = "Tell me about  current research gap?"
#relevant_documents = db.similarity_search(query)
#print(relevant_documents[0].page_content)


retriever = db.as_retriever(search_type="similarity", search_kwargs={"k": 1})

#retriever.get_relevant_documents(query)


load_dotenv()

#repo_id="mistralai/Mistral-7B-v0.1" max_length=128
repo_id="bigscience/bloom"
llm=HuggingFaceEndpoint(repo_id=repo_id,temperature=0.7)

# llm.invoke("What is deep learning learning")


prompt_template = """Based on the provided context, respond to the question below while adhering to these guidelines:
1. If the answer is unclear or not found, do not speculate. Instead, state, "I do not know the answer"
2. If the answer is found, provide a clear and concise response in no more than ten sentences.

{context}

Question: {question}

Answer:
"""


PROMPT = PromptTemplate(
 template=prompt_template, input_variables=["context", "question"]
)



retrievalQA = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever,
    return_source_documents=True,
    chain_type_kwargs={"prompt": PROMPT}
)


# Call the QA chain
"""result = retrievalQA.invoke({"query": query})
print(result['result'])


# Call the QA chain
query = "what is Supervised Learning?"
result = retrievalQA.invoke({"query": query})
print(result['result'])

retriever.get_relevant_documents(query)
"""



def result_text(query):
    """Function to translate text from English to Hindi."""
    return retrievalQA.invoke({"query": query})