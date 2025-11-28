from fastapi import FastAPI, HTTPException
from app.core.config import settings
from app.schemas import InputPayload, OutputResponse
from app.core.cleaner import recursive_cleaner

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

@app.get("/")
async def root():
    return {"message": "Welcome to SemanticFlow API"}

@app.post("/clean", response_model=OutputResponse)
async def clean_data(payload: InputPayload):
    """
    Clean raw data into a narrative string using the recursive cleaner.
    """
    try:
        cleaned_text = recursive_cleaner(payload.data)
        return OutputResponse(cleaned_data=cleaned_text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing data: {str(e)}")
