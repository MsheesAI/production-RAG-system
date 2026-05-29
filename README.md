# RAG Pipeline

## 1. Document Loaders

In a RAG (Retrieval-Augmented Generation) system, Document Loaders are the first step of the pipeline. They are responsible for bringing your raw data into a format that your AI system can understand and search.A Document Loader takes data from different sources and converts it into a standard
format like this

```
Document(
    page_content="your text here",
    metadata={"source": "file_name.txt"}
)
```

#### 📁 Common Document Loaders (LangChain)
1. Text File Loader
2. Pypdf loader
3. WebBaseLoader
4. CSV loader
5. directory loader

<img width="1155" height="447" alt="image" src="https://github.com/user-attachments/assets/e9834f7c-5bc4-4ec3-8797-67bfca80746e" />


## 2.Text Splitters

Text Splitters are the most important step after loaders in RAG because they decide how well your AI will understand context.
A Text Splitter breaks large documents into smaller chunks so that:
🧠 LLM can process them
🔍 embeddings work better
⚡ retrieval becomes accurate

If you don’t split:

❌ bad retrieval
❌ irrelevant answers
❌ token limit issues

If you split correctly:

✔ better search results
✔ higher accuracy
✔ faster processing

#### 📦 Types of Text Splitters (LangChain)
1. CharacterTextSplitter
2. RecursiveCharacterTextSplitter
3. Token-based Splitter

<img width="685" height="340" alt="image" src="https://github.com/user-attachments/assets/7096fdb1-a971-45a0-8a18-4ce093a3e81a" />

## 3.Embeddings

Embeddings = converting text into numbers (vectors) so a computer can understand meaning.
Instead of storing text like:
"Python is used in AI"
We convert it into something like:
```
[0.12, -0.98, 0.33, ..., 0.71]
```
we use embeddings because computers cannot compare meanings using words we used embeddings for :
✔ semantic search (meaning-based search)
✔ not keyword search
✔ better answers in RAG

🔥 Simple Idea

Think of embeddings like this:

Text	Meaning
"car"	vector A
"vehicle"	vector close to A
"banana"	far away vector

👉 similar meaning = close vectors
👉 different meaning = far vectors

<img width="800" height="401" alt="image" src="https://github.com/user-attachments/assets/d58903e3-cca0-4265-b1b8-51cbec15eb88" />

## 4. Vector Stores / Data base
A vector database is a special type of database that stores:

👉 embeddings (vectors)
👉 and allows fast similarity search
Instead of searching by keywords, it searches by meaning.
📦 Simple definition

A vector DB stores:

``` "text" → [0.12, -0.88, 0.33, ...] ```
Then when you ask a question, it finds:
👉 “which stored vector is closest in meaning?”

🔥 Why normal database is NOT enough
Traditional DB (SQL):
searches exact words
like: "Python"
Vector DB:
understands meaning
like: "programming language for AI"

Most popular Vecot DB are :
FAISS
Chroma
pinecone

<img width="1399" height="537" alt="image" src="https://github.com/user-attachments/assets/532c89ce-cbb7-4573-bbe6-b0c7169a5639" />

## 5.Complete pipeline overview

#### ⚙️ FULL PIPELINE FLOW
```
1. Data Sources
   ↓
2. Document Loader
   ↓
3. Text Splitter
   ↓
4. Embeddings Model
   ↓
5. Vector Database (FAISS / Chroma)
   ↓
6. User Query
   ↓
7. Query Embedding
   ↓
8. Similarity Search (Retrieval)
   ↓
9. Retrieved Context
   ↓
10. LLM (Final Answer)
```


<img width="1024" height="614" alt="image" src="https://github.com/user-attachments/assets/31e92a7e-b07e-4194-a317-a6b2fc5f7203" />


