# 🚀 AdOps Toolkit: Automated Link Validator

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Pytest](https://img.shields.io/badge/Test-Pytest-green.svg)
![Pandas](https://img.shields.io/badge/Data-Pandas-orange.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)

> **Automating the manual verification of advertising landing pages with QA-grade reliability.**
> 
> This is a personal project designed to solve a major pain point in Digital Advertising: the manual verification of massive amounts of Landing Page URLs. As an AdOps specialist transitioning into a QA Engineer role, I developed this tool to demonstrate my ability to bridge domain expertise with automated testing practices and modular software design.

## 📖 Background

In daily AdOps workflows, managing hundreds or thousands of ad links is standard. If a Landing Page fails (404 errors, DNS issues, or server crashes), it results in immediate waste of advertising budget.

I built this **Automated Link Validator** to replace manual checks. It reads URLs from Excel reports, performs batch validation of connection statuses, and generates a diagnostic report.

**Core Value:**
* **Efficiency**: Reduces hours of manual verification to a few minutes.
* **Quality Assurance**: Implements `pytest` and `requests-mock` to handle various edge cases, ensuring the tool's own reliability.

## ✨ Key Features

* **📊 Batch Processing**: Utilizes `pandas` to process large-scale URL lists from Excel files.
* **🛡️ Robust Error Handling**: Distinguishes between HTTP status codes (e.g., 200, 404) and low-level network exceptions (Connection Errors, Timeouts) to prevent script crashes.
* **🧪 Unit Test Coverage**: Features a comprehensive test suite using `pytest` and `requests-mock` to verify logic without making actual network requests.
* **📝 Automated Reporting**: Generates a `report.xlsx` output, clearly flagging invalid links (`is_valid: False`) and capturing specific error messages for troubleshooting.

## 🛠️ Tech Stack

* **Language**: Python
* **Data Processing**: Pandas, OpenPyxl
* **HTTP Requests**: Requests
* **Testing**: Pytest, Requests-Mock

## 📂 Project Structure
```text
AdOps-Toolkit/
├── data/
│   ├── urls.xlsx          # [Input] Source Excel file containing URLs
│   └── report.xlsx        # [Output] Validation results and error logs
├── modules/
│   ├── __init__.py
│   └── link_validator.py  # Core logic: Single URL validation module
├── tests/
│   └── test_link_validator.py # Unit tests for the validation module
├── main.py                # Main entry point of the application
├── requirements.txt       # Project dependencies
└── .gitignore             # Git ignore rules for venv and metadata
```

## 🎬 Demo

### Quick Look
![Demo GIF](https://github.com/user-attachments/assets/0a112eb5-c307-4d7f-b227-90172ee95bc3)

### Sample Results

| URL | Status | Error Message |
|-----|--------|---------------|
| `https://example.com` | ✅ Valid | - |
| `https://broken-link.com` | ❌ Invalid | 404 Not Found |

## 💻 Installation & Usage

### 1. Clone the repository
```bash
git clone https://github.com/alanliang666/adops-toolkit.git
cd adops-toolkit
```

### 2. Install dependencies

It is recommended to use a Virtual Environment:
```bash
# Create a virtual environment
python -m venv venv
source venv/bin/activate  # macOS/Linux
# venv\Scripts\activate   # Windows

# Install required packages
pip install -r requirements.txt
```

### 3. Prepare Data

Add your target URLs into the `url` column of the `data/urls.xlsx` file.

### 4. Run the script

Execute the main program:
```bash
python main.py
```

Upon completion, check `data/report.xlsx` for the detailed results.

## 🧪 Testing Strategy

This project employs **Pytest** for unit testing and **Requests-Mock** to isolate external network dependencies. This approach ensures high test reliability and execution speed.

**Scenarios Covered:**

- **Success Case**: Simulates a 200 OK response to verify correct validation logic.
- **Client Error**: Simulates a 404 Not Found to ensure the tool correctly flags dead links.
- **Network Exception**: Simulates connection failures to verify that the error handling mechanism captures the exception without crashing the program.

**Run Tests:**
```bash
pytest tests/
```
