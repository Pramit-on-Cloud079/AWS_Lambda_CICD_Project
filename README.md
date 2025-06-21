# 🚀 AWS Lambda CI/CD Pipeline with GitHub + CodePipeline + CodeBuild

This project demonstrates a fully automated **CI/CD pipeline for AWS Lambda**, using:
- ✅ GitHub (as the source)
- ✅ CodePipeline (to orchestrate)
- ✅ CodeBuild (to install dependencies, zip, and deploy Lambda)
- ✅ No manual console use

---

## 🧠 What It Does
Whenever you push code to the GitHub repo, this pipeline:
1. Pulls the latest code
2. Installs dependencies from `requirements.txt`
3. Zips the Lambda code and packages it
4. Deploys it to your AWS Lambda function (`resizeImageLambda`) **automatically**

---

## 📁 Folder Structure

CI-CD-Lambda-GitHub-Automation/
├── lambda_function/
│ ├── lambda_function.py ← Lambda code
│ └── requirements.txt ← Dependencies (e.g., Pillow)
├── buildspec.yml ← CodeBuild instructions
├── README.md

---

## ⚙️ Tech Stack
- AWS Lambda (Python 3.11)
- AWS CodePipeline
- AWS CodeBuild
- GitHub (trigger-based automation)
- Pillow (Python image processing)

---

## 📸 Sample Logs from CodeBuild

Installing dependencies...
pip install -r lambda_function/requirements.txt -t lambda_function/

Zipping Lambda function...
zip -r ../lambda.zip .

Deploying to Lambda...
aws lambda update-function-code --function-name resizeImageLambda --zip-file fileb://lambda.zip


---

## 🧪 Testing
To test the Lambda:
1. Upload a sample image to the trigger source (if configured).
2. It will be resized using Pillow and processed.

---

## ✅ Status
- CI/CD working ✅
- Dependencies installed ✅
- Automated Lambda deployment ✅

---

## 💼 Project Owner
👤 Pramit Dasgupta  
📌 AWS Cloud & Automation Enthusiast  