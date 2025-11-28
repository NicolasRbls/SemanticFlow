# SemanticFlow - Project Roadmap

## Phase 1: Architecture & Setup (Current)
- [x] Define Project Structure (Folders & Files)
- [x] Create `app/schemas.py` (Pydantic Models)
- [x] Create `app/core/config.py` (Settings)
- [x] Create `app/core/exceptions.py` (Custom Exceptions)
- [x] Create `app/main.py` (FastAPI Skeleton)

## Phase 2: Core Logic (ETL Pipeline)
- [ ] Implement Document Ingestion Endpoint (POST /upload)
- [ ] Setup Redis + Celery/ARQ for async processing
- [ ] Integrate `unstructured` for general parsing
- [ ] Integrate `nougat`/`marker` for scientific PDFs
- [ ] Integrate OCR (`paddleocr`/`trocr`)
- [ ] Implement LLM "Semantic Smoothing"

## Phase 3: Testing & Quality
- [ ] Setup `pytest` framework
- [ ] Write Unit Tests for Schemas
- [ ] Write Integration Tests for API
- [ ] CI/CD Pipeline Setup

## Phase 4: Documentation
- [ ] API Documentation (Swagger/ReDoc)
- [ ] Developer Guide
