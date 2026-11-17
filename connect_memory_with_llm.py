
import os

# Disable TensorFlow (use PyTorch)
os.environ["USE_TF"] = "0"

from langchain_core.prompts import PromptTemplate
from langchain_classic.chains import RetrievalQA
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaLLM


# Step 1: Setup local Ollama LLM
def load_llm():
    llm = OllamaLLM(
        model="mistral",
        temperature=0.5
    )
    return llm


# Step 2: Custom prompt
CUSTOM_PROMPT_TEMPLATE = """
Use the pieces of information provided in the context to answer user's question.
If you don't know the answer, just say that you don't know.
Don't make up an answer.
Don't provide anything outside the given context.

Context: {context}
Question: {question}

Start the answer directly. No small talk please.
"""


def set_custom_prompt(custom_prompt_template):
    prompt = PromptTemplate(
        template=custom_prompt_template,
        input_variables=["context", "question"]
    )
    return prompt


# Step 3: Load FAISS database
DB_FAISS_PATH = "vectorstore/db_faiss"

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

db = FAISS.load_local(
    DB_FAISS_PATH,
    embedding_model,
    allow_dangerous_deserialization=True
)


# Step 4: Create QA chain
qa_chain = RetrievalQA.from_chain_type(
    llm=load_llm(),
    chain_type="stuff",
    retriever=db.as_retriever(search_kwargs={"k": 3}),
    return_source_documents=True,
    chain_type_kwargs={
        "prompt": set_custom_prompt(CUSTOM_PROMPT_TEMPLATE)
    }
)


# Step 5: Function to get response
def get_response(user_query):
    response = qa_chain.invoke({"query": user_query})
    return response["result"]

