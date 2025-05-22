# Playwright_Python
# E-commerce Order Verification Test

This automation framework provides an end-to-end test suite to verify successful order placement and validation across API and UI layers on an e-commerce platform.

## 🧪 Test Case Overview

The test follows a hybrid approach with both API and UI validations:

1. **API Interaction:**
   - Authenticates and retrieves a token.
   - Creates a new order using the token via API.

2. **UI Verification:**
   - Logs into the web application.
   - Navigates to the Order History page.
   - Verifies the presence of the API-created order in the UI.

## 🚀 Framework Features

Built using **Python** and **Playwright**, the framework incorporates industry-standard practices for reliability and scalability:

- **✅ Page Object Model (POM):** Promotes reusability and maintainability by separating page interactions.
- **🔗 API Testing Utilities:** Utility functions to handle authentication, order creation, and response validations.
- **🧪 Pytest Integration:** Leverages Pytest for test discovery, fixtures, and reporting.
- **🌐 Multi-Browser Support:** Run tests on Chromium, Firefox, or WebKit via `--browser_name` CLI argument.
- **👥 Parametrized Testing:** Uses `data/credentials.json` to run tests across multiple user credentials.
- **📊 HTML Report Generation:** Automatically creates a detailed report (with logs and screenshots) in the `report/` folder.
- **📸 Screenshot on Failure:** Automatically captures UI screenshots for failed test cases and includes them in the HTML report.
- **🤖 Continuous Integration:**
  - **GitHub Actions:** Executes the test suite on every push and pull request.
  - **Jenkins:** Optional support for executing tests via Jenkins pipeline or freestyle jobs.
- **⚙️ Parallel Test Execution:** Supports parallel execution using `pytest-xdist` to speed up test runs.

## 🧰 Prerequisites

- Python 3.7 or above
- Playwright (`pip install playwright && playwright install`)
- Required dependencies listed in `requirements.txt`

## 📁 Project Structure

```
Playwright_Python/
├── .github/          # GitHub workflows for CI/CD
├── data/             # Test data files
├── locators/         # UI element locators
├── page_objects/     # Page Object Model classes
├── report/           # Test execution reports and screenshots
├── test/             # Test case scripts
├── utils/            # Utility modules and helper functions
├── .gitignore        # Specifies files/folders to ignore in Git
├── conftest.py       # Shared fixtures and Pytest configurations
├── pytest.ini        # Pytest settings and markers
├── README.md         # Project documentation
└── requirements.txt  # Project dependencies
```

## ▶️ Run Tests

**Run all tests with default browser:**

```
pytest -rA
```
Run with specific browser:
```
pytest --browser_name=firefox
```
Run smoke marked tests:
```
pytest -m smoke
```
### 🔄 Parallel Execution
To run tests in parallel (requires `pytest-xdist`):
```
pip install pytest-xdist
pytest -n 2
```
You can also combine it with browser selection:
```
pytest -n 4 --browser_name=chromium
```
### 📁 View Report
HTML report is generated in the `report/` directory:
```
open report/report.html
```
## 👨‍💻 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.
