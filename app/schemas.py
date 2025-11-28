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
    detected_type: Optional[str] = Field(None, description="Detected document type (e.g., pdf_scientific, handwritten, json, markdown)")
    processing_time_ms: Optional[float] = Field(None, description="Time taken to process the document in milliseconds")
    extra: Optional[Dict[str, Any]] = Field(default_factory=dict, description="Additional metadata")

class JobOutput(BaseModel):
    job_id: UUID = Field(..., description="Unique identifier for the job")
    status: JobStatus = Field(..., description="Current status of the job")
    original_filename: str = Field(..., description="Name of the original uploaded file")
    cleaned_text: Optional[str] = Field(None, description="Full narrative cleaned text")
    chunks: List[str] = Field(default_factory=list, description="List of text chunks")
    metadata: JobMetadata = Field(default_factory=JobMetadata, description="Metadata associated with the job")

class InputPayload(BaseModel):
    data: Any = Field(..., description="Raw input data (dict, list, or string) to be cleaned")
    filename: str = Field("raw_input", description="Identifier for the input data")

