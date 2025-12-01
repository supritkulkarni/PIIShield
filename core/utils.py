import pandas as pd

def normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Normalize PII-related columns to consistent types:
    - email, phone → string
    - dob → datetime
    """
    df = df.copy()

    if "email" in df.columns:
        df["email"] = df["email"].astype(str)

    if "phone" in df.columns:
        df["phone"] = df["phone"].astype(str)

    if "dob" in df.columns:
        df["dob"] = pd.to_datetime(df["dob"], errors="coerce")

    return df
