from fastapi import APIRouter, UploadFile
import pandas as pd
from core.transformer import DataTransformer
from core.audit import AuditLogger
from api.models import UploadResponse

router = APIRouter()

# Instantiate transformer and audit logger
transformer = DataTransformer()
audit = AuditLogger()

@router.get("/health", response_model=dict)
def health_check():
    """Simple health check endpoint."""
    return {"status": "ok"}

@router.post("/upload", response_model=UploadResponse)
async def upload(file: UploadFile):
    """Upload CSV/JSON file, anonymize PII, and log the action."""
    if file.filename.endswith(".csv"):
        df = pd.read_csv(file.file)
    elif file.filename.endswith(".json"):
        df = pd.read_json(file.file)
    else:
        return {"error": "Unsupported file format"}

    anonymized = transformer.anonymize(df)
    audit.log("File processed", file.filename)

    return UploadResponse(
        rows=len(anonymized),
        preview=anonymized.head().to_dict()
    )
