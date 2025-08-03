# API Automation Test

Automated API testing using Python, Pytest, and the public API [Reqres](https://reqres.in)

---
## 🤖 Tech Stack
```
    Python 3.8+
    Pytest – Test framework
    Requests – For making HTTP calls
```

---

## 🔧 Setup

1. 📥 **Clone the Repository**  
    ```bash
    git clone https://github.com/luckyandryan/fuse_automation.git
    ```

2. ➡️ **Move to the project directory**  
    ```bash
    cd fuse_automation
    ```

3. 🐍 **Install Python** *(if not already installed)*  
    Download and install Python 3.8+ from the [official Python website](https://www.python.org/downloads/).  
    *After installation, confirm with:*
    ```bash
    python --version
    ```

4. 🐍 **Create a Virtual Environment (Recommended)**  
    ```bash
    python -m venv venv
    ```

    *On macOS/Linux:*
    ```bash
    source venv/bin/activate
    ```

    *On Windows:*
    ```bash
    venv\Scripts\activate
    ```

5. 🔧 **Install Dependencies**  
    ```bash
    pip install -r requirements.txt
    ```

---

## 🚀 Run Tests

To execute the test, run command below:
```
source tests/execute_test.sh
```


---

## 📁 Project Structure
```
    fuse_automation/
    ├── api/
    │   └── reqres_api.py        # APIs
    ├── tests/
    │   └── execute_test.sh      # Shell script to execute tests
    │   └── pytest.ini           # Pytest config
    │   └── test_users_api.py    # Main test cases
    ├── utils/
    │   └── assertions.py        # Custom assertions
    ├── requirements.txt         # Dependencies
    └── README.md
```
