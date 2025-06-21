import boto3

codebuild = boto3.client('codebuild')

project_name = "LambdaCodeBuildProject"
source_repo = "https://github.com/Pramit-on-Cloud079/AWS_Lambda_CICD_Project.git"
s3_bucket = "codepipeline-artifacts-pramit"
codebuild_role_arn = "arn:aws:iam::231299271232:role/CodeBuildServiceRole"

response = codebuild.create_project(
    name=project_name,
    source={
        'type': 'GITHUB',
        'location': source_repo,
        'buildspec': 'buildspec.yml'
    },
    artifacts={
        'type': 'S3',
        'location': s3_bucket,
        'packaging': 'ZIP',
        'path': 'build_artifacts'
    },
    environment={
        'type': 'LINUX_CONTAINER',
        'image': 'aws/codebuild/standard:7.0',
        'computeType': 'BUILD_GENERAL1_SMALL',
        'environmentVariables': [],
        'privilegedMode': False
    },
    serviceRole=codebuild_role_arn,
    timeoutInMinutes=10
)

print("✅ CodeBuild project created:", response['project']['arn'])
