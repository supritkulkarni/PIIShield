from pydantic import BaseModel
from typing import Any, Dict

class UploadResponse(BaseModel):
    rows: int
    preview: Dict[str, Any]
