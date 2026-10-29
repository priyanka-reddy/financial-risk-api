
from fastapi import FastAPI
from pydantic import BaseModel, Field

from risk_logic import calculate_risk

app = FastAPI(title="Financial Reporting Risk API")


class ReportInput(BaseModel):
    report_name: str
    failed_jobs: int = Field(ge=0)
    data_quality_score: float = Field(ge=0, le=100)
    recent_changes: int = Field(ge=0)


@app.get("/")
def home():
    return {
        "message": "Financial Reporting Risk API is running",
        "status": "success"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "financial-reporting-risk-api",
        "version": "1.0.0"
    }


@app.post("/report")
def evaluate_report(report: ReportInput):
    result = calculate_risk(
        failed_jobs=report.failed_jobs,
        data_quality_score=report.data_quality_score,
        recent_changes=report.recent_changes
    )

    return {
        "report_name": report.report_name,
        **result
    }
