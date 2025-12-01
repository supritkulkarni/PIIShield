import pandas as pd
from cryptography.fernet import Fernet
from core.utils import normalize_columns

class DataTransformer:
    def __init__(self, key: bytes = Fernet.generate_key()):
        self.cipher = Fernet(key)

    def anonymize(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Return a new anonymized DataFrame without mutating the original.
        - email → encrypted
        - phone → masked (XXX-XXX-last4)
        - dob → decade bucket (e.g. 1990s)
        """
        df = normalize_columns(df)  # ensure types are consistent
        df = df.copy()              # avoid mutating caller's DataFrame

        if "email" in df.columns:
            df["email"] = df["email"].apply(
                lambda x: self.cipher.encrypt(x.encode()).decode()
            )

        if "phone" in df.columns:
            df["phone"] = df["phone"].apply(
                lambda x: "XXX-XXX-" + str(x)[-4:]
            )

        if "dob" in df.columns:
            df["dob"] = df["dob"].dt.year.apply(
                lambda y: f"{y//10*10}s" if pd.notnull(y) else None
            )

        return df
