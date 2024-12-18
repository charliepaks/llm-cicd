
# Author: Charles Chibueze
# Email: charlesukpaka@ymail.com
# GitHub: https://github.com/charliepaks
# LinkedIn: https://www.linkedin.com/in/charles-chibueze-cissp-cism-ceh-pnpt-2358a2112/

from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.text_splitter import CharacterTextSplitter
import openai
import os
import sys
import re

# Uncommentee this part below if you want to test the project locally
#from dotenv import load_dotenv, find_dotenv
#_ = load_dotenv(find_dotenv())
#openai_api_key = os.environ["OPENAI_API_KEY"]

# Comment the one liner below if you want to test the project locally
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    print("Error: OPENAI_API_KEY environment variable not set.")
    sys.exit(1)

openai.api_key = OPENAI_API_KEY
 

def split_code_with_langchain(content, chunk_size=3000, chunk_overlap=200):
    
    splitter = CharacterTextSplitter(
        separator="\n",  # Split by newlines
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
    )
    return splitter.split_text(content)

def analyze_code_chunk(chunk, chat_model):
    
    
    prompt_template = ChatPromptTemplate.from_template(
        """
        You are an application security and cloud security expert. if the chunk presented to you has code in it, analyze the following code chunk thoroughly for vulnerabilities according to the owasp code review guide. Do not just look for critical 
        issues. Identify issues of medium and low severity too. When you find the issues, enumerate them all and report them per the owasp code review guide standard. Start with the first finding and let the last finding
        be the end of the report. Do not write anything after the last vulnerability has been documented. Write the report in plain text and not markdown.

        If the chunk presented to you is a terraform file, analyze the following Terraform file and identify potential security issues. Review it according
        to best practices and guidelines such as the CIS Benchmarks, OWASP IaC Security principles, and cloud provider-specific security recommendations (e.g., AWS, Azure, GCP).
        
    :
        {chunk}

        If it's a code file, provide:
        - A summary of each identified issue.
        - Detailed explanation of each issue.
        - Confidence (low, medium, high)
        - Potential severity (low, medium, high)
        - Suggestions for fixing the issue
        
        If it's a terraform file, provide:
        - A summary of identified issues.
        - Detailed explanation of each issue.
        - Confidence levels (low, medium, high).
        - Severity levels (low, medium, high).
        - Suggestions for fixing each issue.
        """
    )
    prompt = prompt_template.format(chunk=chunk)
    response = chat_model.invoke(prompt)
    return response.content

def analyze_large_file(file_content):
    
    chat = ChatOpenAI(temperature=0, model="gpt-4o", openai_api_key=OPENAI_API_KEY)
    chunks = split_code_with_langchain(file_content)
    results = []
    for i, chunk in enumerate(chunks):
        print(f"Analyzing chunk {i + 1}/{len(chunks)}...")
        result = analyze_code_chunk(chunk, chat)
        results.append({"chunk": i + 1, "analysis": result})

    return results

def process_file(file_path):
    
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            code_content = file.read()
            print(f"Analyzing {file_path}...")
            analysis = analyze_large_file(code_content)
            return {"file": file_path, "analysis": analysis}
    except Exception as e:
        print(f"Error processing file {file_path}: {e}")
        return {"file": file_path, "error": str(e)}
    
def scan_directory(directory="."):
    
    supported_extensions = {".py", ".js", ".java", ".cpp", ".c", ".rb", ".go", ".tf"}  
    results = []
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            _, extension = os.path.splitext(file)
            if extension in supported_extensions:
                result = process_file(file_path)
                results.append(result)
    return results

def process_results(results):
    
    high_severity_found = False

    for result in results:
        for finding in result.get("analysis", []):
            if re.search(r"(potential severity: high|severity: high)", finding.get("analysis", ""), re.IGNORECASE):
                high_severity_found = True
                

    if high_severity_found:
        print("Failing due to at least 1 high-severity vulnerability.")
        sys.exit(1)  

    print("Success! No high-severity vulnerabilities found.")
    sys.exit(0)  
    
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python analyze_code.py <path>")
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

    elif os.path.isdir(file_path):
        results = scan_directory(file_path)
        for result in results:
            print("\n--- Vulnerability Analysis Report ---\n")
            print(f"File: {result['file']}\n")
            for chunk_result in result.get("analysis", []):
                print(f"Chunk {chunk_result['chunk']}:\n")
                print(chunk_result.get("analysis", chunk_result.get("error")))
                print("\n" + "-" * 80 + "\n")
    else:
        print("Invalid path. Please provide a valid file or directory.")
    process_results(results)
    