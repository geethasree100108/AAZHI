
from fastapi import FastAPI

from schemas.models import AssessmentRequest
from assessment.assessment import assess_multiple_villages

app = FastAPI(
    title="EQUIFLOW API",
    description="AI-Powered Fair Resource Distribution",
    version="1.0.0"
)

# Store the latest assessment results temporarily
priority_results = []


@app.get("/")
def home():
    return {
        "message": "Welcome to EQUIFLOW API",
        "status": "Running successfully"
    }


# API 1: Assess village needs
@app.post("/assess-needs")
def assess_needs(request: AssessmentRequest):

    global priority_results

    priority_results = assess_multiple_villages(
        request.villages
    )

    return {
        "message": "Village assessment completed successfully",
        "total_villages": len(priority_results),
        "results": priority_results
    }


# API 2: Retrieve priority results
@app.get("/priority-results")
def get_priority_results():

    return {
        "total_villages": len(priority_results),
        "results": priority_results
    }
