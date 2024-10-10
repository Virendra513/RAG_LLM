import streamlit as st
from model import result_text

st.markdown(
    """
    <style>
    body {
        background-color: #F0F2F5;  /* Background color */
    }

    .big-font {
        font-size: 20px !important;
        color: gray;
         text-align: center;  /* Change to your desired color */
    }
    .custom-title {
        font-size: 40px !important;
        color: black;
        text-align: center;
        font-weight: bold;
        text-decoration: underline;  /* Change to your desired color */
    }
    </style>
    """,
    unsafe_allow_html=True
)


# Title in the sidebar
st.sidebar.title(" Synergizing RAG and LLMs for Enhanced Text Generation- Quantum Drug Discovery")

# Paragraph in the sidebar
st.sidebar.write("""RAG (Retrieval-Augmented Generation) represents an innovative approach that merges the capabilities of retrieval systems with generative models. By drawing on external knowledge sources, this architecture significantly enhances the ability to produce accurate and contextually relevant outputs.
""")

st.sidebar.write(""" Trainning of this process start with by loading PDF documents from the local database which contains papers related to Quantum Drug Discovery. It then splits the loaded documents into manageable text chunks, creating embeddings from these chunks using the "BAAI/bge-base-en-v1.5 model". These embeddings are stored in a "FAISS" database, which enables efficient similarity searches for relevant documents. After setting up a retriever for fetching the most pertinent documents based on user queries, the code prepares to generate responses using the "BLOOM" model, known for its multilingual capabilities and high performance.""")


st.markdown('<p class="custom-title">Synergizing RAG and LLMs for Enhanced Text Generation- Quantum Drug Discovery</p>',unsafe_allow_html=True)
st.write("")


# User input
text_to_translate = st.text_area("Enter/Paste text in English:")

# Button to trigger translation
if st.button("Generate"):
    if text_to_translate:
        # Call the translation function
        output =  result_text(text_to_translate)
        st.write("Result of query is :", output["result"])
    else:
        st.error("Please enter/paste valid query.")

st.write("")  # Adds an empty line
st.write("")  # Adds an empty line
st.write("")  # Adds an empty line
st.write("")  # Adds an empty line
st.write("")  # Adds an empty line
st.write("")  # Adds an empty line
st.write("")  # Adds an empty line
st.write("")  # Adds an empty line
st.write("")  # Adds an empty line
st.write("") 
st.write("") 
st.write("") 
st.write("") 
st.write("") 
st.write("") 
st.write("") 
st.write("") 
st.write("") 
st.write("") 
st.write("") 
st.write("")  

st.markdown('<p class="big-font">Designed and Developed by Virendra S K    @2024</p>', unsafe_allow_html=True)