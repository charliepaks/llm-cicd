## Author

- **Charles Chibueze**  
  - [GitHub Profile](https://github.com/charliepaks)  
  - [LinkedIn](https://linkedin.com/charles-chibueze-cissp-cism-ceh-pnpt-2358a2112/)  
  - [Email](charlesukpaka@ymail.com)

## 🛡️ **CI/CD with LLM for Static Application Security Testing (SAST)**

Welcome to the LLM Powered SAST project! This repository integrates an LLM-powered Python script into a GitHub Actions CI/CD pipeline to automatically analyze code files for security vulnerabilities during pull requests and pushes.

## 🚀 **Features**

- **Automated Code Scanning**: Scans all code files in the repository for vulnerabilities using OpenAI's GPT-4.

- **OWASP Standards**: Generates vulnerability reports following the OWASP Code Review Guide.

- **Severity-Based Workflow**: Fails pull requests if high-severity vulnerabilities are found (at least one).

- **Multi-Language Support**: Supports scanning for various code file types (.py, .js, .java, etc.).

- **Actionable Feedback**: Provides detailed vulnerability descriptions, confidence levels, severity ratings, and remediation suggestions.

## **⚙️ Setup and Installation**

**Prerequisites**

- **Python**: Ensure you have Python 3.10 or later installed.
- **Git**: Install Git to clone and manage your repository.
- **OpenAI API Key**: Obtain your API key from OpenAI.

**Installation**

**Clone this repository**:

_git clone https://github.com/charliepaks/llm-cicd.git

cd llm-cicd_

Create a Python virtual environment and activate it:

_python -m venv venv

source venv/bin/activate  

If you want to test this on your github actions workflow, you can push the local files you have cloned and it will trigger the workflow. 

**Install dependencies**:

_pip install -r requirements.txt_

**Add your OpenAI API key as an environment variable**:

- Navigate to your repository on GitHub.
- Click on the "Settings" tab at the top of the repository page.
- Scroll down the left sidebar in the Settings menu.
- Under the "Security" section, click on "Secrets and variables".
- Select "Actions" under Secrets and Variables.
- Click on the "New repository secret" button.
- Provide a name for the secret (e.g., OPENAI_API_KEY).
- Enter the value of the secret (e.g., your OpenAI API key).
- Click "Add secret" to save it.
If you want to test the project locally:
- Add the secret to a .env file this way:  OPENAI_API_KEY = your-api-key-here
- Check the analyze_code.py file and uncomment the portion that will let you test the project locally. There is also a one liner to put in comments to make this work.

## **🔄 Workflow Overview**

The CI/CD pipeline is triggered during:

- Pull Requests to the main branch.
- Pushes to the main branch.

**Key Workflow Steps**:

1. Dependency Installation:
Installs all required Python packages.

2. Code Analysis:
Executes the analyze_code.py script to scan all files in the repository.

3. Pull Request Failing:
The workflow fails if any high-severity vulnerabilities are detected.


## **🛠️ Usage**

**Local Testing**:

Run the analyze_code.py script locally for testing:

_python analyze_code.py <file_or_directory_path>_

## **GitHub Actions**:

Simply commit and push your changes to trigger the workflow:

_git add .
git commit -m "Commit message"
git push origin main_

## **📖 Configuration**

**Workflow File**: .github/workflows/sast.yml

Modify the workflow file to match your project's requirements. Key sections include:

- **Python Version**: Specify the required Python version.

- **OpenAI API Key**: Ensure the key is stored securely as a GitHub Secret (OPENAI_API_KEY).

## **🌟 Contributing**

Contributions are very much welcome! Feel free to submit issues or pull requests for bug fixes, enhancements, or new features.

## **🛡️ Security**

- Ensure your OpenAI API Key is kept confidential.

- Also ensure you regularly update dependencies to avoid security vulnerabilities in libraries.

## **📝 License**

This project is licensed under the MIT License. See the LICENSE file for details.




