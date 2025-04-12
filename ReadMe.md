# 📁 Serverless File Sharing App using AWS

This is a simple serverless file-sharing system built with AWS services like **Lambda**, **API Gateway**, **S3**, and **HTML frontend**.

## 🚀 Features

- Upload a file using a pre-signed URL (GET API via Lambda)
- Download files using a pre-signed URL (GET API via Lambda)
- HTML interface to easily interact with the system
- All files are stored securely in an S3 bucket

---

## 🏗️ Architecture

- **Frontend**: Static HTML + CSS hosted in S3 (Public)
- **Backend**: Two Lambda functions triggered by **API Gateway GET methods**
  - `/upload`: Returns a pre-signed upload URL
  - `/download?filename=FILENAME`: Returns a pre-signed download URL
- **Storage**: AWS S3 Bucket (e.g. `my-serverless-files-akash`)

---

## 📁 Repository Structure

