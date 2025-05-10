# Snaptrude Automation Testing assignment

This project automates the testing of Snaptrude's web application using the Playwright framework. It includes test cases for various features and supports multiple browsers.

## 📁 Project Structure

```
.
├── conftest.py       # Global test setup and fixtures
├── page              # Page Object Models for different pages
│   ├── __init__.py
│   ├── dashboard_page.py
│   ├── login_page.py
│   └── workspace_page.py
├── README.md         # Project documentation
├── test              # Test scripts for various functionalities
│   ├── test_fr_01.py
│   ├── test_fr_02.py
│   ├── test_fr_03.py
│   └── test_fr_05.py
├── traces            # Trace files generated for each test case
│   ├── test_FR01.zip
│   ├── test_FR02.zip
│   ├── test_FR03.zip
│   └── test_FR05.zip
└── utils             # Utility modules for logging and settings
    ├── __init__.py
    ├── logger.py
    ├── setting.py
    └── text_extracting.py
```

## 🚀 Getting Started

### Prerequisites

* Python 3.10+
* Playwright (`pip install playwright`)
* Pytest (`pip install pytest`)

### Setup

1. Clone the repository:

```bash
git clone <repository_url>
cd Snaptrude
```

2. Create a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate  # On macOS/Linux
.venv\Scripts\activate.bat  # On Windows
```

3. Install required packages:

```bash
pip install -r requirements.txt
playwright install
```

4. .env file expect below parameters
```bash
USERNAME=<username>
PASSWORD=<password>
```


### Directory Structure

* **conftest.py** - Central configuration and fixtures for the test framework.
* **page/** - Contains Page Object Models for different pages of the application.
* **test/** - Contains individual test scripts for various features.
* **traces/** - Stores trace files for each test case (automatically generated).
* **utils/** - Utility functions for logging, settings, and text extraction.

## 🧪 Running Tests

Run all tests:

```bash
pytest test/ -s -v
```

Run a specific test:

```bash
pytest test/test_fr_01.py -s -v
```

Run tests with a specific browser:

```bash
pytest test/ -s -v --test-browser=firefox
```

## 📊 Viewing Trace Files

To view a trace file, use the Playwright CLI:

```bash
playwright show-trace traces/test_FR01.zip
```



