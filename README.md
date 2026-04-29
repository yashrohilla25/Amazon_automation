# 🛒 Amazon Automation Testing (Playwright + Python)

## 📌 Project Overview

This project demonstrates automated end-to-end testing of key e-commerce workflows on Amazon using Playwright with Python.
The automation covers product search, price extraction, and cart functionality, executed in parallel to improve efficiency.


## 🎯 Test Scenarios

### ✅ Test Case 1

* Navigate to Amazon.com
* Search for **iPhone**
* Select first product
* Extract and print price
* Add product to cart

### ✅ Test Case 2

* Navigate to Amazon.com
* Search for **Samsung Galaxy device**
* Select first product
* Extract and print price
* Add product to cart

---

## ⚙️ Technologies Used

* **Language:** Python
* **Automation Tool:** Playwright
* **Test Framework:** Pytest
* **Parallel Execution:** pytest-xdist

---

## 🚀 Features Implemented

* Automated browser interactions
* Dynamic element handling (Amazon UI changes)
* Popup handling (location/address modal)
* New tab handling
* Robust selectors for price extraction
* Parallel test execution
* Console logging of product price

---

## 🛠 Setup Instructions

1. Clone the repository:

   ```bash
   git clone <your-repo-link>
   cd amazon-automation
   ```

2. Create virtual environment:

   ```bash
   py -m venv venv
   venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Install Playwright browsers:

   ```bash
   playwright install
   ```

---

## ▶️ Running Tests

Run tests in parallel:

```bash
pytest -n 2
```

---

## 📊 Output

* Product prices are printed in the console
* Browser opens and performs actions visually
* Tests run concurrently for faster execution

---

## ⚠️ Notes

* Amazon UI is dynamic and may change, requiring selector updates
* Occasional popups (like location selection) are handled in the script
* Tests are run in non-headless mode for visibility

---

## 📁 Project Structure

```
amazon-automation/
│
├── test_amazon.py
├── requirements.txt
├── README.md
└── venv/
```

---

## 👨‍💻 Author

Developed as part of an automation assessment to demonstrate:

* UI automation skills
* Problem-solving approach
* Handling real-world web challenges

---
