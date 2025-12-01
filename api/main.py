from fastapi import FastAPI, UploadFile
import pandas as pd
from core.transformer import DataTransformer
from core.audit import AuditLogger

app = FastAPI()

transformer = DataTransformer()
audit = AuditLogger()

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/upload")
async def upload(file: UploadFile):
    if file.filename.endswith(".csv"):
        df = pd.read_csv(file.file)
    elif file.filename.endswith(".json"):
        df = pd.read_json(file.file)
    else:
        return {"error": "Unsupported file format"}

    anonymized = transformer.anonymize(df)
    audit.log("File processed", file.filename)
    return {"rows": len(anonymized), "preview": anonymized.head().to_dict()}
