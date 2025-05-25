# QA Portfolio: Selenium + Pytest Automated Login Testing

This is a test automation project that demonstrates both **technical skills** and **QA thinking** using the [SauceDemo](https://www.saucedemo.com/) website as a test target.

The goal is to go beyond simple "happy path" automation and show **real tester mindset**, including:
- Valid input testing
- Invalid input coverage
- Edge case scenarios
- Assertions based on expected behavior

---

## ⚙️ Technologies Used

- Python
- Selenium WebDriver
- Pytest
- Pytest plugins (`pytest-html`, `pytest-md`)
- Page Object Model (POM)

---

## 🧪 Test Scenarios Covered

### ✅ Valid Login Tests
- Run against multiple user types (e.g., `standard_user`, `problem_user`)
- Assert that the user is successfully logged in by checking for presence of `"app_logo"`

### ❌ Invalid Login Tests
Tests that check how the system handles improper input, including:
- Empty username/password
- SQL injection (`' OR '1'='1`)
- XSS injection (`<script>alert(1)</script>`)
- Excessively long strings
- Special characters
- Invalid credentials

Each test asserts that an **error message appears**, and documents which user types are expected to fail.

---

## 🧠 Test Strategy

- Page Object Model is used for abstraction and code reuse.
- Parametrization is used for data-driven testing.
- Assertions verify expected login outcomes (positive and negative).
- Failure cases are logged with detailed messages.

---

## 📁 Project Structure

- `selenium_project/`
  - `pages/`
    - `__init__.py`
    - `login_page.py` – Page Object for login form
  - `tests/`
    - `__init__.py`
    - `test_login_valid.py` – Tests expected to succeed
    - `test_login_invalid.py` – Tests expected to fail
  - `conftest.py` – Pytest driver fixture
  - `requirements.txt`
  - `reports/`
    - `test_report.md` – Markdown report (via pytest-md)
    - `test_report.html` – HTML report (via pytest-html)
  - `README.md`

---

## ▶️ How to Run the Tests

1. Install dependencies

    pip install -r requirements.txt

2. Run the tests and generate reports

    pytest --md=reports/test_report.md --html=reports/test_report.html

---

## 📊 Sample Output

> You can view the test reports here:
> - reports/test_report.md
> - reports/test_report.html

---

## ✍️ Author

**Numair Kaukab**  
QA Tester & Automation Enthusiast  
