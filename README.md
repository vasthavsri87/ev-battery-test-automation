# EV Battery Test Automation Framework

A lightweight Python/Pytest framework for automated testing of EV battery controller behavior.

## Overview

This project simulates an EV battery controller and uses a Python/Pytest
automation framework to validate expected system behavior.

The framework currently supports:

- Battery level validation
- Charging behavior testing
- Boundary-condition testing
- Temperature safety testing
- Parametrized test execution
- Structured logging
- HTML test reporting
- Automated PASS/FAIL validation

## Project Structure

```text
ev-battery-test-automation/
│
├── battery/
│   └── battery_controller.py
│
├── tests/
│   ├── test_battery.py
│   └── test_charging.py
│
├── utils/
│   └── logger.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

## Technologies

- Python
- Pytest
- pytest-html
- Object-Oriented Programming (OOP)
- Python Logging
- Git/GitHub
- Linux-compatible test execution

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/vasthavsri87/ev-battery-test-automation.git
cd ev-battery-test-automation
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the automated test suite

```bash
python -m pytest
```

## Test Coverage

The current test suite validates:

- Valid battery-level ranges
- Charging initiation
- Charging behavior
- Full-battery protection
- Battery boundary conditions
- Multiple battery states

## Test Results

The current test suite contains **12 automated tests**, all passing successfully.

```text
12 passed
```

HTML reports can be generated using:

```bash
python -m pytest --html=report.html
```

The generated report and its supporting assets are excluded from Git tracking.

## Future Improvements

The framework can be extended with:

- Temperature safety test automation
- Structured logging
- HTML test reports
- GitHub Actions CI/CD
- Simulated vehicle/ECU communication
- Database integration for storing test results