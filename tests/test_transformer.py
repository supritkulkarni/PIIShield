import pandas as pd
from core.transformer import DataTransformer

def test_anonymize_dataframe():
    df = pd.DataFrame({
        "email": ["alice@example.com"],
        "phone": ["5551234567"],
        "dob": ["1990-05-14"]
    })
    transformer = DataTransformer()
    anonymized = transformer.anonymize(df)

    assert anonymized["email"].iloc[0] != "alice@example.com"
    assert anonymized["phone"].iloc[0].startswith("XXX-XXX-")
    assert anonymized["dob"].iloc[0].endswith("s")
