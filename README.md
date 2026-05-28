#Rag Pipeline

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

