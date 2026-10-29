# Financial Reporting Risk API

A REST API built with Python and FastAPI to evaluate operational risks in financial reporting systems using a rule-based scoring approach.

## Overview

Financial reporting systems depend on reliable data processing, scheduled jobs, and controlled production changes. Failures in these areas can affect the completeness and reliability of reports.

This project provides an API that accepts report-related operational metrics and returns a risk score, risk classification, and breakdown of contributing factors.

**Note:** The current scoring logic is illustrative and is not a validated financial risk model.

## Features

- REST API built with FastAPI
- Input validation using Pydantic
- Rule-based risk scoring
- Low, Medium, and High risk classifications
- Breakdown of individual scoring components
- Automated API and unit tests using pytest

## Technology Stack

- Python 3.11
- FastAPI
- Pydantic
- Uvicorn
- pytest
- HTTPX

## Project Structure

```text
financial-risk-api/
├── main.py
├── risk_logic.py
├── test_main.py
├── test_risk_logic.py
├── .gitignore
└── README.md
```

## Setup and Installation

Activate the Conda environment:

```bash
conda activate financial-risk-api
```

Install the required packages if they are not already installed:

```bash
pip install fastapi uvicorn pytest httpx
```

## Run the API

From the project directory, run:

```bash
python -m uvicorn main:app --reload
```

The API will be available at:

`http://127.0.0.1:8000`

Interactive API documentation:

`http://127.0.0.1:8000/docs`

Health check:

`http://127.0.0.1:8000/health`

## Example Request

Send a POST request to `/report` with this JSON input:

```json
{
  "report_name": "Quarterly Regulatory Report",
  "failed_jobs": 3,
  "data_quality_score": 75,
  "recent_changes": 2
}
```

## Example Response

```json
{
  "report_name": "Quarterly Regulatory Report",
  "risk_score": 55,
  "risk_level": "High",
  "score_breakdown": {
    "failed_job_points": 15,
    "data_quality_points": 30,
    "change_points": 10
  }
}
```

## Run Tests

Execute the test suite from the project directory:

```bash
python -m pytest -v
```

The tests cover risk-scoring logic, successful API responses, and invalid input handling.

## Future Improvements

- Integrate a trained machine-learning model for risk prediction.
- Add structured logging and improved error handling.
- Introduce persistent storage for report metrics and risk assessments.
- Containerize the application with Docker.
- Add API authentication and deployment configuration.

## Disclaimer

This project is for educational and portfolio purposes. The scoring rules are illustrative and should not be used to make actual financial, regulatory, or operational risk decisions.
