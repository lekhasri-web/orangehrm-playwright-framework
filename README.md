# orangehrm-playwright-framework
A parallelized automated UI and API test automation framework for OrangeHRM using Python, Pytest, Playwright, and Pytest-Xdist.


# OrangeHRM Test Automation Framework 🚀

A highly parallelized, hybrid UI and API test automation framework built for the OrangeHRM platform using Python, Playwright, and Pytest.

---

## 🛠️ Tech Stack & Features

* **Language:** Python 3.12+
* **Test Runner:** Pytest
* **Automation Engine:** Playwright (Synchronous API)
* **Parallel Execution:** pytest-xdist (runs tests across multiple CPU cores)
* **Design Pattern:** Page Object Model (POM)
* **Reporting:** Built-in HTML reports with automated failure screenshots

---

## 📂 Project Structure

```text
├── api/                  # API Client Layer for backend verification
├── config/               # Global constants & application configurations
├── pages/                # Page Object Model (POM) element locators & actions
├── tests/                # UI and API test suites
│   └── conftest.py       # Shared Pytest fixtures and browser setups
├── .gitignore            # Excluded directories (venv, cache, reports)
├── pytest.ini            # Configuration profiles & parallelization execution flags
└── requirements.txt      # Project library dependencies

