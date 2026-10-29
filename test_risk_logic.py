
from risk_logic import calculate_risk


def test_high_risk_report():
    result = calculate_risk(
        failed_jobs=3,
        data_quality_score=75,
        recent_changes=2
    )

    assert result["risk_score"] == 55
    assert result["risk_level"] == "High"


def test_low_risk_report():
    result = calculate_risk(
        failed_jobs=0,
        data_quality_score=95,
        recent_changes=0
    )

    assert result["risk_score"] == 0
    assert result["risk_level"] == "Low"


def test_medium_risk_report():
    result = calculate_risk(
        failed_jobs=2,
        data_quality_score=85,
        recent_changes=1
    )

    assert result["risk_score"] == 30
    assert result["risk_level"] == "Medium"
