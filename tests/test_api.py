from fastapi.testclient import TestClient
from app.main import app
from app.schemas import JobOutput, JobStatus
import uuid

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to SemanticFlow API"}

def test_schema_validation():
    # Test that we can instantiate the JobOutput model
    job = JobOutput(
        job_id=uuid.uuid4(),
        status=JobStatus.COMPLETED,
        original_filename="test.pdf",
        cleaned_text="Some text",
        chunks=["chunk1"],
        metadata={"page_count": 1}
    )
    assert job.status == JobStatus.COMPLETED
    assert job.original_filename == "test.pdf"
