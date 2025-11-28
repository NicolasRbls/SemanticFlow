# PROJECT: SemanticFlow
# TYPE: API for RAG ETL (Extract, Transform, Load)

## 1. VISION
Une API qui prend des documents "sales" (PDF, JSON imbriqué, Markdown, Scans) et renvoie un JSON propre, structuré et narratif, optimisé pour l'ingestion dans une Base Vectorielle (RAG).

## 2. ARCHITECTURE CIBLE
- **Langage:** Python 3.11+
- **Framework:** FastAPI (Asynchrone)
- **Task Queue:** Redis + Celery/ARQ
- **AI/Parsing:**
  - `unstructured` (General parsing)
  - `nougat` / `marker` (Science & Math PDF)
  - `paddleocr` / `trocr` (Handwritten)
  - LLM Local (via Ollama/vLLM) ou API pour le "lissage sémantique".

## 3. FORMAT DE SORTIE (STRICT)
L'API doit toujours renvoyer ce format :
{
  "job_id": "uuid",
  "status": "completed",
  "original_filename": "doc.pdf",
  "cleaned_text": "Texte narratif complet...",
  "chunks": ["segment 1...", "segment 2..."],
  "metadata": { "page_count": 5, "detected_type": "pdf_scientific" }
}

## 4. RÈGLES DE DÉVELOPPEMENT (AGENTS GUIDELINES)
1. **Type Hinting:** Tout le code Python doit être fortement typé.
2. **Docstrings:** Google Style docstrings pour chaque fonction.
3. **Tests:** Pas de code sans test `pytest` associé.
4. **Erreurs:** Ne jamais crash silencieusement. Utiliser des Custom Exceptions.