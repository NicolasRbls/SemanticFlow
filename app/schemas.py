from enum import Enum
from typing import List, Optional, Dict, Any
from uuid import UUID
from pydantic import BaseModel, Field

class JobStatus(str, Enum):
    QUEUED = "queued"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"

class JobMetadata(BaseModel):
    page_count: Optional[int] = Field(None, description="Number of pages in the document")
    detected_type: Optional[str] = Field(None, description="Detected document type (e.g., pdf_scientific, handwritten)")
    processing_time_ms: Optional[float] = Field(None, description="Time taken to process the document in milliseconds")
    extra: Optional[Dict[str, Any]] = Field(default_factory=dict, description="Additional metadata")

class JobOutput(BaseModel):
    job_id: UUID = Field(..., description="Unique identifier for the job")
    status: JobStatus = Field(..., description="Current status of the job")
    original_filename: str = Field(..., description="Name of the original uploaded file")
    cleaned_text: Optional[str] = Field(None, description="Full narrative cleaned text")
    chunks: List[str] = Field(default_factory=list, description="List of text chunks")
    metadata: JobMetadata = Field(default_factory=JobMetadata, description="Metadata associated with the job")

class JobRequest(BaseModel):
    filename: str = Field(..., description="Name of the file being uploaded")
    # In a real upload, the file content would be handled separately (e.g., UploadFile in FastAPI)
    # This schema might be used for metadata or pre-signed URL flows if applicable.
    # For a direct multipart/form-data upload, this might not be strictly used as a body model,
    # but it's good to have for type definition.

class InputPayload(BaseModel):
    data: Any = Field(..., description="Raw input data (dict, list, or string) to be cleaned")

class OutputResponse(BaseModel):
    cleaned_data: str = Field(..., description="The cleaned, narrative string representation of the input data")
