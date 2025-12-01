import pandas as pd
from core.transformer import DataTransformer

def test_sample_csv():
    df = pd.read_csv("data/sample.csv")
    transformer = DataTransformer()
    anonymized = transformer.anonymize(df)

    # Ensure anonymization happened
    assert anonymized["email"].iloc[0] != df["email"].iloc[0]
    assert anonymized["phone"].iloc[1].startswith("XXX-XXX-")
    assert anonymized["dob"].iloc[2].endswith("s")
