
# Secure Data Transformation Service

[![CI/CD](https://github.com/supritkulkarni/PIIShield/actions/workflows/ci.yml/badge.svg)](https://github.com/supritkulkarni/PIIShield/actions/workflows/ci.yml)


A Python + FastAPI service that ingests raw CSV/JSON datasets, sanitizes PII, and outputs anonymized data.

## Features
- PII anonymization (emails, phones, DOB)
- AES encryption for sensitive fields
- Audit logging
- REST API endpoints
- Dockerized & deployable to GCP CloudRun

## Quickstart
```bash
pip install -r requirements.txt
uvicorn api.main:app --reload
