from fastapi.testclient import TestClient
from app.main import app
from app.schemas import JobOutput, JobStatus
import io
import json

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to SemanticFlow API"}

def test_clean_endpoint_strict_output():
    payload = {"data": {"key": "value"}, "filename": "test_payload.json"}
    response = client.post("/clean", json=payload)
    assert response.status_code == 200
    
    data = response.json()
    # Validate against Pydantic model implicitly by checking fields
    assert "job_id" in data
    assert data["status"] == "completed"
    assert data["original_filename"] == "test_payload.json"
    assert data["cleaned_text"] == "key: value."
    assert data["metadata"]["detected_type"] == "json/raw"

def test_upload_json_file():
    file_content = json.dumps({"title": "Test JSON", "body": "Content"})
    files = {"file": ("test.json", io.BytesIO(file_content.encode("utf-8")), "application/json")}
    
    response = client.post("/upload", files=files)
    assert response.status_code == 200
    
    data = response.json()
    assert data["status"] == "completed"
    assert data["original_filename"] == "test.json"
    assert "title: Test JSON. body: Content." in data["cleaned_text"]
    assert data["metadata"]["detected_type"] == "json"

def test_upload_markdown_file():
    file_content = "# Header\n\n*List item*"
    files = {"file": ("test.md", io.BytesIO(file_content.encode("utf-8")), "text/markdown")}
    
    response = client.post("/upload", files=files)
    assert response.status_code == 200
    
    data = response.json()
    assert data["status"] == "completed"
    assert data["cleaned_text"] == "Header List item"
    assert data["metadata"]["detected_type"] == "markdown"

def test_upload_html_file():
    file_content = "<html><body><h1>Title</h1><p>Paragraph</p></body></html>"
    files = {"file": ("test.html", io.BytesIO(file_content.encode("utf-8")), "text/html")}
    
    response = client.post("/upload", files=files)
    assert response.status_code == 200
    
    data = response.json()
    assert data["status"] == "completed"
    assert "Title Paragraph" in data["cleaned_text"]
    assert data["metadata"]["detected_type"] == "html"

