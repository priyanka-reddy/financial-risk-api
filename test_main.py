
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["status"] == "success"


def test_valid_report():
    response = client.post(
        "/report",
        json={
            "report_name": "Quarterly Capital Report",
            "failed_jobs": 3,
            "data_quality_score": 75,
            "recent_changes": 2
        }
    )

    assert response.status_code == 200
    assert response.json()["risk_score"] == 55
    assert response.json()["risk_level"] == "High"


def test_invalid_data_quality_score():
    response = client.post(
        "/report",
        json={
            "report_name": "Quarterly Capital Report",
            "failed_jobs": 3,
            "data_quality_score": 120,
            "recent_changes": 2
        }
    )

    assert response.status_code == 422


def test_negative_failed_jobs():
    response = client.post(
        "/report",
        json={
            "report_name": "Quarterly Capital Report",
            "failed_jobs": -3,
            "data_quality_score": 75,
            "recent_changes": 2
        }
    )

    assert response.status_code == 422
