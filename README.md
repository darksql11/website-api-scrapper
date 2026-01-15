## 📡 Website API Endpoint Finder

A simple Python script that automatically detects and extracts dynamic API endpoints (e.g. `/api/view`, `/api/profile`) from a given website using Selenium and Selenium Wire.

Useful for security research, reverse engineering, and automation tasks.

---

### ⚙️ Requirements

- Python 3.7+
- Google Chrome
- ChromeDriver
- `selenium`
- `selenium-wire`
- `blinker`
- `certifi`
- `pyOpenSSL`
- `mitmproxy`

---

### 🚀 Installation

```bash
pip install selenium-wire webdriver-manager setuptools blinker==1.7.0
```

Make sure [ChromeDriver](https://chromedriver.chromium.org/downloads) is installed and matches your Chrome version.

---

### 📂 Usage

1. Edit the target URL in the script:

```python
target_url = 'https://target-website.com/'
```

2. Run the script:

```bash
python website_api_finder.py
```

3. Found API endpoints will be saved in a file named:

```
api_endpoints.txt
```

---

### 🛡 License

This project is licensed under the MIT License.\
Feel free to use, modify, and distribute.

---

### 📬 Contact

\
# Discord : DARKSQL11

