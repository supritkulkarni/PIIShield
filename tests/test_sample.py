import pandas as pd
from core.transformer import DataTransformer

def test_sample_csv():
    df = pd.read_csv("data/sample.csv")
    original_email = df["email"].iloc[0]

    transformer = DataTransformer()
    anonymized = transformer.anonymize(df)

    assert anonymized["email"].iloc[0] != original_email
    assert anonymized["phone"].iloc[1].startswith("XXX-XXX-")
    assert anonymized["dob"].iloc[2].endswith("s")

