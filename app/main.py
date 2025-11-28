from fastapi import FastAPI, HTTPException, UploadFile, File
from app.core.config import settings
from app.schemas import InputPayload, JobOutput, JobStatus, JobMetadata
from app.core.cleaner import recursive_cleaner
import uuid
import json
import time

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

@app.get("/")
async def root():
    return {"message": "Welcome to SemanticFlow API"}

@app.post("/clean", response_model=JobOutput)
async def clean_data(payload: InputPayload):
    """
    Clean raw data into a narrative string using the recursive cleaner.
    Returns a strict JobOutput format.
    """
    start_time = time.time()
    try:
        cleaned_text = recursive_cleaner(payload.data)
        processing_time = (time.time() - start_time) * 1000
        
        return JobOutput(
            job_id=uuid.uuid4(),
            status=JobStatus.COMPLETED,
            original_filename=payload.filename,
            cleaned_text=cleaned_text,
            chunks=[cleaned_text], # For MVP, simple single chunk
            metadata=JobMetadata(
                detected_type="json/raw",
                processing_time_ms=processing_time
            )
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing data: {str(e)}")

@app.post("/upload", response_model=JobOutput)
async def upload_file(file: UploadFile = File(...)):
    """
    Upload a file (JSON, Markdown, HTML) and clean it.
    """
    start_time = time.time()
    try:
        content = await file.read()
        filename = file.filename
        file_extension = filename.split(".")[-1].lower() if "." in filename else ""
        
        data_to_clean = None
        detected_type = "unknown"
        
        if file_extension == "json":
            detected_type = "json"
            try:
                data_to_clean = json.loads(content)
            except json.JSONDecodeError:
                raise HTTPException(status_code=400, detail="Invalid JSON file")
        elif file_extension in ["md", "markdown"]:
            detected_type = "markdown"
            data_to_clean = content.decode("utf-8")
        elif file_extension in ["html", "htm"]:
            detected_type = "html"
            data_to_clean = content.decode("utf-8")
        else:
            # Fallback for text files
            detected_type = "text"
            try:
                data_to_clean = content.decode("utf-8")
            except:
                 raise HTTPException(status_code=400, detail="Unsupported file type or encoding")

        cleaned_text = recursive_cleaner(data_to_clean)
        processing_time = (time.time() - start_time) * 1000
        
        return JobOutput(
            job_id=uuid.uuid4(),
            status=JobStatus.COMPLETED,
            original_filename=filename,
            cleaned_text=cleaned_text,
            chunks=[cleaned_text],
            metadata=JobMetadata(
                detected_type=detected_type,
                processing_time_ms=processing_time
            )
        )

    except HTTPException as he:
        raise he
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing file: {str(e)}")
