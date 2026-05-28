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

## 3.Text Splitters

