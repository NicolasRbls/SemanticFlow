# SemanticFlow - Project Roadmap

## Phase 1: MVP "Texte Structuré" (Current Focus)
**Objectif :** Gérer le JSON, Markdown, et HTML sale. Sortie propre et narrée.

### Architecture & Setup
- [x] Define Project Structure
- [x] Create `app/schemas.py` (Pydantic Models)
- [x] Create `app/core/config.py` (Settings)
- [x] Create `app/core/exceptions.py` (Custom Exceptions)
- [x] Create `app/main.py` (FastAPI Skeleton)

### Core Features (MVP)
- [ ] **Strict Output Compliance**: Update API to return `JobOutput` format (job_id, status, metadata...).
- [ ] **File Ingestion**: Implement `POST /upload` for .json, .md, .html files.
- [ ] **Flattener Module**:
    - [x] Recursive JSON cleaner (Basic).
    - [ ] Improve Markdown/HTML stripping.
- [ ] **LLM Integration ("Semantic Smoothing")**:
    - [ ] Setup LLM Client (Groq/Ollama/OpenAI compatible).
    - [ ] Create "Smoothing" prompt (JSON -> Narrative Text).
    - [ ] Integrate LLM step into the cleaning pipeline.

## Phase 2: Module "Science & Structure"
**Objectif :** Gérer les PDF complexes, LaTeX et formules scientifiques.

- [ ] **General Parsing**: Integrate `unstructured` library.
- [ ] **Scientific PDF**: Integrate `nougat` or `marker` for LaTeX detection.
- [ ] **Math Handling**: Implement logic to choose between LaTeX raw output or Text description.
- [ ] **Table Extraction**: Detect tables and convert to Markdown/CSV or narrative description.

## Phase 3: Module "Vision"
**Objectif :** Écriture manuscrite et scans.

- [ ] **Image Pre-processing**: OpenCV (denoising, contrast).
- [ ] **OCR Pipeline**: Integrate `PaddleOCR` or `TrOCR`.
- [ ] **OCR Correction**: LLM pass to fix OCR typos.

## Phase 4: Industrialisation & Async
**Objectif :** Robustesse et passage à l'échelle.

- [ ] **Async Queue**: Setup Redis + Celery (or ARQ).
- [ ] **Job Management**: Endpoints for Job Status/Result polling.
- [ ] **Docker**: Create Dockerfile (API) and Docker Compose (API + Worker + Redis).
- [ ] **Error Handling**: Robust management of corrupted files and timeouts.
- [ ] **Documentation**: Swagger/ReDoc polish + Developer Guide.

## Phase 5: Testing & Quality
- [ ] **Unit Tests**: Complete coverage for Schemas and Cleaner.
- [ ] **Integration Tests**: Test full API flows.
- [ ] **CI/CD**: Github Actions pipeline.
