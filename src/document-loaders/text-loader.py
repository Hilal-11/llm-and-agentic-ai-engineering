# from pathlib import Path
# from langchain_community.document_loaders import TextLoader

# file_path = Path(__file__).parent / "ai-knowledge-base.txt"
# print(file_path, file_path.exists())   # should print True

# docs = TextLoader(str(file_path), encoding="utf-8").load()
# print(docs[0].page_content)
# print(docs[0].metadata)

from pathlib import Path
from langchain_community.document_loaders import DirectoryLoader, TextLoader

ROOT = Path(__file__).resolve().parents[2] # C:\Users\HP\OneDrive\Desktop\Agentic-AI\langchain-fundamentals
file_path = ROOT / "data" / "ai-knowledge-base.txt" # C:\Users\HP\OneDrive\Desktop\Agentic-AI\langchain-fundamentals\data\ai-knowledge-base.txt

loader = TextLoader(str(file_path), encoding="utf-8")

docs = loader.load()
print(docs[0].page_content)
print(docs[0].metadata)
print(len(docs))