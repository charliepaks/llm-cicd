
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.text_splitter import CharacterTextSplitter
import openai
import os
import sys

# Retrieve thee OpenAI api key from environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    print("Error: OPENAI_API_KEY environment variable not set.")
    sys.exit(1)

openai.api_key = OPENAI_API_KEY

def split_code_with_langchain(content, chunk_size=3000, chunk_overlap=200):
    """
    Splits the code into chunks using LangChain's CharacterTextSplitter.
    """
    splitter = CharacterTextSplitter(
        separator="\n",  # Split by newlines
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
    )
    return splitter.split_text(content)

def analyze_code_chunk(chunk, chat_model):
    """
    Analyzes a single chunk of code using the LLM.
    """
    prompt_template = ChatPromptTemplate.from_template(
        """
        You are a security expert. Analyze the following code chunk for vulnerabilities:
        {code}

        Provide:
        - Vulnerability description
        - Potential severity (low, medium, high)
        - Suggestions for fixing the issue
        """
    )
    prompt = prompt_template.format(code=chunk)
    response = chat_model.call(prompt)
    return response

def analyze_large_file(file_content):
    """
    Handles large files by splitting them into chunks and analyzing each chunk.
    """
    chat = ChatOpenAI(temperature=0, openai_api_key=OPENAI_API_KEY)
    chunks = split_code_with_langchain(file_content)
    results = []
    for i, chunk in enumerate(chunks):
        print(f"Analyzing chunk {i + 1}/{len(chunks)}...")
        result = analyze_code_chunk(chunk, chat)
        results.append({"chunk": i + 1, "analysis": result})

    return results

def process_file(file_path):
    """
    Reads and analyzes a single file.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            code_content = file.read()
            print(f"Analyzing {file_path}...")
            analysis = analyze_large_file(code_content)
            return {"file": file_path, "analysis": analysis}
    except Exception as e:
        print(f"Error processing file {file_path}: {e}")
        return {"file": file_path, "error": str(e)}
    
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python analyze_code.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]

    if os.path.isfile(file_path):
        result = process_file(file_path)
        print("\n--- Vulnerability Analysis Report ---\n")
        print(f"File: {result['file']}\n")
        for chunk_result in result.get("analysis", []):
            print(f"Chunk {chunk_result['chunk']}:\n")
            print(chunk_result.get("analysis", chunk_result.get("error")))
            print("\n" + "-" * 80 + "\n")
    else:
        print("Invalid path. Please provide a valid file.")