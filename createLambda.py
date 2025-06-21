import boto3 
import zipfile
import os

lambda_client = boto3.client('lambda')
lambda_role_arn = "arn:aws:iam::231299271232:role/LambdaExecutionRole"

# Step 1: Create a dummy Lambda function folder and file
os.makedirs("dummy_lambda", exist_ok=True)
with open("dummy_lambda/lambda_function.py", "w") as f:
    f.write("def lambda_handler(event, context):\n    return {'statusCode': 200, 'body': 'Hello from Lambda'}")

# Step 2: Zip the function
with zipfile.ZipFile("lambda_payload.zip", "w") as zipf:
    zipf.write("dummy_lambda/lambda_function.py", arcname="lambda_function.py")

# Step 3: Create Lambda function
with open("lambda_payload.zip", "rb") as f:
    zipped_code = f.read()

response = lambda_client.create_function(
    FunctionName='resizeImageLambda',
    Runtime='python3.11',
    Role=lambda_role_arn,
    Handler='lambda_function.lambda_handler',
    Code={'ZipFile': zipped_code},
    Description='Initial dummy Lambda for CI/CD pipeline demo',
    Timeout=10,
    MemorySize=128,
    Publish=True
)

print("✅ Lambda function created:", response['FunctionArn'])
