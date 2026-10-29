
def calculate_risk(failed_jobs, data_quality_score, recent_changes):
    failed_job_points = min(failed_jobs * 5, 30)

    if data_quality_score < 80:
        data_quality_points = 30
    elif data_quality_score < 90:
        data_quality_points = 15
    else:
        data_quality_points = 0

    change_points = min(recent_changes * 5, 20)

    risk_score = (
        failed_job_points
        + data_quality_points
        + change_points
    )

    if risk_score >= 50:
        risk_level = "High"
    elif risk_score >= 25:
        risk_level = "Medium"
    else:
        risk_level = "Low"

    return {
        "risk_score": risk_score,
        "risk_level": risk_level,
        "score_breakdown": {
            "failed_job_points": failed_job_points,
            "data_quality_points": data_quality_points,
            "change_points": change_points
        }
    }
