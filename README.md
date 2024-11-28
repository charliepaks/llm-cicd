🛡️ **CI/CD with LLM for Static Application Security Testing (SAST)**

Welcome to the LLM Powered SAST project! This repository integrates an LLM-powered Python script into a GitHub Actions CI/CD pipeline to automatically analyze code files for security vulnerabilities during pull requests and pushes.

🚀 **Features**

- Automated Code Scanning: Scans all code files in the repository for vulnerabilities using OpenAI's GPT-4.

- OWASP Standards: Generates vulnerability reports following the OWASP Code Review Guide.

- Severity-Based Workflow: Fails pull requests if high-severity vulnerabilities are found.

- Multi-Language Support: Supports scanning for various code file types (.py, .js, .java, etc.).

- Actionable Feedback: Provides detailed vulnerability descriptions, confidence levels, severity ratings, and remediation suggestions.

**📂 Directory Structure**

llm-cicd/
│
├── .github/
│   └── workflows/
│       └── sast.yml        
├── analyze_code.py         
├── requirements.txt        
├── vulnerable-code-files/                
└── README.md               
