# Amazon Test Automation Pipeline

Amazon Test Automation Pipeline is a lightweight, Python-based test framework using Selenium and pytest to validate the Amazon homepage. It runs in a Docker container and integrates with GitHub Actions for CI/CD, enabling headless browser testing, fast feedback, and HTML reporting. This project showcases Agile testing and modern automation best practices.


## ✅ Features

- Headless browser testing using Selenium WebDriver
- Pytest-based test execution
- GitHub Actions CI pipeline with Docker
- HTML and JUnit test reports
- Modular and maintainable test structure

## 📁 Project Structure


## 🚀 Getting Started

### Prerequisites

- Python 3.10+ installed
- Google Chrome installed (for local execution)
- `pip` and virtualenv (optional)
- Docker (optional, for containerized runs)

### 1. Clone the Repository

```bash
git clone https://github.com/MarwanSultan/amazon_test_automation_pipeline.git
cd amazon_test_automation_pipeline

#### 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

### 3. Install dependencies
pip install -r requirements.txt

### 4. Run the tests
pytest

# To generate an HTML test report
pytest --html=report.html

# (Optional) Run tests inside Docker
docker build -t amazon-test .
docker run --rm amazon-test

