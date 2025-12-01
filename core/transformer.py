import pandas as pd
from cryptography.fernet import Fernet

class DataTransformer:
    def __init__(self, key: bytes = Fernet.generate_key()):
        self.cipher = Fernet(key)

    def anonymize(self, df: pd.DataFrame) -> pd.DataFrame:
        if "email" in df.columns:
            df["email"] = df["email"].apply(lambda x: self.cipher.encrypt(x.encode()).decode())
        if "phone" in df.columns:
            df["phone"] = df["phone"].apply(lambda x: "XXX-XXX-" + str(x)[-4:])
        if "dob" in df.columns:
            df["dob"] = pd.to_datetime(df["dob"]).dt.year.apply(lambda y: f"{y//10*10}s")
        return df
